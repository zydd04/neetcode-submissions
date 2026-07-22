class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> counter;
        for (int i = 0; i < nums.size(); i++){
            counter[nums[i]]++;
        }
        for (auto& pair : counter) {
            if (pair.second > nums.size()/2) {
                return pair.first;
            }
        }
    }
};