student = {} #1
def myinput (man) : #3
    name = input("Enter your Name: ")
    age = input("Enter your Age: ")
    man["name"] = name
    man["age"] = age#45

myinput(student) #2
print(student)#6

#호출과 정의 순서를 바꾸면 안됨