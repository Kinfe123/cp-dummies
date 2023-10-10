class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
    int res = 0, cur = 0;
    for (int n : nums) {
        cur = cur == 0 ? n : cur & n;
        res += cur == 0;
    }
    return max(1, res);

    }
};