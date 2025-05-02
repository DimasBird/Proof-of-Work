class Leaf:
    def __init__(self, hash_value, parent=None, left=None, right=None):
        super(Leaf, self).__init__()
        self.HashValue = hash_value
        self.Left = parent
        self.Right = right
        self.Parent = left

    # Тут надо не складывать хэши, а находить хэш от конкатенации хэшей детей
    # TO DO
    def count_summ(self):
        if self.Left is None and self.Right is None:
            return self.HashValue

        elif self.Left is None and self.Right is None:
            if self.Left is not None: return self.Left.count_summ()
            if self.Right is not None: return self.Right.count_summ()

        else:
            return self.Left.count_summ() + self.Right.count_summ()

    # Тут надо не складывать хэши, а находить хэш от конкатенации хэшей детей
    # TO DO
    def check_summ(self):
        if self.Left is None and self.Right is None:
            return True

        elif self.Left is None and self.Right is None:
            if self.Left is not None: return self.Left.check_summ()
            if self.Right is not None: return self.Right.check_summ()

        else:
            return self.Left.check_summ() and self.Right.check_summ() and self.HashValue == self.count_summ()

    def put_left(self, leaf):
        if self.Left is None:
            self.Left = leaf
            leaf.Parent = self
        else:
            left = self.Left
            left.Parent = leaf
            leaf.Left = left
            self.Left = leaf
            leaf.Parent = self

    def put_right(self, leaf):
        if self.Right is None:
            self.Right = leaf
            leaf.Parent = self
        else:
            right = self.Right
            right.Parent = leaf
            leaf.Left = right
            self.Right = leaf
            leaf.Parent = self


class MerkleTree:
    def __init__(self, leaf):
        super(MerkleTree, self).__init__()

        if leaf is None:
            self.Root = Leaf(0)
        else:
            self.root = leaf

    def put_leaf(self, leaf):  # Простейшая функция, может не подойти
        current = self.root

        while current is not None:
            if current.Value >= leaf.Value:
                current = current.Left
            else:
                current = current.Right
        current = leaf

    def count_height(self, leaf):  # Считает высоту текущего дерева
        if leaf.Left is None and leaf.Right is None:
            return 1
        elif leaf.Left is None or leaf.Right is None:
            if leaf.Left is None: return self.count_height(leaf.Right) + 1
            if leaf.Right is None: return self.count_height(leaf.Left) + 1
        else:
            return max(self.count_height(leaf.Left), self.count_height(leaf.Right)) + 1

    def build_high_tree(self, height):  # Строит дерево определённой высоты
        level = 1
        current_level = [self.root]

        while level < height:
            new_level = []

            for node in current_level:
                # Создаём новые узлы
                node.Left = Leaf(0)
                node.Right = Leaf(0)
                # Заполняем новый уровень
                new_level.append(node.Left)
                new_level.append(node.Right)

            # Меняем уровни
            current_level = new_level

        return current_level

    def put_hashes(self, hash_list=[]):  # Складывает хэши в деревья
        if len(hash_list) > 1:
            # Подсчёт необходимой высоты дерева
            exp = 2
            x = 1
            while exp < len(hash_list):
                exp *= 2
                x += 1

            current_level = self.build_high_tree(x)

            used_nodes = 0
            for hash in hash_list:
                current_level[0] = Leaf(hash)
                used_nodes += 1

            if used_nodes < len(current_level):
                for i in range(used_nodes, len(current_level)):
                    current_level[i] = Leaf(hash_list[i - used_nodes])

    def count_hash(self):
        return self.Root.count_summ()

    def check_summ(self):
        return self.Root.check_summ()

