/*
 * @lc app=leetcode id=27 lang=golang
 *
 * [27] Remove Element
 */
package main

// @lc code=start
func removeElement(nums []int, val int) int {
	slow := 0
	for fast := 0; fast < len(nums); fast++ {
		if nums[fast] == val {
			continue
		} else {
			nums[slow] = nums[fast]
			slow++
		}
	}
	return slow
}

// @lc code=end
