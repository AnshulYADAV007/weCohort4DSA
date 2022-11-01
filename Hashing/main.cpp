#include "Hash.cpp"
#include <iostream>

int main()
{
	HashTable ht(4);
	ht.insert("Merudhula", 2217796);
	ht.insert("Rishika", 2217777);

	cout << ht.get("Bhumika") << endl;
	cout << ht.get("Rishika") << endl;
	return 0;
}