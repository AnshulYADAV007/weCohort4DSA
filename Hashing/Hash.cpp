#include "Hash.h"
#include <iostream>

using namespace std;

HashEntry::HashEntry(string key, int value) {
	this->key = key;
	this->value = value;
	next = NULL;
}


HashTable::HashTable(int s) {
	bucket = new HashEntry * [s];
	for (int i = 0; i < s; i++) {
		bucket[i] = NULL;
	}
	slots = s;
	size = 0;
}

int HashTable::getSize() {
	return size;
}

bool HashTable::isEmpty() {
	return getSize() == 0;
}

int HashTable::getIndex(string key) {
	int Key = 0, PRIME = 37;

	for(auto ch : key) {
		Key = PRIME * Key + ch;
		Key %= slots;
	}

	if (Key < 0) Key *= -1;

	return Key % slots;
}

void HashTable::insert(string key, int value) {
	int hashIndex = getIndex(key);

	if(bucket[hashIndex] == NULL) {
		bucket[hashIndex] = new HashEntry(key, value);
		size++;
	} else {
		HashEntry * head = bucket[hashIndex];
		HashEntry * newNode = new HashEntry(key, value);
		newNode -> next = head;
		bucket[hashIndex] = newNode;
		size++;
	}
}

int HashTable::get(string key) {
	int hashIndex = getIndex(key);

	if(bucket[hashIndex] == NULL) {
		cout << "Value not found!" << endl;
		return -1;
	}

	HashEntry * temp = bucket[hashIndex];
	while(temp != NULL) {
		if(temp -> key == key) return temp -> value;
		temp = temp -> next;
	}

	cout << "Value not found!" << endl;
	return -1;
}