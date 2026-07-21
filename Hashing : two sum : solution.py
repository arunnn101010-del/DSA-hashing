# Promblem - two sum 
# Approach - Hash map
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 1 & easy 
class Solution {
public:
    vector<int> twoSum(vector<int>& arr, int tar) {
        unordered_map<int, int> m;
        vector<int> ans;

         for(int i=0; i<arr.size(); i++) {
            int first = arr[i];
            int sec = tar - first;

            if(m.find(sec) != m.end()) {
                ans.push_back(i);
                ans.push_back(m[sec]);
                break;
            }

            m[first] = i; // store key value pairs of i 
        }   

        return ans;
    }
};
