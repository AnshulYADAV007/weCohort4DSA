#include <bits/stdc++.h>
#include "bst.cpp"

using namespace std;

int main() {
	BinarySearchTree bst(8);
	bst.insert(5);
	cout << boolalpha ;
	cout << "BST has 5 " << bst.has(5) << endl;
	cout << bst.deleteBST(5) << endl;
	cout << "BST has 5 after delete " <<  bst.has(5);
	return 0;
}