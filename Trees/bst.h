#include <iostream>

using namespace std;

class Node {
public:
	int value;
	Node * leftChild;
	Node * rightChild;
	Node(int val);
};

class BinarySearchTree {
private:
	Node * root;
	Node * insertHelper(Node * current, int val);
	bool deleteHelper(Node * currentNode, int value);
	bool isLeaf(Node * currentNode);
	Node * findLeastNode(Node * currentNode);
public:
	BinarySearchTree();
	BinarySearchTree(int rootValue);
	void insert(int value);
	bool has(int value);
	bool deleteBST(int val);
};