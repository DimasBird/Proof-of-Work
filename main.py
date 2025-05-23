from structs import MerkleTree
import struct
from hash_function import streebog
from pseudorandom_number_generator import PRNG
from datetime import datetime
def create_transactions(surname_name, num_transactions=5, size=200):
    generator = PRNG(surname_name, overall_iterations=num_transactions * 7)
    transactions = []
    for i in range(num_transactions):
        if i == 0:  # Первая транзакция с фамилией и именем
            data = surname_name.encode('utf-8')
            data = data[:size] if len(data) > size else data + generator.numbers[i][:size - len(data)]
        else:  # Остальные заполняются псевдослучайными данными
            data = b''.join(generator.numbers[i*6:(i+1)*6])[:size]
        transactions.append(data)
        with open(f'transaction_{i+1}.bin', 'wb') as f:
            f.write(data)
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

def find_nonce(block_size, prev_hash, merkle_root, timestamp_):
    nonce = 0
    while nonce < 2**32:  # Ограничение 32-битного nonce
        header = block_size + prev_hash + merkle_root + timestamp_ + nonce.to_bytes(4, 'big')
        hash_result = streebog(header, 256)

        if hash_result[0] == 0 and hash_result[1] == 0:  # Проверка того, что в первый байт будет меньше 8 = 00000111 + 1 <== ПЕРЕДЕЛАТЬ КОММЕНТАРИЙ
            return nonce, hash_result
        nonce += 1
        if nonce % 100000 == 0:
            print(f"Проверено {nonce} nonce...")
    raise ValueError("Не удалось найти nonce")

if __name__ == "__main__":
    # ГПСЧ
    surname_name = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
    generator = PRNG(surname_name, overall_iterations=16)
    print("Псевдослучайные числа:")
    for i in range(len(generator.numbers)):
        print(f"{i + 1}) {generator.numbers[i].hex()}")

    # Создание транзакций
    transactions = create_transactions(surname_name)
    print("Транзакции созданы")

    # Создание заголовка блока
    prev_block_hash = generator.numbers[0]  # Первое число из ГПСЧ
    block_size, prev_hash, merkle_root, timestamp, nonce = create_block_header(transactions, prev_block_hash)
    print("Заголовок блока создан:")
    print(f"Размер блока: {block_size.hex()}")
    print(f"Хэш предыдущего блока: {prev_hash.hex()}")
    print(f"Хэш корня Меркла: {merkle_root.hex()}")
    print(f"Метка времени: {timestamp.hex()}")


    # Поиск nonce
    try:
        nonce, block_hash = find_nonce(block_size, prev_hash, merkle_root, timestamp)
        print(f"Найден nonce: {nonce}")
        print(f"Хэш блока: {block_hash.hex()}")
    except ValueError as e:
        print(e)
