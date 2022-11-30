#include <bits/stdc++.h>

using namespace std;

int findLPSLengthRecursive(const string &s, int start, int end) {
	if(start > end) return 0;
	if(start == end) return 1;

	if(s[start] == s[end]) return 2 + findLPSLengthRecursive(s, start + 1, end - 1);

	int choice1 = findLPSLengthRecursive(s, start + 1, end);
	int choice2 = findLPSLengthRecursive(s, start, end - 1);
	return max(choice1, choice2);
}

int findLPSLengthIterative(const string &s) {
	vector<vector<int>> dp(s.length(), vector<int>(s.length(), 0));

	for(int i = 0; i < s.length(); i++) dp[i][i] = 1;

	for(int start = s.length() - 2; start >= 0; start--){// row will move from bottom to top
		for(int end = start + 1; end < s.length(); end++) { // column moves left to right
			if(s[start] == s[end]){
				cout << s.substr(start, end - start + 1) << " <- 2 + " 
					 << s.substr(start + 1, end - start -1) << "(" 
					 << dp[start + 1][end - 1] << ")" << endl;  
				dp[start][end] = 2 + dp[start + 1][end - 1];	
			} 
			else {
				cout << s.substr(start, end - start + 1) << " <- max (" 
					 << s.substr(start + 1, end - start) << "(" << dp[start + 1][end] << "), " 
					 << s.substr(start, end - start) << "("<< dp[start][end - 1] << "))" << endl;
				dp[start][end] = max(dp[start + 1][end], dp[start][end - 1]);
			}
		}
	}

	return dp[0][s.length() - 1];
}

int findLPSLength(const string &s) {
	return findLPSLengthIterative(s);
}

int main() {
	cout << findLPSLength("abcdecba") << endl;
}