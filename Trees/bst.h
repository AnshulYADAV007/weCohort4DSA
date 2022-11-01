#include <iostream>

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
public:
	BinarySearchTree()
	BinarySearchTree(int rootValue);
	void insert(int value);
	bool has(int value);
};