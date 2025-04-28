#pragma once
#include "googletest/googletest/include/gtest/gtest.h"
#include "MerkleTree.h"
#include "HashFunction.h"

class MerkleTreeTest : public ::testing::Test
{

};

TEST(MerkleTreeTest, Test1_Children_and_Parent_are_NullPTR)
{
    MerkleTree* tree = new MerkleTree();

    EXPECT_TRUE(tree->Root->HashValue == 0);

    EXPECT_FALSE(tree->Root->Left || tree->Root->Right || tree->Root->Parent);
}

TEST(MerkleTreeTest, Test2_Check_and_Count_Hash)
{
    MerkleTree* tree = new MerkleTree();

    Node* root = tree->Root;

    Node* ptr = root;

    root->AddLeft(new Node(10));
    root->AddRight(new Node(20));

    ptr = root->Left;
    ptr->AddLeft(new Node(40));

    EXPECT_FALSE(tree->CheckHash());

    ptr = root->Right;
    ptr->AddLeft(new Node(5));
    ptr->AddRight(new Node(7));

    EXPECT_TRUE(tree->CountHash() == 52);
    EXPECT_TRUE(tree->CheckHash());

    delete tree;
}