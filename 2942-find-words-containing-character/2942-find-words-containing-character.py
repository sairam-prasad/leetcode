class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        arr=[]
        for i in range(len(words)):
            if words[i].find(x)>=0:
                print(words[i].find(x))
                arr.append(i)
                print(arr)
        return arr

        