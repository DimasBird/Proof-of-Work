#include "MerkleTree.h"

Node::Node(int hash)
{
    HashValue = hash;
}

Node::Node(int hash, Node* parent)
{
    HashValue = hash;
    Parent = parent;
}

Node::Node(int hash, Node* parent, Node* left, Node* right)
{
    HashValue = hash;
    Parent = parent;
    Left = left;
    Right = right;
}

Node::~Node()
{
    if (Left) delete Left;
    if (Right) delete Right;
}

Node* Node::AddLeft(Node* node)
{
    Node* current_left = this->Left;

    this->Left = node;
    node->Parent = this;
    node->Left = current_left;

    return node;
}

Node* Node::AddRight(Node* node)
{
    Node* current_right = this->Right;
    
    this->Right = node;
    node->Parent = this;
    node->Right = current_right;

    return node;
}

int Node::CountSumm()
{
    if (Left == nullptr & Right == nullptr)
    {
        return HashValue;
    }

    else if (Left == nullptr | Right == nullptr)
    {
        if (Left) return Left->CountSumm();
        else return Right->CountSumm();
    }

    else
    {
        return Left->CountSumm() + Right->CountSumm();
    }
}

MerkleTree::MerkleTree()
{
    Root = new Node(0);
}

MerkleTree::~MerkleTree()
{
    delete Root; // рекурсивное удаление
}

int MerkleTree::CountHash()
{
    Root->HashValue = Root->CountSumm();

    return Root->HashValue;
}

// TO DO
bool MerkleTree::CheckHash()
{
    return true;
}