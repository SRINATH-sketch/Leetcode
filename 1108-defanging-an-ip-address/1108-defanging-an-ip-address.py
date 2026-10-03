class Solution:
    def defangIPaddr(self, address: str) -> str:
        r=address.replace(".","[.]")
        return r