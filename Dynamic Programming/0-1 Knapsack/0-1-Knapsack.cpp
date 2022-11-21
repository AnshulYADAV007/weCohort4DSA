#include <bits/stdc++.h>

using namespace std;

class Knapsack {
public:
	int solveKnapsack(const vector<int> &profits, const vector<int> &weights, int capacity) {
		vector<vector<int>> dp(profits.size(), vector<int>(capacity + 1, -1));
		return this->knapsackTopDown(dp, profits, weights, capacity, 0);
	}

/*
for each item 'i' 
  create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and 
     recursively process the remaining capacity and items
  create a new set WITHOUT item 'i', and recursively process the remaining items 
return the set from the above two sets with higher profit 
*/

private:
	// T(n) = 2 * T(n-1) = 2 * 2 * T(n - 2) = 2 * 2 * 2 * T(n - 3) = O(2 ^ n)
	int knapsackRecursive(const vector<int> &profits, const vector<int> &weights, 
						  int capacity, int index){
		if (capacity <= 0 || index >= profits.size()) {
			return 0;
		}

		int choice1 = 0;

		if(weights[index] <= capacity) {
			choice1 = 
					profits[index] + 
					this->knapsackRecursive(profits, weights, capacity - weights[index], index + 1);
		}

		int choice2 = this->knapsackRecursive(profits, weights, capacity, index + 1);
		return max(choice1, choice2);
	}

	int knapsackTopDown(vector<vector<int>> &dp, const vector<int> &profits, const vector<int> &weights, 
						  int capacity, int index) {
		if (capacity <= 0 || index >= profits.size()) {
			return 0;
		}

		if (dp[index][capacity] != -1) {
			return dp[index][capacity];
		}

		int choice1 = 0;

		if(weights[index] <= capacity) {
			choice1 = 
					profits[index] + 
					this->knapsackTopDown(dp, profits, weights, capacity - weights[index], index + 1);
		}

		int choice2 = this->knapsackTopDown(dp, profits, weights, capacity, index + 1);

		dp[index][capacity] = max(choice1, choice2);

		return dp[index][capacity];
	}
};

int main() {
	Knapsack ks;
	vector<int> profits = {1, 6, 10, 16};
	vector<int> weights = {1, 2, 3, 5};

	int maxProfit = ks.solveKnapsack(profits, weights, 7);
	cout << "Total Knapsack profit ---> " << maxProfit << endl;
	maxProfit = ks.solveKnapsack(profits, weights, 6);
	cout << "Total Knapsack profit ---> " << maxProfit << endl;
}