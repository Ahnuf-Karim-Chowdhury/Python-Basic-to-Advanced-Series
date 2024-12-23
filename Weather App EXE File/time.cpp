/* 
You are given an array nums consisting of non-negative integers. 
You are also given a queries array, where queries[i] = [xi, mi].
The answer to the ith query is the maximum bitwise XOR value of xi and 
any element of nums that does not exceed mi. In other words, 
the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. 
If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and 
answer[i] is the answer to the ith query.

Example 1:
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 
         0 XOR 3 = 3 and 1 XOR 3 = 2. 
         The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

Example 2:
Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
 */

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maximizeXor(vector<int>& a, vector<vector<int>>& que) {
        const int n = a.size(), q = que.size();
        vector<int> res(q, -1);
        sort(a.begin(), a.end());

        for (int i = 0; i < q; i++) {
            const int x = que[i][0], m = que[i][1];
            if (m < a[0])
                continue;

            int e = upper_bound(a.begin(), a.end(), m) - a.begin();
            //cout <<" e = "<<e<<endl;
            int s = 0, k = 0, cur = 0;

            for (int bit = 31; bit >= 0; bit--) {
                if (x & (1 << bit)) { 
                    if (!(a[s] & (1 << bit))) {
                        k |= 1 << bit;
                        e = lower_bound(a.begin() + s, a.begin() + e,
                                        cur | (1 << bit)) -
                            a.begin();
                    } else {
                        cur |= 1 << bit;
                    }
                } else {
                    if (s <= e - 1 && (a[e - 1] & (1 << bit))) {
                        k |= 1 << bit;
                        cur |= 1 << bit;
                        s = lower_bound(a.begin() + s, a.begin() + e, cur) -
                            a.begin();
                    }
                }
            }
            res[i] = k;
        }
        return res;
    }
};

int main(){
    Solution s1;
    vector<int>nums={0,1,2,3,4};
    vector<vector<int>> que={{3,1},{1,3},{5,6}};
    vector<int>res=s1.maximizeXor(nums,que);
    for(auto i:res){
        cout<<i<<" ";
    }
}