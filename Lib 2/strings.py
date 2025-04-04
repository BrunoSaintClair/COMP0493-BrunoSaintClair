def kmp(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0 
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    result = []
    i = j = 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def rabin_karp(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1, q)
    p = 0 
    t = 0
    result = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                result.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return result

def boyer_moore(text, pattern):
    def bad_char_heuristic(pattern):
        bad_char = [-1] * 256
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    bad_char = bad_char_heuristic(pattern)
    m = len(pattern)
    n = len(text)
    result = []

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            result.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return result


# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"

# print("KMP:", kmp(text, pattern))
# print("Boyer-Moore:", boyer_moore(text, pattern))
# print("Rabin-Karp:", rabin_karp(text, pattern))
