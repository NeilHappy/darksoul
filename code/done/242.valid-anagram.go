/*
 * @lc app=leetcode id=242 lang=golang
 *
 * [242] Valid Anagram
 */

// @lc code=start
func isAnagram(s string, t string) bool {
	record := [26]int{}
	for _, r := range s {
		record[r-rune('a')]++
	}
	for _, r := range t {
		record[r-rune('a')]--
	}

	return record == [26]int{}
}

// @lc code=end

