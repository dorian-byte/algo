def generatePossibleNextMoves(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    for i in xrange(len(s)-1):
        if s[i] == s[i+1] == '+':
            tmp = s[:i] + '--' + s[i+2:]
            res.append(tmp)
    return res
