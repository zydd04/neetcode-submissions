class Solution {
public:
    int maxDifference(string s) {
        int even = 1000;
        int odd = 0;
        std::unordered_map<char, int> counter;
        for (int i = 0; i < s.length(); i++) {
            counter[s[i]]++;
        }
        for (const auto& pair : counter) {
            int value = pair.second;
            if ((value % 2 == 0) && (value < even)) {
                even = value;
            }
            if ((value % 2 != 0) && (value > odd)) {
                odd = value;
            }
        }
        return odd - even;
    }
};