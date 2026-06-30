def build_lps(pattern):

    lps = [0] * len(pattern)
    prefix_len = 0  
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            lps[i] = prefix_len
            i += 1
        else:
            if prefix_len != 0:
                prefix_len = lps[prefix_len - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    if not pattern or not text:
        return []

    lps = build_lps(pattern)
    matches = []

    i = 0  
    j = 0  

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1] 
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches
