/*
 * @lc app=leetcode id=367 lang=golang
 *
 * [367] Valid Perfect Square
 */
package main

// @lc code=start
func isPerfectSquare(num int) bool {
	left := 0
	right := num + 1
	for left < right {
		mid := left + (right-left)>>1
		if mid*mid == num {
			return true
		} else if mid*mid < num {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return false
}

// @lc code=end
