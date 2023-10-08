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
	for {
		current := x / 2
		next := current + 1
		if current*current <= x && next*next > x {
			return current
		}
		x = current
	}
}

// @lc code=end
