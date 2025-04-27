class Node
{
    public:
        int HashValue = 0;
        Node* Left = nullptr;
        Node* Right = nullptr;
        Node* Parent = nullptr;

    Node(int hash);
    Node(int hash, Node* parent);
    Node(int hash, Node* parent, Node* left, Node* right);
};