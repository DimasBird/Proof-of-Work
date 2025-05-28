from hash_function import streebog
from pseudorandom_number_generator import PRNG

p = 0xee8172ae8996608fb69359b89eb82a69854510e2977a4d63bc97322ce5dc3386ea0a12b343e9190f23177539845839786bb0c345d165976ef2195ec9b1c379e3
q = 0x98915e7ec8265edfcda31e88f24809ddb064bdc7285dd50d7289f0ac6f49dd2d
a = 0x1166bfd877c478b39345b3473836647e28bf38bcd05e4055916ef90d645e1a0c70f40d8f34b5d9cf0eba327681b9b637efb79fb68d93c70725e6920473b3d2a0

Lp = (p.bit_length()+7)//8

def int_to_bytes(x:int) -> bytes:
    return x.to_bytes(Lp,'big')

def H(data:bytes) -> int:
    h256 = streebog(data, hash_size=256)
    return int.from_bytes(h256, 'big') % q

def keygen(l):
    generator = PRNG(l)
    x = int.from_bytes(generator.generate_numbers()[0],'big') % q
    P = pow(a, x, p)
    return x, P

def sign(m:bytes, x:int, P:int,l):
    generator = PRNG(l)
    r = int.from_bytes(generator.generate_numbers()[0],'big') % q
    R = pow(a, r, p)
    e = H(int_to_bytes(R) + int_to_bytes(P) + m)
    s = (r + e * x) % q
    return R, s

def verify(m:bytes, P:int, R:int, s:int) -> bool:
    e = H(int_to_bytes(R) + int_to_bytes(P) + m)
    return pow(a, s, p) == (R * pow(P, e, p)) % p

