# link: https://leetcode.com/problems/encode-and-decode-strings/description/
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for word in strs:
            encoded_string += word + "jake"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list = []

        return s.split("jake")[:-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
