from copy import deepcopy

PI = [
    0xFC, 0xEE, 0xDD, 0x11, 0xCF, 0x6E, 0x31, 0x16, 0xFB, 0xC4, 0xFA, 0xDA, 0x23, 0xC5, 0x04, 0x4D,
    0xE9, 0x77, 0xF0, 0xDB, 0x93, 0x2E, 0x99, 0xBA, 0x17, 0x36, 0xF1, 0xBB, 0x14, 0xCD, 0x5F, 0xC1,
    0xF9, 0x18, 0x65, 0x5A, 0xE2, 0x5C, 0xEF, 0x21, 0x81, 0x1C, 0x3C, 0x42, 0x8B, 0x01, 0x8E, 0x4F,
    0x05, 0x84, 0x02, 0xAE, 0xE3, 0x6A, 0x8F, 0xA0, 0x06, 0x0B, 0xED, 0x98, 0x7F, 0xD4, 0xD3, 0x1F,
    0xEB, 0x34, 0x2C, 0x51, 0xEA, 0xC8, 0x48, 0xAB, 0xF2, 0x2A, 0x68, 0xA2, 0xFD, 0x3A, 0xCE, 0xCC,
    0xB5, 0x70, 0x0E, 0x56, 0x08, 0x0C, 0x76, 0x12, 0xBF, 0x72, 0x13, 0x47, 0x9C, 0xB7, 0x5D, 0x87,
    0x15, 0xA1, 0x96, 0x29, 0x10, 0x7B, 0x9A, 0xC7, 0xF3, 0x91, 0x78, 0x6F, 0x9D, 0x9E, 0xB2, 0xB1,
    0x32, 0x75, 0x19, 0x3D, 0xFF, 0x35, 0x8A, 0x7E, 0x6D, 0x54, 0xC6, 0x80, 0xC3, 0xBD, 0x0D, 0x57,
    0xDF, 0xF5, 0x24, 0xA9, 0x3E, 0xA8, 0x43, 0xC9, 0xD7, 0x79, 0xD6, 0xF6, 0x7C, 0x22, 0xB9, 0x03,
    0xE0, 0x0F, 0xEC, 0xDE, 0x7A, 0x94, 0xB0, 0xBC, 0xDC, 0xE8, 0x28, 0x50, 0x4E, 0x33, 0x0A, 0x4A,
    0xA7, 0x97, 0x60, 0x73, 0x1E, 0x00, 0x62, 0x44, 0x1A, 0xB8, 0x38, 0x82, 0x64, 0x9F, 0x26, 0x41,
    0xAD, 0x45, 0x46, 0x92, 0x27, 0x5E, 0x55, 0x2F, 0x8C, 0xA3, 0xA5, 0x7D, 0x69, 0xD5, 0x95, 0x3B,
    0x07, 0x58, 0xB3, 0x40, 0x86, 0xAC, 0x1D, 0xF7, 0x30, 0x37, 0x6B, 0xE4, 0x88, 0xD9, 0xE7, 0x89,
    0xE1, 0x1B, 0x83, 0x49, 0x4C, 0x3F, 0xF8, 0xFE, 0x8D, 0x53, 0xAA, 0x90, 0xCA, 0xD8, 0x85, 0x61,
    0x20, 0x71, 0x67, 0xA4, 0x2D, 0x2B, 0x09, 0x5B, 0xCB, 0x9B, 0x25, 0xD0, 0xBE, 0xE5, 0x6C, 0x52,
    0x59, 0xA6, 0x74, 0xD2, 0xE6, 0xF4, 0xB4, 0xC0, 0xD1, 0x66, 0xAF, 0xC2, 0x39, 0x4B, 0x63, 0xB6
]

TAU = [
    0, 8, 16, 24, 32, 40, 48, 56,
    1, 9, 17, 25, 33, 41, 49, 57,
    2, 10, 18, 26, 34, 42, 50, 58,
    3, 11, 19, 27, 35, 43, 51, 59,
    4, 12, 20, 28, 36, 44, 52, 60,
    5, 13, 21, 29, 37, 45, 53, 61,
    6, 14, 22, 30, 38, 46, 54, 62,
    7, 15, 23, 31, 39, 47, 55, 63
]

