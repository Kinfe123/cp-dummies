#include <vector>
#include <unordered_map>

class Solution {
public:
    int minimumTotal(std::vector<std::vector<int>>& triangle) {
        std::unordered_map<std::pair<int, int>, int, PairHash> memo;
        return dp(0, 0, triangle, memo);
    }

private:
    struct PairHash {
        template <typename T1, typename T2>
        std::size_t operator()(const std::pair<T1, T2>& p) const {
            auto h1 = std::hash<T1>{}(p.first);
            auto h2 = std::hash<T2>{}(p.second);
            return h1 ^ h2;
        }
    };

    int dp(int indx, int inner, std::vector<std::vector<int>>& triangle, std::unordered_map<std::pair<int, int>, int, PairHash>& memo) {
        if (indx == triangle.size()) {
            return 0;
        }
        if (inner == triangle[indx].size()) {
            return 0;
        }

        auto key = std::make_pair(indx, inner);
        if (memo.count(key)) {
            return memo[key];
        }

        memo[key] = std::min(dp(indx + 1, inner, triangle, memo) + triangle[indx][inner], dp(indx + 1, inner + 1, triangle, memo) + triangle[indx][inner]);

        return memo[key];
    }
};