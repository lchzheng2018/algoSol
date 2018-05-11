########################################################
# A bettr version of getAve of last n * unit seconds   #
# It will be n minutes if "unit" is set to 60.         #
# For test purpose, the default unit is 1 second.      #
#   O(1) addData via circular buffer                   #
#   O(log(n)) getAverag via binary search              #
########################################################

import time

class bItem(object):
    def __init__(self, timestamp, total, count):
        """
        :type timestamp: int 
        :type total: int
        :type count: int
        """
        self.ts = timestamp
        self.total = total
        self.count = count
        

class Solution(object):
    def __init__(self, n, unit=1):
        """
        :type n: int -the time window lenght
        :type unit: int - the interval of each windown item
        """
        
        self.tLen = n
        self.unit = unit
        
        # create a n + 1 circurla buffet 
        self.index = -1
        self.buckets = []
        for i in range(n + 1):
            self.buckets.append(bItem(0, 0, 0))
        
        
    def addData(self, val):
        """
        :type val: int
        """
        
        curTime = time.time()
        cur = int(curTime) // self.unit
        
        if self.index == -1:
            self.index = 0
            self.buckets[0].ts = cur
            self.buckets[0].total = val
            self.buckets[0].count = 1
            return 
        
        last = self.buckets[self.index].ts
        if cur - last == 0:
            self.buckets[self.index].total += val
            self.buckets[self.index].count += 1
        else:
            # remove the oldest data 
            nextIndex = (self.index + 1) % (self.tLen + 1)
            
            # add the new data 
            self.buckets[nextIndex].ts = cur
            self.buckets[nextIndex].total = self.buckets[self.index].total + val
            self.buckets[nextIndex].count = self.buckets[self.index].count + 1
            self.index = nextIndex
        #print "index, total, count", self.index, self.buckets[self.index].total, self.buckets[self.index].count
        
    
    
    def getAverage(self):
        """
        :rtype: float
        """
        
        if self.index == -1:
            return 0
        
        curTime = time.time()
        cur = int(curTime) // self.unit
        last = self.buckets[self.index].ts
        
        
        # No add in the last n window
        if cur - last >= self.tLen:
            return 0
          
        pivotTS = cur - self.tLen
        pivotIndex = -1
        
        #print "cur, last, pivotTS", cur, last, pivotTS
        #print self.buckets
      
        endIndex = (self.index - 1) % (self.tLen + 1)
        if self.buckets[endIndex].ts <= pivotTS:
            pivotIndex = endIndex
            
        startIndex = (self.index - (last - pivotTS)) % (self.tLen + 1)
        
        if self.buckets[startIndex].ts == pivotTS:
            pivotIndex = startIndex
        
    
        start = 0
        end = last + self.tLen - cur 
        #print "start, end, startIndex", start, end, startIndex
        # Binary search to find  the latest bucket with ts <= cur - n   
        while pivotIndex == -1 and start <= end:
            mid = (start + end) / 2
            index = (startIndex + mid) % (self.tLen + 1)
            #print "search index", index
            nextIndex = (index + 1) % (self.tLen + 1)
            
            # According to the previous condition, there should be always a point
            if self.buckets[index].ts > pivotTS:
                end = mid - 1
            elif self.buckets[index].ts == pivotTS:
                pivotIndex = index
            elif self.buckets[nextIndex].ts == pivotTS:
                pivotIndex = nextIndex
            elif self.buckets[nextIndex].ts > pivotTS:
                pivotIndex = index
            else:
                start = mid + 1
    
        #print "startIndex, pivotIndex", startIndex, pivotIndex
        #self.printBuckets()
        total = self.buckets[self.index].total - self.buckets[pivotIndex].total 
        count = self.buckets[self.index].count -  self.buckets[pivotIndex].count
        
        return total * 1.0 / count if count > 0 else 0
    
  
    def printBuckets(self):
        print "last Index:", self.index
        for i in range(len(self.buckets)):
            print "Index i:", i, self.buckets[i].ts, self.buckets[i].total, self.buckets[i].count
      
        
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


"""
Test Results with some print statements:

index, total, count 0 35 2
17.5
index, total, count 1 55 3
index, total, count 1 76 4
20.5
index, total, count 2 98 5
search index 1
search index 0
21.0
0
index, total, count 0 118 6
index, total, count 0 139 7
index, total, count 1 161 8
index, total, count 1 189 9
search index 0
search index 2
22.75
index, total, count 2 222 10
index, total, count 2 242 11
25.75
26.5
0
"""
