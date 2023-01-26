# a=9.5*4.5-2.5*3/45.5-3.5
# print(a)

# # Area of rectangle
# h=7.9
# w=4.5
# A=h*w
# print(A)

# Area of circle
# radius=eval(input("Enter the value for radius:"))
# Area=3.14*radius*radius
# print("The area of circle of radius",radius,"is",Area)

# displaytime.py
# second=eval(input("Enter the second:"))
# # get minutes in  given second
# minutes=second//60
# # seconds remaining
# remainingsecond=second%60
# print(second,"second is",minutes,"and",remainingsecond,"second")

# a=45+43%5*(23*3%2)
# print(a)
# print(5.1**2)

# pind the current time
import time
currenttime=time.time()
totalSecond = int(currenttime)
# get the current second
currentSecond=totalSecond%60
# get the total minutes
totalminutes=totalSecond//60
# compute the current minutes in houres
currentminutes=totalminutes%60
# get the total houres
totalhoures=totalminutes//60
# compute the currnt houres
currenthoures=totalhoures%24
print("current time is",currenthoures,":",currentminutes,":",currentSecond,"GMT")


