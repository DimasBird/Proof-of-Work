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