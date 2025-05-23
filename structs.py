import hash_function as hsh

class Leaf:
    def __init__(self, message=None, parent=None, left=None, right=None):
        self.HashValue = hsh.streebog(message, hash_size=256) if message is not None else None
        self.Left = left
        self.Right = right
        self.Parent = parent

    def count_summ(self):
        if self.Left is None and self.Right is None:
            return self.HashValue
        left_hash = self.Left.count_summ() if self.Left else self.HashValue
        right_hash = self.Right.count_summ() if self.Right else left_hash  # Дублирование
        return hsh.streebog(left_hash + right_hash, hash_size=256)

    def check_summ(self):
        if self.Left is None and self.Right is None:
            return True
        left_hash = self.Left.count_summ() if self.Left else self.HashValue
        right_hash = self.Right.count_summ() if self.Right else left_hash
        expected_hash = hsh.streebog(left_hash + right_hash, hash_size=256)
        return (self.Left.check_summ() if self.Left else True) and \
               (self.Right.check_summ() if self.Right else True) and \
               (self.HashValue == expected_hash if self.HashValue is not None else True)

class MerkleTree:
    def __init__(self):
        self.root = None

    def put_hashes(self, hash_list=[]):
        if not hash_list:
            return
        # Создание листьев
        leaves = [Leaf(message=h) for h in hash_list]
        # Дублирование последнего хэша, если нечётное число
        if len(hash_list) % 2 == 1:
            leaves.append(Leaf(message=hash_list[-1]))

        while len(leaves) > 1:
            new_level = []
            for i in range(0, len(leaves), 2):
                parent = Leaf()
                parent.Left = leaves[i]
                parent.Right = leaves[i+1] if i+1 < len(leaves) else leaves[i]
                parent.Left.Parent = parent
                parent.Right.Parent = parent
                parent.HashValue = hsh.streebog(parent.Left.HashValue + parent.Right.HashValue, hash_size=256)
                new_level.append(parent)
            leaves = new_level
        self.root = leaves[0] if leaves else None

    def count_hash(self):
        return self.root.count_summ() if self.root else b'\x00' * 32 # Рекурсивный вызов

    def check_summ(self):
        return self.root.check_summ() if self.root else True # Рекурсивный вызов