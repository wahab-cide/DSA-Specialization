#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>
using namespace std;


/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

*/




class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        int i = m - 1, j = n - 1 , k = m + n - 1;

        while(i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]){
                nums1[k] = nums1[i];
                i--;
            }
            else{
                nums1[k] = nums2[j];
                j--;
            }

            k--;
        }

        while ( j >= 0){
            nums1[k] = nums2[j];
            j--;
            k--;
        }
        
    }
};


/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
*/
int removeElement(vector<int>& nums, int val) {
    int i = 0;
    int n = nums.size();
    
    while (i < n) {
        if (nums[i] == val) {
            nums[i] = nums[n-1];
            n--;
        } else {
            i++;
        }
    }
    
    return n;
}


/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int k = 1;  // Pointer for position to place unique elements
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
};

/*
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;
        
        int k = 2;  // Pointer for position to place valid elements
        
        for (int i = 2; i < n; i++) {
            // Compare with element two positions back in the result array
            if (nums[i] != nums[k - 2]) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
};


/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
*/

int majorityElement_hash(vector<int>& nums) {
    unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }
    
    int majority = 0;
    int max_count = 0;
    for (auto& [num, cnt] : count) {
        if (cnt > max_count) {
            max_count = cnt;
            majority = num;
        }
    }
    return majority;
}

//Bayer-Moore

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }
        
        return candidate;
    }
};

//Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;  // Handle cases where k > n
        
        // Step 1: Reverse entire array
        reverse(nums.begin(), nums.end());
        // Step 2: Reverse first k elements
        reverse(nums.begin(), nums.begin() + k);
        // Step 3: Reverse remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};

/*
Best Time to Buy and Sell Stock I

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        
        int min_price = INT_MAX;
        int max_profit = 0;
        
        for (int price : prices) {
            // Update minimum price seen so far
            if (price < min_price) {
                min_price = price;
            }
            // Calculate profit if we sell today
            int profit = price - min_price;
            // Update maximum profit
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
        
        return max_profit;
    }
};

/*
One Pass Method:

Keep track of the minimum price seen so far

For each day, calculate potential profit if we sold at current price (bought at min price)

Update maximum profit if current profit is better

Time: O(n), Space: O(1)
*/


/*
Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int maxProfit = 0;

        for(int i = 1; i < prices.size(); i++){
            if (prices[i] > prices[i - 1]) maxProfit += prices[i] - prices[i - 1];
        }

        return maxProfit;
        
    }
};

/*
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
*/

class Solution {
public:
    bool canJump(vector<int>& nums) {

        int max_reach = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++){
            if(i > max_reach) return false;
            max_reach = max(max_reach, i + nums[i]);
            if (max_reach >= n - 1) return true;
        }
        return false;
    }
};


/*
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

*/

class Solution {
public:
    int jump(vector<int>& nums) {

        int n = nums.size(), jumps = 0;
        int current_reach = 0, next_reach = 0;

        if(n <= 1) return 0;

        for(int i = 0; i < n - 1; i++){
            next_reach = max(next_reach, i + nums[i]);

            if(i == current_reach){
                jumps++;
                current_reach = next_reach;

                if(current_reach >= n - 1){
                    break;
                }
            }
        }

        return jumps;


        
    }
};