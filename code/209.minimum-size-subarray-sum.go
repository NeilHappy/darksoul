/*
 * @lc app=leetcode id=209 lang=golang
 *
 * [209] Minimum Size Subarray Sum
 */
package main

// @lc code=start
func minSubArrayLen(target int, nums []int) int {
	length := len(nums)
	left := 0
	sum := 0
	minLength := length + 1
	for right := 0; right < length; right++ {
		sum += nums[right]
		for sum >= target {
			curLength := right - left + 1
			if minLength > curLength {
				minLength = curLength
			}
			sum -= nums[left]
			left++
		}
	}
	if minLength == length+1 {
		return 0
	}
	return minLength

}

func main() {

}

// @lc code=end
