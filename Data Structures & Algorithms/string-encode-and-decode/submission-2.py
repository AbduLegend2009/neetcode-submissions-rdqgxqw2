class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for z in strs:
            k = len(z)
            s+= str(k) + "#" + z
        return s
    def decode(self, s: str) -> List[str]:
        j = s.find("#")
        k = []
        while s.find("#") != -1:
            l = int(s[:j])
            if l!=0:
                k.append(s[j+1: j+l+1])
                s = s[j+l+1:]
                j = s.find("#")
            else:
                k.append("")
                s = s[j+1:]
                j = s.find("#")
        return k


        