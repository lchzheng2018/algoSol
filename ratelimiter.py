# This is a solution for the rate limiter question in the 
# following URL
# https://www.careercup.com/question?id=5147519440912384
#
# Liagnchen Zheng, 2018

import time

class Solution(object):
    def __init__(self, n=0):
        """
        :type n: int
        """
        self.setLimit(n)
        
    
    def setLimit(self, n):
        """
        :type n: int
        """
        if n < 0:
            print "invalid input"
	    return 
        self.limit = n
        self.start = 0
        self.bucket = []

    def IsRequestAllow(self):
        curTime = time.time()         
        if len(self.bucket) < self.limit:
            self.bucket.append(curTime)
            return True 
        elif curTime - self.bucket[self.start] >= 1.0:
            self.bucket[self.start] = curTime 
            self.start = (self.start + 1) % self.limit
            return True
        else:
            return False 

        
        
obj = Solution()
obj.setLimit(2)

print time.time(), obj.IsRequestAllow()
print time.time(), obj.IsRequestAllow()
print time.time(), obj.IsRequestAllow()

time.sleep(0.5)
print time.time(), obj.IsRequestAllow()
time.sleep(0.5)
print time.time(), obj.IsRequestAllow()
