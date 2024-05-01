class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        i=0
        for i in range(len(word)):
            if word[i]==ch:
                break

        if i==len(word)-1 and ch not in word:
            return word
        

        low,high = 0,i
        li = list(word)
        
        while low<=high:
            temp= li[low]
            li[low]= li[high]
            li[high]=temp
            low=low+1
            high=high-1
        
        return "".join(li)        