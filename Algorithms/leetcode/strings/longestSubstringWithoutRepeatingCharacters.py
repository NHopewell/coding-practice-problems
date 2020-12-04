# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def length_of_longest_substring(string: str) -> int:
    """
    Given a string, return the length of the longest
    non-repeating substring.

    ======
    >>> In: res = length_of_longest_substring("trstvghvl")
    >>> In: print(res)
    >>> Out: 4  # why? len("tvgh") = 4
    """
    pointer_a = 0
    pointer_b = 0
    longest_substring = []
    _max = 0

    while pointer_b < len(string):
        # if value at pointer b not in set
        if string[pointer_b] not in longest_substring:
            longest_substring.append(string[pointer_b])
            # increment b
            pointer_b += 1
            _max = max(len(longest_substring), _max)
        else:
            longest_substring.remove(string[pointer_a])
            pointer_a += 1

    return _max


def test(string, func):

    expected = 3
    actual = func(string)

    print(f"expected: {expected}, actual {actual}")
    assert(actual == expected)
    


test("pwwkew", length_of_longest_substring)

