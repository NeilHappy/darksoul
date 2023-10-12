/*
 * @lc app=leetcode id=69 lang=golang
 *
 * [69] Sqrt(x)
 */

package main

// @lc code=start
func mySqrt(x int) int {
	low := 0
	high := x + 1
	for low < high {
		mid := low + (high-low)>>1
		if mid*mid == x {
			return mid
		} else if mid*mid > x {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low - 1
}

// @lc code=end
