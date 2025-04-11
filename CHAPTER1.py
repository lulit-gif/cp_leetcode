class Solution:
    def addDigits(self, num: int):
        while num>9:
            digit = 0
            while num:
                digit +=(num%10)
                num//=10
            num = digit

<<<<<<<< HEAD:CHAPTER1/AddDigits.py
        return num
========
        return num

        
>>>>>>>> 654e181906a9527d147d884f9561ab2203823a7e:CHAPTER1.py
