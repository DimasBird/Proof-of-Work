import structs
import hash_function as hsh

int512 = 2**512
int256 = 2**256

hash_size = 256

if __name__ == '__main__':
    print(hsh.Hash2018.hash(b"s"*64))