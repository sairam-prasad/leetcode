class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        maximum,words=0,0
        for i in range(len(sentences)):

            words = len(sentences[i].split())
            maximum=max(words,maximum)
        return maximum