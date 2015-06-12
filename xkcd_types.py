#Operator overloading comes from: http://blog.teamtreehouse.com/operator-overloading-python
import math

class Types:
    def __init__(self,data):
        self.data = data
    def is_root(self,data,power):
        if math.pow(data,1/float(power)).is_integer():
            return True
        else:
            return False
    def is_sequence(self,listing):
        #print listing
        check_against = listing[:]
        check_against.sort()
        if check_against == listing:
            for i in xrange(1,15):
                if listing == range(listing[0],listing[-1]+1,i):
                    return True,"range",i
            for power in xrange(2,15):
                if all([self.is_root(elem,power) for elem in listing]):
                    return True,"power",power
        else:
            return False,None,None
        
    def __add__(self,other):
        if type(self.data) == type(int()) and type(other.data)==type(str()):
            other = int(other.data)
            return str(self.data + other)
        elif type(self.data) == type(str()) and type(other.data)==type(int()):
            data = int(self.data)
            return str(data+other.data)
        elif type(self.data)==type([]) and type(other.data)==type(int()):
            is_seq,hint,offset = self.is_sequence(self.data)
            if is_seq:
                if hint == "range":
                    if self.data[-1]+offset == other.data:
                        return True
                if hint == "power":
                    if (len(self.data)+1)**offset == other.data:
                        return True
                else:
                    return False
            else:
                return False
        elif type(self.data) == type(int()) and type(other.data) == type(int()):
            return "DONE"
        else:
            return False
