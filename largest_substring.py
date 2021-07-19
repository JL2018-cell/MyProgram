def largest_substring(s):
    i = j = lon = 0
    chars = set()
    while j < len(s):
        if s[j] not in chars:
            chars.add(s[j])
            j = j + 1
            lon = max(lon, len(chars))
        else:
            chars.remove(s[i])
            i = i + 1
    return lon

s = "abcabcabcFFF"
print(largest_substring(s))
