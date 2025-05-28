import os
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
                hex(int.from_bytes(b''.join(generator.\
                            numbers[i*6:(i+1)*6])[:(size - len(string_value))//2], 'big'))[2:]

            with open(f'transaction_{i + 1}.bin', 'w') as f:
                f.write(data)
            transactions.append(bytearray(data, encoding="utf-8"))
        else:
            data = b''.join(generator.numbers[i*6:(i+1)*6])[:size]
            with open(f'transaction_{i + 1}.bin', 'wb') as f:
                f.write(data)
            transactions.append(data)
        print(f"  Создано: транзакция {i+1} => transaction_{i+1}.bin")

    return transactions

def create_block_header(transactions, prev_block_hash):
    # Метка времени
    now = datetime.now()
    hour = now.hour
    day = now.day
    month = now.month
    year = now.year % 100
    timestamp = struct.pack('BBBB', hour, day, month, year)

    # Размер блока (произвольные ненулевые байты)
    block_size = bytes([1, 2, 3, 4])

    # Хэш предыдущего блока
    prev_hash = prev_block_hash

    # Хэш корня Меркла
    merkle_tree = MerkleTree()
    transaction_hashes = [streebog(t, 256) for t in transactions]
    merkle_tree.put_hashes(transaction_hashes)
    merkle_root = merkle_tree.count_hash()

    return block_size, prev_hash, merkle_root, timestamp

def sign_transactions(transactions: list[bytes], seed: str) -> list[tuple[int, int]]:
        # Генерация ключей на основании seed
        x, P = keygen(seed)

        signatures = []
        # Подписание
        for i, msg in enumerate(transactions, start=1):
            R, s = sign(msg, x, P, seed)
            signatures.append((R, s))

            # Сохранение подписи
            data = int_to_bytes(R) + int_to_bytes(s)
            filename = f"signature_{i}.bin"
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"  Подписано: транзакция {i} => {filename}")

        return signatures, P

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

def combine(transactions : list, signs : list) -> list[bytes]:
    assert len(transactions) == len(signs)

    combined = []
    for i in range(len(transactions)):
        combined.append(transactions[i] + int_to_bytes(signs[i][0]) + int_to_bytes(signs[i][1]))
    return combined

if __name__ == "__main__":
    # ГПСЧ
    surname_name = "Gutnikov Dmitriy"
    generator = PRNG(surname_name, overall_iterations=16)

    # Создание транзакций
    print("\nСоздание транзакций")
    transactions = create_transactions(surname_name)


    # Подписывание транзакций
    print("\nПодпись транзакций")
    signs, P = sign_transactions(transactions, seed="Medvedev_Daniil")

    # Проверка первой подписи
    R0, s0 = signs[0]
    ok = verify(transactions[0], P, R0, s0)
    print("\nПервая подпись верна?", ok)

    # Создание заголовка блока
    prev_block_hash = generator.numbers[0]  # Первое число из ГПСЧ -> симуляция того, что мы в блокчейне
    combined = combine(transactions, signs) # Объединение транзакций и подписей
    block_size, prev_hash, merkle_root, timestamp = \
        create_block_header(combined, prev_block_hash) # Создание заголовка

    print("\nЗаголовок блока создан:")
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

    # Удаление вторичных файлов
    for i in "12345":
        os.remove(f"signature_{i}.bin")
        os.remove(f"transaction_{i}.bin")