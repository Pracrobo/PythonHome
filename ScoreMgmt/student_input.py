# stuudent_input
def myinput(student):
    name = input("Enter your name : " )
    kor = int(input("Enter your Korea : "))
    eng = int(input("Enter your English : "))
    math = int(input("Enter your Math : "))
    student["name"] = name
    student["kor"] = kor  
    student["eng"] = eng
    student["math"] = math
   #  print(type())