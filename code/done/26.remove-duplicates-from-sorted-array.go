/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

package main

// @lc code=start
func removeDuplicates(nums []int) int {
	slow := 0
	for fast := 1; fast < len(nums); fast++ {
		if nums[fast] == nums[slow] {
			continue
		} else {
			slow++
			nums[slow] = nums[fast]
		}
	}
	return slow + 1
}

// @lc code=end
