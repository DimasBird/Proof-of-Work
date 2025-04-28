#ifndef MERKLETREE_H
#define MERKLETREE_H

class Node
{
    public:
        int HashValue = 0;
        Node* Left = nullptr;
        Node* Right = nullptr;
        Node* Parent = nullptr;
        Node* AddLeft(Node* node);
        Node* AddRight(Node* node);
        int CountSumm();
        bool CheckSumm();


    Node(int hash);
    Node(int hash, Node* parent);
    Node(int hash, Node* parent, Node* left, Node* right);

    ~Node();


};

class MerkleTree
{
    public:
        Node* Root;
        int CountHash();
        bool CheckHash();

    MerkleTree();
    ~MerkleTree();
};

#endif