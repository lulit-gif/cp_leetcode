class Solution:
    def mostWordsFound(self, sentences: List[str]):
        output = 0
        for sentence in sentences:
            arr = sentence.split(" ")
            num = len(arr)
            if num > output:
                output = num
        return output
        