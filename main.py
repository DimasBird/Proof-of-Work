import struct
from hash_function import streebog


# Example usage
if __name__ == "__main__":
    message = b"message digest"
    print("STREEBOG-512:", streebog(message, 512).hex())
    print("STREEBOG-256:", streebog(message, 256).hex())