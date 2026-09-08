class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_str = ''
        for str in strs:
            encoded_str += f"{len(str)}#{str}"
        return encoded_str




    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i            
            while s[j] != '#':
                j += 1

            length = int(s[i:j]) # Slicing will give the length of string
            res.append(s[j+1:j+1 + length]) # Append the word in list
            i = j+1 + length
        return res
