"""
LeetCode-394

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution:
    @staticmethod
    def decode_string(s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        res = ''
        encode = list(s)
        decode = []

        while encode:
            encode_ch = encode.pop()
            if encode_ch == '[':
                digit_str = ''
                digit_ch = encode.pop()
                while encode and digit_ch.isdigit():
                    digit_str = digit_ch + digit_str
                    digit_ch = encode.pop()

                if not digit_ch.isdigit():
                    encode.append(digit_ch)
                else:
                    digit_str = digit_ch + digit_str

                decode_ch = decode.pop()
                decode_str = ''
                while decode_ch != ']':
                    decode_str += decode_ch
                    decode_ch = decode.pop()

                decode_str = decode_str * int(digit_str)
                decode.append(decode_str)
            else:
                decode.append(encode_ch)

        while decode:
            res += decode.pop()

        return res


print(Solution().decode_string('20[a]'))
