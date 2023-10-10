/*
 * @lc app=leetcode id=704 lang=golang
 *
 * [704] Binary Search
 */
package main

// @lc code=start
func search(nums []int, target int) int {
	left, right := 0, len(nums)
	for left < right {
		mid := left + (right-left)>>1
		if target == nums[mid] {
			return mid
		} else if target < nums[mid] {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return -1
}

// @lc code=end
