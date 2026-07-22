class Solution {
public:
    int lengthOfLastWord(string s) {
        std::stringstream ss(s);
        std::string str;
        std::vector<std::string> strs;
        while (ss >> str) {
            strs.push_back(str);
        }
        if (strs.empty()) {
            return 0;
        }
        return strs.back().length();
    }
};