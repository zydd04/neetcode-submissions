class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int a = 1;
        int b = 1;
        int d = 1;
        int i = 1;
        for (int r = 0; r < nums.size() - 1; r++) {
            if(nums[r] < nums[r+1]) {
                a++;
                i = max(i, a);      
                cout << nums[r] << "\n";
                cout << "Increasing" << "\n";
                cout << d << "\n";
                b = 1;
            }
            else if (nums[r] > nums[r+1]) {
                b++;
                d = max(d, b);
                cout << nums[r] << "" << "\n";
                cout << "Decreasing" << "\n";
                cout << d << "\n";
                a = 1;
            }
            else if (nums[r] == nums[r+1]) {
                d = max(d, b);  
                i = max(i, a); 
                cout << nums[r] << "\n";
                cout << "Equal" << "\n";
                cout << d << "\n";
                cout << i << "\n";
                a = 1;
                b = 1;
            }
        }
        return max(d, i);
    }
};