# Promblem - intersection of two arrays 
# Approach - hash set 
# Time and space complexity - 0(n+m) & 0(n) 
# Leetcode and diffculty level - 349 & easy 
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s(nums1.begin(), nums1.end());
        unordered_set<int> result;

        for(int num : nums2) {
            if(s.find(num) != s.end()) {
                result.insert(num);
            }
        }
        return vector<int>(result.begin(), result.end());
    }
};
