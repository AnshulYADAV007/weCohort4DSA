#include <iostream>
using namespace std;

class HashEntry {
public:
	string key;
	int value;
	HashEntry * next;

	HashEntry(string key, int value);
};

class HashTable {
private:
	HashEntry ** bucket;
	int slots;
	int size;
	int getIndex(string key);
public:
	HashTable(int s);
	int getSize();
	bool isEmpty();
	int get(string key);
	void insert(string key, int value);
};