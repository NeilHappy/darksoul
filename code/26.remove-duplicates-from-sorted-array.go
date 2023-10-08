/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

package code

// @lc code=start
func removeDuplicates(nums []int) int {
	slow := 0
	for fast := 1; fast < len(nums); {
		if nums[fast] == nums[slow] {
			fast++
		} else {
			slow++
			nums[slow] = nums[fast]
		}
	}
	return slow + 1

}

// @lc code=end
