def permutation(s):
    permutation_internal(s, '')


def permutation_internal(s, prefix):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[:i] + s[i + 1:]
            permutation_internal(rem, prefix + s[i])


permutation("cat")