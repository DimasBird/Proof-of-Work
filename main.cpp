#include <iostream>
#include "MerkleTree.h"

int main()
{
    MerkleTree* tree = new MerkleTree();

    Node* root = tree->Root;

    Node* ptr = root;

    root->AddLeft(new Node(10));
    root->AddRight(new Node(20));

    ptr = root->Left;
    ptr->AddLeft(new Node(40));

    ptr = root->Right;
    ptr->AddLeft(new Node(5));

    ptr->AddRight(new Node(7));

    std::cout << "Check hash: " << tree->CheckHash() << "\n";

    std::cout << "Count hash: " << tree->CountHash() << "\n"; // Возвращает сумму на нижнем ярусе

    std::cout << "Check hash: " << tree->CheckHash() << "\n";

    delete tree;

    return 0;
}