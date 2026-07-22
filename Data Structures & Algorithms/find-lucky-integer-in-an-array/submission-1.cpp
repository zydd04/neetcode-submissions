class Solution {
public:
    int findLucky(vector<int>& arr) {
        int lucky = -1;
        std::unordered_map<int, int> counter;
        for (int i = 0; i < arr.size(); i++) {
            counter[arr[i]]++;
        }
        for (auto& pair : counter) {
            if (pair.first == pair.second) {
                if(lucky < pair.first) {
                    lucky = pair.first;
                }
            }
        }
        return lucky;
    }
};