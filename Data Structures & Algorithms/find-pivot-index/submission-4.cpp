class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0;
        int right = 0;
        for (int i = 1; i < nums.size(); i++) {
            right += nums[i];
        }
        for (int i = 0; i < nums.size(); i++) {
            if (right == left) {
                return i;
            }
            cout << left << "" << " left" << "\n";
            cout << i << "" << "\n";
            cout << right << "" << " right" << "\n";
            left += nums[i];
            right -= nums[i+1];
            
        }
        return -1;
    }
};