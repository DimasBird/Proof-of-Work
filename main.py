int512 = 2**512
int256 = 2**256

class Leaf:
    def __init__(self, value, parent=None, left=None, right=None):
        super(Leaf, self).__init__()
        self.Value = value
        self.Left = parent
        self.Right = right
        self.Parent = left

    def put_left(self, leaf):
        if self.Left is None: self.Left = leaf
        else:
            left = self.Left
            leaf.Left = left
            self.Left = leaf

    def put_right(self, leaf):
        if self.Right is None: self.Right = leaf
        else:
            right = self.right
            leaf.Left = right
            self.Right = leaf

class MerkleTree:
    def __init__(self, leaf):
        super(MerkleTree, self).__init__()

        if leaf == None: self.root = Leaf(0)
        else: self.root = leaf

    def put_leaf(self, leaf):
        current = self.root

        while(current != None):
            if current.Value >= leaf.Value: current = current.Left
            else: current = current.Right
        current = leaf

    def count_height(self, leaf):
        if leaf.Left == None and leaf.Right == None:
            return 1
        elif leaf.Left == None or leaf.Right == None:
            if leaf.Left == None: return self.count_height(leaf.Right) + 1
            if leaf.Right == None: return self.count_height(leaf.Left) + 1
        else:
            return max(self.count_height(leaf.Left), self.count_height(leaf.Right)) + 1

    def build_high_tree(self, height):
        level = 1
        current_level = [self.root]

        while (level < height):
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

    def put_transactions(self, hash_list=[]):
        if len(hash_list) > 1:
            # Подсчёт необходимой высоты дерева
            exp = 2
            x = 1
            while(exp < len(hash_list)):
                exp *= 2
                x += 1

            self.build_high_tree(x)

            




if __name__ == '__main__':
    print("Hello!")