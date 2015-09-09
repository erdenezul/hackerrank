s = raw_input()
count = {}
for i in range(len(s)):
    if s[i] not in count: count[s[i]] = 0
    count[s[i]] += 1
isPalindrome = True
hasOdd = False
#if (???): hasOdd = True
if bool([x for x in count if count[x]%2!=0]): hasOdd = True
for k in count:
    if count[k] % 2 != 0:
        if hasOdd: hasOdd = False
        else:
            isPalindrome = False
            break
print "YES" if isPalindrome else "NO"
