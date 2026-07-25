# Promblem - contains duplicate 
# Approach - hashing 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 217 & easy 
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;

        for(int num : nums) {
            if(s.find(num) != s.end()) {
                return true;
            }
            s.insert(num);
        }
        return false;
    }
};
