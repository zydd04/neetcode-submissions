class Solution {
public:
    int heightChecker(vector<int>& heights) {
        std::vector<int> sorted = heights;
        std::sort(sorted.begin(), sorted.end());
        int count = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (sorted[i] != heights[i]) {
                count++;
            }
        }
        return count;
    }
};