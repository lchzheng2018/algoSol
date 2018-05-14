import time

class bItem(object):
  def __init__(self, timestamp, total, count):
    """
    :type timestamp: int (seconds) 
    :type total: int 
    :type count: int
    """
    self.ts = timestamp
    self.total = total
    self.count = count
    
class Solution(object):
  
  def __init__(self, n, unit=1):
    """
    :type n: int  - interval count
    :type unit: int - interval length (seconds)
    """
    self.wLen = n
    self.unit = unit
    # Initialize the buckets
    self.buckets = []
    for i in range(n + 1):
      self.buckets.append(bItem(0, 0, 0))

    # Initial bucket index
    self.index = -1    
    
  def addData(self, val):
    """
    :type val: int
    :rtype: void 
    """
    curtime = time.time()
    curTS = int(curtime) // self.unit
    
    if self.index == -1:
      self.index = 0
      self.buckets[0].ts = curTS
      self.buckets[0].total = val
      self.buckets[0].count += 1
      return 
  
    if curTS == self.buckets[self.index].ts:
      self.buckets[self.index].total += val
      self.buckets[self.index].count += 1
      return 
    
    # increase the self.buckets 
    oldIndex = self.index
    self.index = (oldIndex + 1) % (self.wLen + 1)
    self.buckets[self.index].ts = curTS
    self.buckets[self.index].total = self.buckets[oldIndex].total + val
    self.buckets[self.index].count = self.buckets[oldIndex].count + 1
    
  def getAverage(self):
    """
    :rtype: float 
    """
    if self.index == -1:
      return 0
    
    curtime = time.time()
    curTS = int(curtime) // self.unit
    
    n = self.wLen 
    lastTS = self.buckets[self.index].ts
    
    # No add in the last n interval
    if curTS - lastTS >= n:
      return 0
    
    targetTS = curTS - n
    targetIndex = -1
    pivot = self.index
    start = 0
    end = n
    while targetIndex == -1 and start <= end:
      mid = (start + end) / 2 
      midIndex = (mid + pivot + 1) % (n + 1)
      midNext = (midIndex + 1) % (n + 1)
      
      if self.buckets[midIndex].ts == targetTS:
        targetIndex = midIndex
      elif self.buckets[midIndex].ts > targetTS:
        end = mid - 1
      elif self.buckets[midNext].ts == targetTS:
        targetIndex = midNext
      elif self.buckets[midNext].ts > targetTS:
        targetIndex = midIndex
      else:
        start = mid + 1
    
    # It should never happen 
    if targetIndex == -1:
      print "something is wrong"
      return 0
    
    total = self.buckets[pivot].total - self.buckets[targetIndex].total
    count = self.buckets[pivot].count - self.buckets[targetIndex].count
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
