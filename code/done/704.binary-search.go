/*
 * @lc app=leetcode id=704 lang=golang
 *
 * [704] Binary Search
 */
package main

// @lc code=start
func search(nums []int, target int) int {
	left := 0
	right := len(nums)
	for left < right {
		mid := left + (right-left)>>1
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return -1
}

// @lc code=end
