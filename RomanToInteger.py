values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s):
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                res += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                res += values[s[i]]
                i += 1
        return res
