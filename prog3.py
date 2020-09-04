#Assigning elements to different lists...
def lis():
    list = []
    n = int(input("Enter number of elements to be entered in the list: "))
    print("Enter elements to be entered in list")
    for i in range(0,n):
        a = int(input())
        list.append(a)
    print("List after assingning values: ",list)

#Accessing elements from a tuple...
def tup():
    tuple = ("mango","banana","apple","pineapple")
    print(tuple)
    a = int(input("Enter index of the element to be accessed:"))
    print(tuple[a])

#Deleting different dictionary elements...
def di():
    car = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
    print(car)
    a = input("Enter element to be deleted: ")
    del car[a]
    print("Dictionary after deleting the given element: ",car)

print("Enter 1 for list, 2 for tuple, 3 for dictionary")
a = int(input())
if a==1:
    lis()
elif a==2:
    tup()
elif a==3:
    di()
else:
    print("Wrong choice...")
