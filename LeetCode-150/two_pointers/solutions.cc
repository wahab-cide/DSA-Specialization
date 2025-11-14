using namespace std;
#include <string>
#include <cctype> 
#include <vector>
#include <algorithm>



/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
*/
class Solution {
public:
    bool isPalindrome(string s) {

        int l = 0, r = s.length() - 1;

        while(l < r){
           while(l < r && !isalnum(s[l])) l++;
           while(l < r && !isalnum(s[r])) r--;

           if(tolower(s[l]) != tolower(s[r])) {return false;}
           l++;
           r--;

        }

        return true;
        
    }
};

/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

*/


class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;  // i for s, j for t
        
        while (i < s.length() && j < t.length()) {
            // If characters match, move both pointers
            if (s[i] == t[j]) {
                i++;
            }
            // Always move j forward
            j++;
        }
        
        // If we matched all characters in s, it's a subsequence
        return i == s.length();
    }
};

/*
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
*/


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        
        while (left < right) {
            int current_sum = numbers[left] + numbers[right];
            
            if (current_sum == target) {
                // Return 1-based indices
                return {left + 1, right + 1};
            } else if (current_sum < target) {
                // Need larger sum, move left pointer right
                left++;
            } else {
                // Need smaller sum, move right pointer left
                right--;
            }
        }
        
        // Problem guarantees exactly one solution
        return {-1, -1};
    }
};

/*
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
*/


class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int max_area = 0;
        
        while (left < right) {
            // Calculate current area
            int current_area = min(height[left], height[right]) * (right - left);
            max_area = max(max_area, current_area);
            
            // Move the pointer with smaller height
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return max_area;
    }
};

/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
*/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> result;
        
        for(int i = 0; i < n - 2; i++){
            // Fixed: should be i > 0, not i > 1
            if(i > 0 && nums[i] == nums[i - 1]) continue;
            
            int l = i + 1, r = n - 1;
            while(l < r){
                int sum = nums[i] + nums[l] + nums[r];
                
                if(sum == 0){
                    result.push_back({nums[i], nums[l], nums[r]});
                    
                    // Skip duplicates for left pointer
                    while(l < r && nums[l] == nums[l + 1]) l++;
                    // Skip duplicates for right pointer  
                    while(l < r && nums[r] == nums[r - 1]) r--;
                    
                    l++;
                    r--;
                }
                else if(sum > 0){
                    r--;
                }
                else { // Fixed: should be l++, not r++
                    l++;
                }
            }
        }
        return result;
    }
};