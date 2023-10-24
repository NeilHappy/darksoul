/*
 * @lc app=leetcode id=904 lang=golang
 *
 * [904] Fruit Into Baskets
 */

package main

// @lc code=start
func totalFruit(fruits []int) int {
	left := 0
	cntMap := make(map[int]int)
	result := 0
	for right, v := range fruits {
		cntMap[v]++
		for len(cntMap) > 2 {
			y := fruits[left]
			cntMap[y]--
			if cntMap[y] == 0 {
				delete(cntMap, y)
			}
			left++
		}
		result = max(result, right-left+1)
	}
	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
