class rectangle:
    def __init__(self, num):
        self.num = num

    @classmethod
    def area (cls,lis):
        return cls(lis*lis)

    @classmethod
    def perimeter(cls,lis):
        return cls(2*(lis+lis))
    
my_list1 = [1, 2, 3, 4, 5]
obj = rectangle.area(my_list1)
print(obj.num)

total = rectangle.perimeter(my_list1)
print(total)
