from math import *
print(":|Please Enter Number1|: ")
Number1 = input()
Operator = input(":|+ - / *  or  | ≈ - UP or Down |  Exp² |: ")
print(":|Please Enter Number2 :If Not */+- put 1|: ")
Number2 = input()
Number1 = float(Number1)
Number2 = float(Number2)
if Operator == "+":
  Sum = Number1 + Number2
  print(Sum)
if Operator == "-":
  Sum = Number1 - Number2
  print(Sum)
if Operator == "/":
  Sum = Number1 / Number2
  print(Sum)
if Operator == "*":
  Sum = Number1 * Number2
  print(Sum)
if Operator == "Up":
  Sum = floor(Number1)
  print(Sum)
if Operator == "Down":
  Sum = ceil(Number1)
  print(Sum)
if Operator == "Exp" or "exp" or "e" or "Exp²" or "exp²" or "Exp2" or "exp2" :
  print("Type the Exponent you would like: ")
  Exponent = input()
  Exponent = int(Exponent)
  Sum = pow(Number1, Exponent)
  print(Sum)
