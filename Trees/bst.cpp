#include "bst.h"

Node::Node(int val) {
	value = val;
	leftChild = NULL;
	rightChild = NULL;
}

BinarySearchTree::BinarySearchTree() {
}

BinarySearchTree::BinarySearchTree(int rootValue) {
	root = new Node(rootValue);
}

void BinarySearchTree::insert(int val) {
	root = insertHelper(root, val);
	/*
	if(root == NULL) {
		root = new Node(val);
		return;
	}

	Node * currentNode = root;
	Node * parent = NULL;

	while(currentNode != NULL) {
		parent = currentNode;
		if (val < currentNode -> value) currentNode = currentNode -> leftChild;
		else currentNode = currentNode -> rightChild;
	}

	// parent == leaf node
	if(val < parent -> value) parent -> leftChild = new Node(val);
	else parent -> rightChild = new Node(val);
	*/
}


Node * BinarySearchTree::insertHelper(Node * current, int val) {
	if (current == NULL) return new Node(val);
	else if(val < current -> value) current -> leftChild = insertHelper(current -> leftChild, val);
	else current->rightChild = insertHelper(current -> rightChild, val);
	return current;
}

bool BinarySearchTree::has(int val) {
	Node * currentNode = root;

	while(currentNode && currentNode -> value != val) {
		if (val < currentNode ->value) currentNode = currentNode -> leftChild;
		else currentNode = currentNode -> rightChild;
	}

	return currentNode != NULL;
}

bool BinarySearchTree::deleteBST(int val) {
	return deleteHelper(root, val);	
}


bool BinarySearchTree::deleteHelper(Node * currentNode, int val) {
	// Case 1 : Empty tree
	if (root == NULL) return false;

	Node * parent;
	while(currentNode && currentNode->value != val) {
		parent = currentNode;
		if (val < currentNode -> value) currentNode = currentNode -> leftChild;
		else currentNode = currentNode -> rightChild;
	}

	if(currentNode == NULL) return false;
	else if(isLeaf(currentNode)) {
		if (currentNode == root) {
			delete root;
			root = NULL;
			return true;
		}
		else if (parent -> value <= currentNode -> value) {
			delete parent -> rightChild;
			parent ->rightChild = NULL;
			return true;
		} else {
			delete parent -> leftChild;
			parent -> leftChild = NULL;
			return true;
		}
	}else if(currentNode->rightChild == NULL) {
		if(root == currentNode) {
			delete root;
			root = currentNode -> leftChild;
			return true;
		}
		else if (parent -> value <= currentNode -> value) {
			parent ->rightChild = currentNode -> leftChild;
			delete currentNode;
			return true;
		} else {
			parent -> leftChild = currentNode -> leftChild;
			delete currentNode;
			return true;
		}
	}else if(currentNode->leftChild == NULL) {
		if(root == currentNode) {
			delete root;
			root = currentNode -> rightChild;
			return true;
		}
		else if (parent -> value <= currentNode -> value) {
			parent ->rightChild = currentNode -> rightChild;
			delete currentNode;
			return true;
		} else {
			parent -> leftChild = currentNode -> rightChild;
			delete currentNode;
			return true;
		}
	}else {
		Node * leastNode = findLeastNode(currentNode -> rightChild);
		int tmp = leastNode -> value;
		deleteHelper(root, tmp);
		currentNode -> value = tmp;
		return true;
	}
}

bool BinarySearchTree::isLeaf(Node * currentNode) {
	return currentNode && currentNode -> leftChild == NULL && currentNode -> rightChild == NULL;
}

Node * BinarySearchTree::findLeastNode(Node * currentNode) {
	while(currentNode -> leftChild) currentNode = currentNode -> leftChild;
	return currentNode;
}