A_MATRIX = [
    int(x, 16).to_bytes(8, 'big') for x in [
        "8e20faa72ba0b470", "47107ddd9b505a38", "ad08b0e0c3282d1c", "d8045870ef14980e",
        "6c022c38f90a4c07", "3601161cf205268d", "1b8e0b0e798c13c8", "83478b07b2468764",
        "a011d380818e8f40", "5086e740ce47c920", "2843fd2067adea10", "14aff010bdd87508",
        "0ad97808d06cb404", "05e23c0468365a02", "8c711e02341b2d01", "46b60f011a83988e",
        "90dab52a387ae76f", "486dd4151c3dfdb9", "24b86a840e90f0d2", "125c354207487869",
        "092e94218d243cba", "8a174a9ec8121e5d", "4585254f64090fa0", "accc9ca9328a8950",
        "9d4df05d5f661451", "c0a878a0a1330aa6", "60543c50de970553", "302a1e286fc58ca7",
        "18150f14b9ec46dd", "0c84890ad27623e0", "0642ca05693b9f70", "0321658cba93c138",
        "86275df09ce8aaa8", "439da0784e745554", "afc0503c273aa42a", "d960281e9d1d5215",
        "e230140fc0802984", "71180a8960409a42", "b60c05ca30204d21", "5b068c651810a89e",
        "456c34887a3805b9", "ac361a443d1c8cd2", "561b0d22900e4669", "2b838811480723ba",
        "9bcf4486248d9f5d", "c3e9224312c8c1a0", "effa11af0964ee50", "f97d86d98a327728",
        "e4fa2054a80b329c", "727d102a548b194e", "39b008152acb8227", "9258048415eb419d",
        "492c024284fbaec0", "aa16012142f35760", "550b8e9e21f7a530", "a48b474f9ef5dc18",
        "70a6a56e2440598e", "3853dc371220a247", "1ca76e95091051ad", "0edd37c48a08a6d8",
        "07e095624504536c", "8d70c431ac02a736", "c83862965601dd1b", "641c314b2b8ee083"
    ]
]

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def S(data):
    return bytes(PI[b] for b in data)

def P(data):
    return bytes(data[TAU[i]] for i in range(64))

def L(data):
    result = bytearray(64)
    for i in range(8):
        for j in range(8):
            acc = 0
            for k in range(8):
                if data[i * 8 + k] & (1 << (7 - j)):
                    acc ^= A_MATRIX[k][j]
            result[i * 8 + j] = acc
    return result

def LPS(data):
    return L(P(S(data)))

# Генерация C[i]
def get_C():
    C = []
    for i in range(12):
        block = bytearray(64)
        block[0] = i + 1
        C.append(LPS(block))
    return C

C = get_C()

def E(K, m):
    state = xor(K, m)
    for i in range(12):
        state = LPS(state)
        K = LPS(xor(K, C[i]))
        state = xor(state, K)
    return state

def g(h, N, m):
    K = LPS(xor(h, N))
    return xor(xor(E(K, m), h), m)

def add_mod512(a, b):
    res = (int.from_bytes(a, 'big') + int.from_bytes(b, 'big')) % (1 << 512)
    return res.to_bytes(64, 'big')

def streebog(message: bytes, hash_size=512):
    if hash_size == 512:
        IV = bytes([1] * 64)
    elif hash_size == 256:
        IV = bytes([0] * 64)
    else:
        raise ValueError("hash_size must be 256 or 512")

    h = IV
    N = b'\x00' * 64
    Sigma = b'\x00' * 64

    blocks = [message[i:i+64] for i in range(0, len(message), 64)]
    if len(blocks[-1]) < 64:
        pad_len = 64 - len(blocks[-1])
        blocks[-1] = blocks[-1] + b'\x00' * pad_len

    for block in blocks[:-1]:
        h = g(h, N, block)
        N = add_mod512(N, (512).to_bytes(64, 'big'))
        Sigma = add_mod512(Sigma, block)

    last_block = blocks[-1]
    msg_len = (len(message) * 8).to_bytes(64, 'little')
    h = g(h, N, last_block)
    N = add_mod512(N, msg_len)
    Sigma = add_mod512(Sigma, last_block)
    h = g(h, b'\x00' * 64, N)
    h = g(h, b'\x00' * 64, Sigma)

    return h[-hash_size // 8:]
