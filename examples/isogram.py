def is_isogram(s):
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

#s="Machine" # Not an isogram
s="isogram" # Is an isogram

print("Test String =", s)

if (is_isogram(s)):
    print("is_isogram = Yes")
else:
    print("is_isogram = No")
