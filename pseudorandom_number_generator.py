from hash_function import streebog

class PRNG:
    def __init__(self, string, overall_iterations=1):
        super(PRNG, self).__init__()
        self.h0 = streebog(PRNG.make_string_k_bytes(string, 64), hash_size=256)
        self.overall_iterations = overall_iterations
        self.numbers = self.generate_numbers()

    @staticmethod
    def make_string_k_bytes(s, k=32) -> bytes:
        s = s.encode('utf-8')
        if len(bytes(s)) == 32:
            return bytes(s)
        if len(bytes(s)) > 32:
            return bytes(s)[:32]
        if len(bytes(s)) < 32:
            zeros = bytes([0 for i in range(k - len(s))])
            return bytes(s) + zeros

    def generate_numbers(self) -> list:
        numbers = []
        for i in range(1, self.overall_iterations + 1, 1):
            current_number = streebog(self.h0 + i.to_bytes(32, byteorder="big"))
            numbers.append(current_number)

        return numbers
