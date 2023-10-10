/*
 * @lc app=leetcode id=844 lang=golang
 *
 * [844] Backspace String Compare
 */

// @lc code=start

package main

import "fmt"

func backspaceCompare(s string, t string) bool {
	return getCleanStr(s) == getCleanStr(t)
}

func getCleanStr(s string) string {
	resultSlice := make([]byte, len(s))
	slow := 0
	for fast := 0; fast < len(s); fast++ {
		if s[fast] != '#' {
			resultSlice[slow] = s[fast]
			slow++
		} else {
			if fast == 0 {
				continue
			} else {
				slow--
			}
		}
	}
	fmt.Println(resultSlice)
	return string(resultSlice[:slow])

}
func main() {
	fmt.Printf("%s\n", getCleanStr("a#c"))
}

// @lc code=end
