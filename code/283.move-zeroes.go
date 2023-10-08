/*
 * @lc app=leetcode id=283 lang=golang
 *
 * [283] Move Zeroes
 */

package code

// @lc code=start
func moveZeroes(nums []int) {
	slow := 0
	for fast := 0; fast < len(nums); fast++ {
		if nums[fast] != 0 {
			nums[slow] = nums[fast]
			slow++
		} else {
			continue
		}
		/*
			if nums[fast] == 0 {
				continue
			} else {
				nums[slow] = nums[fast]
				slow++
			}
		*/
	}
	for i := slow; i < len(nums); i++ {
		nums[i] = 0
	}

}

// @lc code=end
