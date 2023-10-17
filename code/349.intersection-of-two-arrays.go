/*
 * @lc app=leetcode id=349 lang=golang
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
package main

func intersection(nums1 []int, nums2 []int) []int {
	result := []int{}
	set := make(map[int]int)
	for _, v := range nums1 {
		set[v] = 1
	}
	for _, v := range nums2 {
		if _, ok := set[v]; ok {
			result = append(result, v)
			delete(set, v)
		}
	}
	return result
}

// @lc code=end
