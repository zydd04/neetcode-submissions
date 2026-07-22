class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        char c;
        char b;
        for (int i = 0; i < s.length()-1; i++) {
            char c = s[i];
            char b = s[i+1];
            score = score +abs(b - c);
        }
        return score;
    }
};