class circle:
 def __init__(self):
     self._pi = 3.14
     self.a = 24

 def show(self):
     print("private: ",self._pi)
# Driver code
obj1 = circle()
print(obj1._pi)
