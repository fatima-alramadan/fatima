import numpy as np

class myClass:
    def __init__(self,arrList):
        self.arrList = arrList
    
    def return_max(arrList):

        maxVal = arrList[0]
    
        for num in arrList:
            if num > maxVal:
                maxVal = num
            
        return maxVal

    def return_min(arrList):
        minVal = arrList[0]
    
        for num in arrList:
            if num < minVal:
                minVal = num
            
    return minVal

    def return_max_squared(arrList):
        maxVal = arrList[0]
    
        for num in arrList:
            if num > maxVal:
                maxVal = num

        return maxVal* maxVal

    def return_length(arrList):
         count = 0
        for l in arrList:
            count += 1
        return count

    def return_positive_sum(arrList):
          posSum = 0
        for num in arrList:
            if num > 0 :
                posSum += num
                
        arrList[len(arrList)-1] = posSum
        
        return arrList

    def return_negative_count(arrList):
        counter = 0
        for num in arrList:
            if num < 0 :
                counter += 1

        return arrList

    def sum(arrList):
        sum1 = 0
        for num in arrList:
            sum1 += num
        return sum1  

    def average(arrList):
        sum1 = 0
        for n in arrList:
            sum1 += n
        return (sum1/len(arrList))  
    

if __name__ == "__main__":
    myClass()