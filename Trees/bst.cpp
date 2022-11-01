#include "bst.h"

Node::Node(int val) {
	value = 0;
	leftChild = NULL;
	rightChild = NULL;
}

BinarySearchTree::BinarySearchTree() {
}

BinarySearchTree::BinarySearchTree(int rootValue) {
	root = new Node(rootValue);
}

BinarySearchTree::insert(int val) {
	if(root == NULL) {
		root = new Node(val);
	}
}