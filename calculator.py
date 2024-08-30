nameOfuser = input("Please enter your name: ")
print("Welcome",nameOfuser,",","\n This is a handmade calculator made by Rahul")
print("Please enter number and operator to calculate")
r1 = int(input("Enter large number first: "))
r2 = int(input("Enter small number now: ")) 
Calc = input("Enter operator (+,-,*,/,//,%): ")

add = '+'
sub = '-'
mul = '*'
div1 = '/'
div2 = '//'
rem = '%'

if Calc==add :
    print("Adding..",r1,"+",r2,"=",r1+r2,"Answer")
elif Calc==sub :
    print("Subtracting..",r1,"-",r2,"=",r1-r2,"Answer")
elif Calc==mul :
    print("Multiplying..",r1,"*",r2,"=",r1*r2,"Answer")
elif Calc==div1 :
    print("Dividing..",r1,"/",r2,"=",r1/r2,"Answer")
elif Calc==div2 :
    print("Dividing..",r1,"//",r2,"=",r1//r2,"Answer")
elif Calc==rem :
    print("Remainder of..",r1,"%",r2,"=",r1%r2,"Answer")

else :
    print("Please input the operator sign wisely!")
