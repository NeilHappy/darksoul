/*
 * @lc app=leetcode id=209 lang=golang
 *
 * [209] Minimum Size Subarray Sum
 */
package main

// @lc code=start
func minSubArrayLen(target int, nums []int) int {
	left := 0
	sum := 0
	length := len(nums) + 1
	for right, v := range nums {
		sum += v
		for sum >= target {
			cLen := right - left + 1
			length = min(cLen, length)
			sum -= nums[left]
			left++
		}
	}
	if length == len(nums)+1 {
		return 0
	}
	return length
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
