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
