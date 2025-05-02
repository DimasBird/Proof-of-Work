import numpy as np
import galois

GF = galois.GF(2)

pi = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147,
      46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1,
      142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72,
      171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135,
      21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138, 126,
      109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3,
      224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26,
      184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88,
      179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83,
      170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
      116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

tau = (0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27, 35,
       43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7,
       15, 23, 31, 39, 47, 55, 63)

A = np.array([
    ["8e20faa72ba0b470", "47107ddd9b505a38", "ad08b0e0c3282d1c", "d8045870ef14980e"],
    ["6c022c38f90a4c07", "3601161cf205268d", "1b8e0b0e798c13c8", "83478b07b2468764"],
    ["a011d380818e8f40", "5086e740ce47c920", "2843fd2067adea10", "14aff010bdd87508"],
    ["0ad97808d06cb404", "05e23c0468365a02", "8c711e02341b2d01", "46b60f011a83988e"],
    ["90dab52a387ae76f", "486dd4151c3dfdb9", "24b86a840e90f0d2", "125C354207487869"],
    ["092e94218d243cba", "8a174a9ec8121e5d", "4585254f64090fa0", "accc9ca9328a8950"],
    ["9d4df05d5f661451", "C0a878a0a1330aa6", "60543c50de970553", "302a1e286fc58ca7"],
    ["18150f14b9ec46dd", "0c84890ad27623e0", "0642ca05693b9f70", "0321658cba93c138"],
    ["86275df09ce8aaa8", "439da0784e745554", "afc0503c273aa42a", "d960281e9d1d5215"],
    ["e230140fc0802984", "71180a8960409a42", "b60c05ca30204d21", "5b068c651810a89e"],
    ["456c34887a3805b9", "ac361a443d1c8cd2", "561b0d22900e4669", "2b838811480723ba"],
    ["9bcf4486248d9f5d", "c3e9224312c8c1a0", "effa11af0964ee50", "f97d86d98a327728"],
    ["e4fa2054a80b329c", "727d102a548b194e", "39b008152acb8227", "9258048415eb419d"],
    ["492c024284fbaec0", "aa16012142f35760", "550b8e9e21f7a530", "a48b474f9ef5dc18"],
    ["70a6a56e2440598e", "3853dc371220a247", "1ca76e95091051ad", "0edd37c48a08a6d8"],
    ["07e095624504536c", "8d70c431ac02a736", "c83862965601dd1b", "641c314b2b8ee083"]
])

A_bin = np.array([[[int(bit) for bit in f"{int(x, 16):064b}"] for x in row] for row in A])
A_GF = GF(A_bin.reshape(16, 4, 64))  # Правильная размерность 16x4x64

c1 = int(
    "b1085bda1ecadae9ebcb2f18c0567f1f26a7642e45d016714eb88d75854cfc4c7b2e09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507",
    16)
c2 = int(
    "6fa3b58aa99d2f14afe39d460f70b5d7f3feea720a232b986d155ef0f16b501319ab5176b12d699585bc561c2d0ba7ca55dda21bd7cbcd56e679047021b19bb7",
    16)
c3 = int(
    "f574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea751461297b7bd3e20fe490359eb1c1C93a376062db09c2b6f443867adb31991e96f50aba0ab2",
    16)
c4 = int(
    "eff1fdfb3e8156cd2f948e1a05d71e4dd488e857e335c7c3d9d721cad685e353fad927c28ed3067d58b7133395230be3453eaa193e8371f220cbec84e3d12e",
    16)
c5 = int(
    "4bea6abca4d747999a3f4106cca923637f151c1f1686104a359e35d7800fffbd8bfcd1747253af53d40ff0b723271a167a56a27ea9ea63f5601758fd7c6cfe57",
    16)
c6 = int(
    "ae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6Cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e",
    16)
c7 = int(
    "f4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c90992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493",
    16)
