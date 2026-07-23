class Solution {
public:
    string largestGoodInteger(string num) {
        string ans = "";
        bool f = false;
        char n = '0';
        for (int i = 1; i < num.length() - 1; i++) {
            if ((num[i] == num[i-1] && num[i+1] == num[i]) && num[i] >= n) {
                n = num[i];
                f = true;
            }
        }
        if (f) {
            for (int i = 0; i < 3; i++) {
                ans += n;
            }
        }
        return ans;
    }
};