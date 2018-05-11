########################################################
# A simple version of getAve of last n * unit seconds. #
# It will be n minutes if "unit" is set to 60.         #
# For test purpose, the default unit is 1 second.      #
#   O(1) addData                                       #
#   O(n) getAverag                                     #
########################################################
import time 

class Solution(object):
    class buckItem(object):
        def __init__(self, total, count, timestamp):
            """
            :type total: int
            :type count: int
            """
            self.total = total 
            self.count = count 
            self.ts = timestamp
            
            
    def __init__(self, n, unit = 1):
        """
        :type n: int
        :type unit: int
        :rtype: void
        """
        self.tLen = n 
        self.unit = unit 
        
        
        # Intialize the buckets
        self.buckets = []
        self.index = -1
        for i in range(n):
            self.buckets.append(self.buckItem(0, 0, 0))
    
    def addData(self, val):
        """
        :type val: int
        :rtype: void  
        """
        
        curTime = time.time()
        cur = int(curTime) // self.unit
        
        if self.index < 0:
            self.index = 0
            self.buckets[self.index].ts = cur
            self.buckets[self.index].total = val
            self.buckets[self.index].count = 1
            return 
    
        last = self.buckets[self.index].ts
        diff = cur - last    
        
        self.index = (self.index + diff) %  (self.tLen)
        if self.buckets[self.index].ts == cur:
            self.buckets[self.index].total += val
            self.buckets[self.index].count += 1
        else:
            self.buckets[self.index].ts = cur
            self.buckets[self.index].total = val
            self.buckets[self.index].count = 1
    
    
    def getAverage(self):
        """
        :rtype: float 
        """
        
        if self.index < 0:
            return 0
        
        curTime = time.time()
        cur = int(curTime) // self.unit
        
        total = count = 0
        for i in range(self.tLen):
            if cur - self.buckets[i].ts < self.tLen:
                total += self.buckets[i].total
                count += self.buckets[i].count
    
        return (total * 1.0) / count if count > 0 else 0
  
  
"""
Unit Test
"""       
obj = Solution(2)
obj.addData(15)
obj.addData(20)
print obj.getAverage()
time.sleep(2.0)
obj.addData(20)
obj.addData(21)
print obj.getAverage()
time.sleep(1.0)
#print obj.getAverage()
obj.addData(22)
print obj.getAverage()
time.sleep(2.0)
print obj.getAverage()
obj.addData(20)
obj.addData(21)
time.sleep(1.0)
obj.addData(22)
obj.addData(28)
print obj.getAverage()        
time.sleep(1.0)
obj.addData(33)
obj.addData(20)
print obj.getAverage() 
time.sleep(1.0)
print obj.getAverage()
time.sleep(1.0)
print obj.getAverage()
