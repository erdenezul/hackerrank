from __future__ import division
from sys import stdin
from collections import defaultdict

def lcs(s1, s2):
    prev = defaultdict(int)
    for i in range(len(s1)):
        cur = defaultdict(int)
        for j in range(len(s2)):
            #cur[j] = ??? if s1[i] == s2[j] else max(cur[j - 1], prev[j])
            cur[j] = prev[j-1]+1 if s1[i] == s2[j] else max(cur[j - 1], prev[j])
        prev = cur
    return prev[len(s2)-1]
                
def main():
    s, t = stdin.next().strip(), stdin.next().strip()
    print lcs(s, t)

main()
