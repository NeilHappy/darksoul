/*
 * @lc app=leetcode id=904 lang=golang
 *
 * [904] Fruit Into Baskets
 */

package main

// @lc code=start
func totalFruit(fruits []int) int {
	cntMap := map[int]int{}
	//length := len(fruits)
	left := 0
	ans := 0
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
		ans = max(ans, right-left+1)

	}
	return ans

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
