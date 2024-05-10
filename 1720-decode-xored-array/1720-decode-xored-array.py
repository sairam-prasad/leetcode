class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        arr=[first]

        for i in encoded:
            x=i^first
            arr.append(x)
            first=x
        return arr