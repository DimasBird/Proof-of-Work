from structs import MerkleTree
import struct
from hash_function import streebog
from pseudorandom_number_generator import PRNG
from datetime import datetime
from schnorr_signature import keygen, sign, int_to_bytes, verify, p
def create_transactions(string_value, num_transactions=5, size=200):
    generator = PRNG(surname_name, overall_iterations=num_transactions * 7)
    transactions = []
    for i in range(num_transactions):
        if i == 0:
            data = string_value[:size] if len(string_value) > size else string_value +\
                hex(int.from_bytes(b''.join(generator.numbers[i*6:(i+1)*6])[:(size - len(string_value))//2], 'big'))[2:]
            with open(f'transaction_{i + 1}.bin', 'w') as f:
                f.write(data)
            transactions.append(bytearray(data, encoding="utf-8"))
        else:
            data = b''.join(generator.numbers[i*6:(i+1)*6])[:size]
            with open(f'transaction_{i + 1}.bin', 'wb') as f:
                f.write(data)
            transactions.append(data)

    return transactions

def create_block_header(transactions, prev_block_hash):
    # Метка времени
    now = datetime.now()
    hour = now.hour  # Например, 0 (00:40)
    day = now.day  # Например, 23
    month = now.month  # Например, 5
    year = now.year % 100  # Например, 2025 -> 25
    timestamp = struct.pack('BBBB', hour, day, month, year)

    # Размер блока
    block_size = bytes([1, 2, 3, 4])

    # Хэш предыдущего блока
    prev_hash = prev_block_hash
    # Хэш корня Меркла
    merkle_tree = MerkleTree()
    transaction_hashes = [streebog(t, 256) for t in transactions]
    merkle_tree.put_hashes(transaction_hashes)
    merkle_root = merkle_tree.count_hash()

    # Начальный nonce
    nonce = 0
    return block_size, prev_hash, merkle_root, timestamp, nonce

def sign_transactions(transactions: list[bytes], seed: str) -> list[tuple[int, int]]:
        # 1. Генерация ключей
        x, P = keygen(seed)

        signatures = []
        # 2. Цикл подписания
        for i, msg in enumerate(transactions, start=1):
            R, s = sign(msg, x, P, seed)
            signatures.append((R, s))

            # 3. Сохранение подписи в файл
            data = int_to_bytes(R) + int_to_bytes(s)
            filename = f"signature_{i}.bin"
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"Подписано: транзакция {i} → {filename}")

        return signatures

def find_nonce(block_size, prev_hash, merkle_root, timestamp_):
    nonce = 0
    while nonce < 2**32:  # Ограничение 32-битного nonce
        header = block_size + prev_hash + merkle_root + timestamp_ + nonce.to_bytes(4, 'big')
        hash_result = streebog(header, 256)

        if hash_result[0] < 8:  # Проверка того, что в первый байт будет меньше 8 = 00000111 + 1
            return nonce, hash_result
        nonce += 1
        if nonce % 100000 == 0:
            print(f"Проверено {nonce} nonce...")
    raise ValueError("Не удалось найти nonce")

if __name__ == "__main__":
    # ГПСЧ
    surname_name = "Medvedev_Daniil"
    generator = PRNG(surname_name, overall_iterations=16)
    """print("Псевдослучайные числа:")
    for i in range(len(generator.numbers)):
        print(f"{i + 1}) {generator.numbers[i].hex()}")"""

    # Создание транзакций
    transactions = create_transactions(surname_name)
    print("Транзакции созданы\n")

    # Подписывание транзакций
    signs = sign_transactions(transactions, seed="Medvedev_Daniil")
    print("Транзакции подписаны\n")

    R0, s0 = signs[0]
    ok = verify(transactions[0], p, R0, s0)
    print (R0, s0)
    print("Первая подпись валидна?", ok)

    # Создание заголовка блока
    prev_block_hash = generator.numbers[0]  # Первое число из ГПСЧ -> симуляция того, что мы в блокчейне
    # !!!!!! Вместо transactions должно быть слияние
    # !!!!!! подписей и транзакций:
    # Грубо говоря: create_block_header(transactions || signs, prev_block_hash)
    block_size, prev_hash, merkle_root, timestamp, nonce = create_block_header(transactions, prev_block_hash)
    print("Заголовок блока создан:")
    print(f"  Размер блока: {block_size.hex()}")
    print(f"  Хэш предыдущего блока: {prev_hash.hex()}")
    print(f"  Хэш корня Меркла: {merkle_root.hex()}")
    print(f"  Метка времени: {timestamp.hex()}")


    # Поиск nonce
    try:
        nonce, block_hash = find_nonce(block_size, prev_hash, merkle_root, timestamp)
        print(f"\nНайден nonce: {nonce}")
        print(f"Хэш блока: {block_hash.hex()}")
    except ValueError as e:
        print(e)
