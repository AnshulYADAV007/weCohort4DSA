#include <bits/stdc++.h>

using namespace std;

class PartitionSet {
public:
	bool canPartition(const vector<int> &nums) {
		int sum = 0;
		for(auto num : nums) sum += num;
		if(sum % 2 == 1) return false;

		vector<vector<int>> dp(nums.size(), vector<int>(sum + 1, -1));
		return this->canPartitionTopDown(dp, nums, sum/2, 0);
	}
/*
	for each number 'i' 
	  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively 
	      process the remaining numbers
	  create a new set WITHOUT number 'i', and recursively process the remaining items 
	return true if any of the above sets has a sum equal to 'S/2', otherwise return false
*/
private:
	bool canPartitionRecursive(const vector<int> &nums, int sum, int index) {
		if(sum == 0) return true;

		// sum > 0
		if(index >= nums.size()) return false;

		bool choice1 = false;
		if(nums[index] <= sum) {
			choice1 = this->canPartitionRecursive(nums, sum - nums[index], index + 1);
		}

		bool choice2 = this->canPartitionRecursive(nums, sum, index + 1);
		return choice1 || choice2;
	}

	bool canPartitionTopDown(vector<vector<int>> &dp, const vector<int> &nums, 
							int sum, int index) {
		if(sum == 0) return true;
		if(index >= nums.size()) return false;

		if(dp[index][sum] != -1) return dp[index][sum] == 1;

		bool choice1 = false;
		if(nums[index] <= sum) {
			choice1 = this->canPartitionTopDown(dp, nums, sum - nums[index], index + 1);
		}

		bool choice2 = this->canPartitionTopDown(dp, nums, sum, index + 1);
		dp[index][sum] = choice1 || choice2 ? 1: 0;
		return dp[index][sum] == 1;
	}
};


int main() {

  PartitionSet ps;
  vector<int> num = {1, 2, 3, 4};
  cout << ps.canPartition(num) << endl;
  num = vector<int>{1, 1, 3, 4, 7};
  cout << ps.canPartition(num) << endl;
  num = vector<int>{2, 10, 4, 6};
  cout << ps.canPartition(num) << endl;

}