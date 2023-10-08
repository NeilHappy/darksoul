/*
 * @lc app=leetcode id=69 lang=golang
 *
 * [69] Sqrt(x)
 */

package code

// @lc code=start
func mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	left := 0
	right := x
	ans := 1
	for left <= right {
		mid := left + (right-left)>>1
		if mid*mid == x {
			return mid
		} else if mid*mid < x {
			left = mid + 1
		} else {
			right = mid - 1
			ans = right
		}
	}
	return ans
}

// @lc code=end
