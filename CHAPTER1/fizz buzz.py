class Solution:
    def fizzBuzz(self, n: int):
        output =[]
        for i in range(1,n+1):
            if i %3 == 0:
                soln= "Fizz"
                if i%5 ==0:
                    soln += "Buzz"
            elif i% 5 == 0:
                soln ="Buzz"
            else:
                soln = str(i)
            output.append(soln)
        return output



            
        

        
