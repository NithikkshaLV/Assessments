# -*- coding: utf-8 -*-
"""internal1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v20RHLkf-P-Z8qIfG6VE4UeCOSA2WZcV
"""

#1
length=int(input("Enter the length in meters: "))
width=int(input("Enter the width in meters: "))
area=length*width
print("area is", area)
if area <200:
  print("It is small area")
elif area<500:
  print("It is medium area")
else:
  print("It is Large area")

#2
weight=float(input("Enter the weight in kilogram: "))
height=float(input("Enter the height in meters: "))
bmi=weight/(height**2)
print(bmi)

#If bmi is between 18-24 then it is considered as normal bmi.

#3
d={
    "nithi": 100,
    "sam": 90,
    "ram": 30
}
print(d)
num=int(input("enter a number: "))
def add(num):
  d.append(num)
  return d
def update(num):
  d['nithi']=99
  return d
def retrieve(num):
  return d

#4
age=int(input("Enter your age: "))
if age<12:
  print("You are a children")
elif age<20:
  print("You are a teenager")
elif age<40:
  print("You are an adult")
else:
  print("You are a senior")

#5
evn=[]
num=int(input("enter the number of subscriber id: "))
for i in range(num):
  lst=int(input("enter an even number: "))
  if lst%2==0:
    evn.append(lst)
  else:
    print("Please enter an even number")
    break
print(evn)

#6
password="qwerty12345"
user=input("enter your password: ")
while True:

  if user!=password:
    print("enter the correct password")
    break
  elif user==password:
    print("correct password")
    break

#7
l=[1,2,3,4,5,6,7,8]
sum=0
def avg_scores(l1):
  for i in range(len(l)):
    sum=sum+i
    return sum
for i in range(len(l)):
  sum=sum+l[i]
print(sum)
average=sum/len(l)
print("average is",average)

#8
s=input("enter a string: ")
ans=0
for i in range(len(s)):
  if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
    ans=ans+1
print("count of vowels", ans)

#9
import datetime
s=datetime.datetime.now()
print(s)

#13
with open("sample.txt", 'w') as log_file:
  print(log_file.write("daily status reports"))
  log_file.close()

#14
with open("sample.txt", 'r') as log_file:
  print(log_file.read())
  log_file.close()

#15
with open("sample.txt", 'a') as log_file:
  print(log_file.write("company news: 100 revenue id generated"))
  print(log_file.write("stock performance: Good"))
  print(log_file.write("industry news: delivered"))
  log_file.close()

#10
try:
  p=int(input("enter the amount: "))
  n=int(input("enter the time: "))
  r=int(input("enter the interest: "))
  si=p*n*r/100
  print(si)
except ValueError:
  print("enter an integer")

#11
try:
  name=str(input("enter your name: "))
  age=int(input("enter your age: "))
except ValueError:
  print("invalid")
except TypeError:
  print("invalid datatype")

#12
try:
  num=int(input("enter a numerator:"))
  den=int(input("enter a denominator: "))
  d=num/den
  print(d)
except ZeroDivisionError:
  print("Invalid input")