c8 = int(
    "91bff1b5c81dc3a9703e7aa002e64f141eb787179c36d1e8e9b443b4dbd409af4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e",
    16)
c9 = int(
    "378f5a54613229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d098480004440dbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb",
    16)
c10 = int(
    "abbdeae68005f652382ae548b2e4f3f8941e71cff8a78db1fffe18a1b3361039fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced",
    16)
c11 = int(
    "7bcd9ed0fec889fb3002c6cd635afe94d8fa6bbbebab07612001802114846798a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd856bcaa4cd81f32d1b",
    16)
c12 = int(
    "378ee767f11631bad21380b00449b17acda43c2bcdf1d77f82012d43021f9fb5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720",
    16)

c = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]


class Hash2018:
    def __init__(self, hash_size=256):
        if hash_size == 256:
            self.used256 = True
            self.IV = "00000001" * 64
        else:
            self.used256 = False
            self.IV = "0" * 512

    @staticmethod
    def l_transform(data):
        # Преобразуем входной список байтов (64 байта) в вектор битов (512 бит)
        bits = GF(np.unpackbits(np.array(data, dtype=np.uint8)))

        # Результат — вектор из 512 бит
        result_bits = GF.Zeros(512)

        # Выполняем умножение матрицы A на вектор битов
        for i in range(64):
            acc = GF(0)
            for j in range(64):
                acc += A_GF[i, j] * bits[j]
            result_bits[i] = acc

        # Упаковываем обратно в байты
        result_bytes = np.packbits(result_bits).tolist()
        return result_bytes

    @staticmethod
    def X_transform(k, a):
        # Преобразуем входные данные в массивы np.uint8
        k = np.array(k, dtype=np.uint8)
        a = np.array(a, dtype=np.uint8)

        # Проверка длины
        if k.shape != (64,) or a.shape != (64,):
            raise ValueError(f"Invalid input shapes: k={k.shape}, a={a.shape}")

        return k ^ a

    @staticmethod
    def S_transform(s):
        return [pi[byte] for byte in s]

    @staticmethod
    def P_transform(s):
        return [s[t] for t in tau]

    @staticmethod
    def L_transform(s):
        assert len(s) == 64
        # Преобразуем 64 байта в 512 бит
        bits = GF(np.unpackbits(np.array(s, dtype=np.uint8)))

        # Результат — вектор из 512 бит
        result_bits = GF.Zeros(512)

        # Выполняем умножение матрицы A на вектор битов
        for i in range(16):  # 16 блоков
            for j in range(4):  # 4 столбца в каждом блоке
                for k in range(64):  # 64 бита в каждом столбце
                    result_bits[i * 32 + j * 8 + k // 8] += A_GF[i, j, k] * bits[j * 128 + k]

        # Преобразуем result_bits в массив NumPy перед вызовом packbits
        result_bits_np = result_bits.view(np.ndarray)
        result_bytes = np.packbits(result_bits_np).tolist()

        # Проверяем длину результата
        if len(result_bytes) != 64:
            raise ValueError(f"Invalid L_transform output length: {len(result_bytes)}")

        return result_bytes
    @staticmethod
    def pad_data(data):
        """Дополняет данные до размера, кратного 64 байтам"""
        if len(data) % 64 != 0:
            pad_len = 64 - (len(data) % 64)
            # Добавляем 1 и затем нули
            padded = data + b'\x01' + bytes([0] * (pad_len - 1))
            return padded
        return data

    @staticmethod
    def forward(data):
        s = Hash2018.S_transform(data)
        p = Hash2018.P_transform(s)
        l = Hash2018.L_transform(p)
        return l

    @staticmethod
    def E(K, m):
        if len(K) != 64 or len(m) != 64:
            raise ValueError(f"Invalid input lengths: K={len(K)}, m={len(m)}")

        Ki = np.array(K, dtype=np.uint8)
        state = Hash2018.X_transform(Ki, np.array(m, dtype=np.uint8))

        for i in range(12):
            state = np.array(Hash2018.forward(state.tolist()), dtype=np.uint8)
            if state.shape != (64,):
                raise ValueError(f"Invalid state shape after forward: {state.shape}")

            c_bytes = c[i].to_bytes(64, 'big')
            c_array = np.frombuffer(c_bytes, dtype=np.uint8)
            Ki = Hash2018.X_transform(Ki, c_array)
            Ki = np.array(Hash2018.forward(Ki.tolist()), dtype=np.uint8)
            if Ki.shape != (64,):
                raise ValueError(f"Invalid Ki shape after forward: {Ki.shape}")

            state = Hash2018.X_transform(state, Ki)

        return state.tolist()

    @staticmethod
    def gN(h, m, N):
        # Преобразуем входные данные в массивы np.uint8
        h = np.array(h, dtype=np.uint8)
        m = np.array(m, dtype=np.uint8)
        N = np.array(N, dtype=np.uint8)

        # Проверяем длины
        if h.shape != (64,) or m.shape != (64,) or N.shape != (64,):
            raise ValueError(f"Invalid input shapes: h={h.shape}, m={m.shape}, N={N.shape}")

        # K = LPS(h ⊕ N)
        k = Hash2018.X_transform(h, N)
        k = np.array(Hash2018.forward(k.tolist()), dtype=np.uint8)

        # E(K, m)
        e = np.array(Hash2018.E(k.tolist(), m.tolist()), dtype=np.uint8)

        # gN = e xor h xor m
        result = Hash2018.X_transform(Hash2018.X_transform(e, h), m)

        return result.tolist()

    @staticmethod
    def hash(data: bytes, is256: bool = True) -> list[int]:
        # Начальные значения
        h = [1] * 64 if is256 else [0] * 64  # IV: 0x01*64 для 256 бит, 0x00*64 для 512 бит
        N = [0] * 64  # Счётчик длины сообщений в битах
        e = [0] * 64  # Сумма всех сообщений

        # Дополняем данные
        padded_data = Hash2018.pad_data(data)

        # Разбивка на 64-байтные блоки
        blocks = [padded_data[i:i + 64] for i in range(0, len(padded_data), 64)]

        for block in blocks:
            m = list(block)
            if len(m) != 64:
                raise ValueError(f"Invalid block length: {len(m)}")

            # gN step
            h = Hash2018.gN(h, m, N)

            # N = (N + len(m)*8) % 2^512
            block_length_bits = len(m) * 8
            length_bytes = block_length_bits.to_bytes(64, byteorder='little')
            length_list = list(length_bytes)
            N = Hash2018.add_mod512(N, length_list)

            # e = (e + m) % 2^512
            e = Hash2018.add_mod512(e, m)

        # Финальные преобразования
        h = Hash2018.gN(h, N, [0] * 64)
        h = Hash2018.gN(h, e, [0] * 64)

        return h[:32] if is256 else h  # Возвращаем 32 байта для 256-битного хэша или 64 для 512-битного

    @staticmethod
    def add_mod512(a: list[int], b: list[int]) -> list[int]:
        assert len(a) == 64 and len(b) == 64, f"Invalid lengths: len(a)={len(a)}, len(b)={len(b)}"
        result = [0] * 64
        carry = 0

        for i in reversed(range(64)):
            temp = a[i] + b[i] + carry
            result[i] = temp & 0xFF  # Оставляем младший байт
            carry = temp >> 8  # Перенос в следующий байт

        return result
"""
Для проверки размерности c1-c12
for i, const in enumerate(c):
    hex_str = hex(const)[2:].zfill(128)  # Убираем '0x' и добавляем ведущие нули
    print(f"c[{i}]: length={len(hex_str)}, value={hex_str[:20]}...")
    assert len(hex_str) == 128, f"Invalid length for c[{i}]: {len(hex_str)}"
"""