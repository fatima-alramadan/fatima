import numpy as np

class myClass:
    def __init__(self, arrList=[1,2,3,4,5,6]):
        self.arrList = arrList
    
    def return_max(self):

        maxVal = self.arrList[0]
    
        for num in self.arrList:
            if num > maxVal:
                maxVal = num
            
        return maxVal

    def return_min(self):
        minVal = self.arrList[0]
    
        for num in self.arrList:
            if num < minVal:
                minVal = num
            
        return minVal

    def return_max_squared(self):
        maxValue = self.arrList[0]
    
        for num in self.arrList:
            if num > maxValue:
                maxValue = num

        return maxValue*maxValue

    def return_length(self):
         count = 0
         for l in self.arrList:
            count += 1
         return count

    def return_positive_sum(self):
        posSum = 0
        for num in self.arrList:
            if num > 0 :
                posSum += num
                
        self.arrList[len(self.arrList)-1] = posSum
        
        return posSum

    def return_negative_count(self):
        counter = 0
        for num in self.arrList:
            if num < 0 :
                counter += 1

        return counter
 

    def positive_count(self):
        count = 0
        for num in self.arrList:
            if num > 0 :
                count += 1

        return count


        return 

    def negative_sum(self):
        negSum = 0
        for num in self.arrList:
            if num < 0 :
                negSum += num
                
        self.arrList[len(self.arrList)-1] = negSum
        
        return negSum
    

if __name__ == "__main__":
    myClass()
