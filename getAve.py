import time

class Solution(object):
    def __init__(self, interval):
        """
        :type interval: int
        """
        self.interval = 0
        self.buckets = []
        if interval < 0:
            print "Invalid input" 
            return 
        
        self.interval = interval 
        self.total = 0
        self.count = 0
        self.bucket_index = 0
        # Initialize each bucket item, [timestamp, totalValue, count]
        for i in range(self.interval):
            self.buckets.append([0, 0, 0])
        
    
    def addData(self, value):
        """
        :type value: int
        """
        
        # add the data to the proper bucket 
        timestamp = int(time.time() // 1)
        print "addData:", value, " at", timestamp 
        if self.count == 0:
            self.buckets[self.bucket_index] = [timestamp, value, 1]  
            self.total = value 
            self.count = 1
            return 
        
    
        last_timestamp = self.buckets[self.bucket_index][0]
        diff = timestamp - last_timestamp
        if diff == 0:  
            
            self.buckets[self.bucket_index][1] += value
            self.buckets[self.bucket_index][2] += 1
            self.total += value
            self.count += 1
            
        elif diff >= self.interval: #exceed
            
            self.bucket_index = 0
            for i in range(self.interval):
                self.buckets[i] = [0, 0, 0]
                
            self.buckets[self.bucket_index][0] = timestamp  # set the timetampe
            self.buckets[self.bucket_index][1] = value      # set the total 
            self.buckets[self.bucket_index][2] = 1          # set the count
            self.total = value 
            self.count = 1

        else:
            # If add is often, this forloop will be executed at most 1
            for i in range(1, diff + 1):
                # get the actually index 
                index = (self.bucket_index + i) % self.interval
                # remove out of data value, though maybe 0
                self.total -= self.buckets[index][1]
                self.count -= self.buckets[index][2]
                # reset the buffer 
                self.buckets[index] = [last_timestamp + i, 0, 0]
                
            self.bucket_index = (self.bucket_index + diff) % self.interval
            self.buckets[self.bucket_index] = [timestamp, value, 1]
                
            self.total += value
            self.count += 1
        

    def getAverage(self):
        """
        :rtype value: float 
        """
        timestamp = int(time.time() // 1)
        print "getAverage at time:", timestamp
        last_timestamp = self.buckets[self.bucket_index][0]
        diff = (timestamp - last_timestamp) // 1
        if diff == 0:
            return (self.total * 1.0 / self.count ) if self.count > 0 else 0
        elif diff >= self.interval:
            self.bucket_index = 0

            for i in range(self.interval):
                self.buckets[i] = [0, 0, 0]
            
            self.buckets[self.bucket_index][0] = timestamp
                
            self.total = 0 
            self.count = 0
            print "here"
            return 0
            
        
        # If add is often, this forloop will be executed at most 1
        for i in range(1, diff + 1): 
            # get the actually index 
            index = (self.bucket_index + i) % self.interval
            # remove out of data value, though maybe 0
            self.total -= self.buckets[index][1]
            self.count -= self.buckets[index][2]
            # reset the buffer 
            self.buckets[index] = [last_timestamp + i, 0, 0]
        
        self.bucket_index = (self.bucket_index + diff) % self.interval
        self.buckets[self.bucket_index] = [timestamp, 0, 0]
        
        return (self.total * 1.0 / self.count ) if self.count > 0 else 0
        
        
        
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
time.sleep(1.0)
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
Execution Results:
addData: 15  at 1525301366
addData: 20  at 1525301366
getAverage at time: 1525301366
17.5
addData: 20  at 1525301368
addData: 21  at 1525301368
addData: 22  at 1525301369
getAverage at time: 1525301369
21.0
getAverage at time: 1525301371
here
0
addData: 20  at 1525301371
addData: 21  at 1525301371
addData: 22  at 1525301372
addData: 28  at 1525301372
getAverage at time: 1525301372
22.75
addData: 33  at 1525301373
addData: 20  at 1525301373
getAverage at time: 1525301373
25.75
getAverage at time: 1525301374
26.5
getAverage at time: 1525301375
0
"""
