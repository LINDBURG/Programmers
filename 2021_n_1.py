def decode(m, k):
    mdx = 0
    kdx = 0
    result = ''
    while kdx < len(k) or mdx < len(m):
        if mdx < len(m) and (kdx >= len(k) or m[mdx] != k[kdx]):
            result += m[mdx]
        else:
            kdx += 1
        mdx += 1

    return result

def solution(m, k):
    return decode(m,k)