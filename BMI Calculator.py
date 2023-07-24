#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# 

# In[43]:


Name= input("Enter your name :  ")
Weight= int(input("Enter weight in pound : "))

Height= int(input("Enter Height in inches : "))

BMI= (Weight * 703)/(Height * Height)

print("BMI is : ",BMI)

if (BMI > 0):
    if (BMI <= 18.5):
        print(Name + "You are Underweight")
    elif (BMI <= 24.9):
        print(Name + " You are Normal weight")
    elif (BMI <= 29.9):
        print(Name + " You are Overweight")
    elif (BMI > 30):
        print(Name + " You are obese")
else:
    print(Name + " Please enter a valid input")


# In[ ]:





# In[ ]:




