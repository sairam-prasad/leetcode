class Solution:
    def reverseWords(self, s: str) -> str:

        reverse = s.split(' ')
        reverse.reverse()
        print(reverse) 
        str=''
        for i in reverse:

            if len(i)>0:
                str+= i
                str+=" "


        return str.strip()