from math import floor,ceil
def arrays_to_numbers(arr):
    if isinstance(arr, int):
        return Number(value=arr)
    else:
        return Number(left=arrays_to_numbers(arr[0]), right=arrays_to_numbers(arr[1]))
    


class Number():
    def __init__(self, left=None, right=None,value=None):
        assert ((left is not None) and (right is not None)) ^ (value is not None)
        self.left=left
        self.right=right
        self.value = value

    def mag(self):
        if self.value!=None:
            return self.value
        else:
            return 3*self.left.mag()+2*self.right.mag()

    def __repr__(self):
        if self.value!=None:
            return str(self.value)
        else:
            return "["+str(self.left)+", "+str(self.right)+"]"



def add(a,b):
    n = Number(left=a,right=b)
    return n


def find_array_with_big_number(n):
    if n.left.value!=None and n.left.value>=10:
        return n
    if n.left.value is None:
        q = find_array_with_big_number(n.left)
        if q:
            return q
    if n.right.value!=None and n.right.value>=10:
        return n
    if n.right.value is None:
        q = find_array_with_big_number(n.right)
        if q:
            return q
    return None

def split(n):
    p = find_array_with_big_number(n)
    if p:
        if p.left.value!=None and p.left.value>=10:
            p.left=Number(left=floor(p.left.value/2), right=ceil(p.left.value/2))
        elif p.right.value!=None and p.right.value >=10:
            p.right=Number(left=floor(p.right.value/2), right=ceil(p.right.value/2))
        else:
            raise Exception("Oops")


data= """[[1,[2,14]],[1,11]]"""



for line in data.split("\n"):
    eq= eval(line)
    print(eq)
    n=arrays_to_numbers(eq)
    print(n)
    split(n)
    print(n)
    
