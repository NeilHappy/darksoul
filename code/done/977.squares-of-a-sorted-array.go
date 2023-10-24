/*
 * @lc app=leetcode id=977 lang=golang
 *
 * [977] Squares of a Sorted Array
 */

package main

// @lc code=start
func sortedSquares(nums []int) []int {
	length := len(nums)
	result := make([]int, length)
	left := 0
	right := length - 1
	k := length - 1
	for left <= right {
		if nums[left]*nums[left] > nums[right]*nums[right] {
			result[k] = nums[left] * nums[left]
			left++
		} else {
			result[k] = nums[right] * nums[right]
			right--
		}
		k--
	}
	return result
}

// @lc code=end
