/*
 * @lc app=leetcode id=69 lang=golang
 *
 * [69] Sqrt(x)
 */

package main

// @lc code=start
func mySqrt(x int) int {
	if x <= 0 {
		return 0
	}
	left := 0
	right := x + 1
	for left < right {
		mid := left + (right-left)>>1
		if mid*mid == x {
			return mid
		} else if mid*mid > x {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left - 1
}

// @lc code=end
