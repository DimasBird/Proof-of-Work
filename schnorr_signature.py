import os
from hash_function import streebog
from pseudorandom_number_generator import PRNG

p = 0xEE8172AE8996608FB69359B89EB82A69854510E2977A4D63BC97322CE5DC3386EA0A12B343E9190F23177539845839786BB0C345D165976EF2195EC9B1C379E3
q = 0x98915E7EC8265EDFCDA31E88F24809DDB064BDC7285DD50D7289F0AC6F49DD2D
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

