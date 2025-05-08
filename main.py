import struct
from hash_function import streebog
from pseudorandom_number_generator import PRNG


# Example usage
if __name__ == "__main__":
    message = b"message digest"
    print("STREEBOG-512:", streebog(message, 512).hex())
    print("STREEBOG-256:", streebog(message, 256).hex())

    Surname = "Medvedev"

    generator = PRNG(Surname, overall_iterations=16)

    for i in range(len(generator.numbers)):
        print("{0}) {1}".format(i+1, generator.numbers[i].hex()))
