
if str1 + str2 != str2 + str1:
    return ""

max_len = gcd(len(str1), len(str2))
return str1[:max_len]