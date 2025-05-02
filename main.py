import structs
import hash_function as hsh

int512 = 2**512
int256 = 2**256

hash_size = 256

if __name__ == '__main__':
    result = hsh.Hash2018.hash(b"s"*32, is256=True)
    print("Hash (256-bit):")
    print("".join([hex(x)[2:].zfill(2) for x in result]))  # Вывод в шестнадцатеричном формате