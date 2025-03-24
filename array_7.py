#calculate sum of the element of the array

arr = [54, 65, 75, 81, 21, 46]

class Sum:
    def __init__(self, arr):
        self.arr = arr
        self.result = 0


    def sum_it(self):
       for element in self.arr:
            self.result += element
       return self.result

obj1 = Sum(arr)

print(obj1.sum_it())