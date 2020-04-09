#!/usr/bin/env python3

fahrenheit = float(input("Please enter the fahrenheit tempreture you'd like converting to Celsius: "))
print(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)
print("Your fahrenheit tempreture",fahrenheit,"F is",round(celsius,2),"C in Celsius")