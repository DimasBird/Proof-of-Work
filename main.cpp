#include <iostream>
#include "MerkleTree.h"

int main()
{
    MerkleTree* tree = new MerkleTree();

    Node* root = tree->Root;

    root->AddLeft(new Node(10));
    root->AddRight(new Node(20));

    std::cout << tree->CountHash();
    delete tree;

    return 0;
}