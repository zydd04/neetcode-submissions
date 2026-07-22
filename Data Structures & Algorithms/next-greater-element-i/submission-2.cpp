class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> ans(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); i++) {
            bool seen = false;
            for (int j = 0 ; j < nums2.size(); j++) {
                if (nums2[j] > nums1[i] && seen) {
                    ans[i] = nums2[j];
                    break;
                }
                if(nums2[j] == nums1[i]) {
                    seen = true;
                }
            }
        }
        return ans;      
    }
};