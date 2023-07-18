#!/usr/bin/env python
# Python program to explain os.environ object  
  
# importing os module  
import os 
import pprint 
  
# Get the list of user's 
# environment variables 
env_var = os.environ 
  
# Print the list of user's 
# environment variables 
print("Printing current Environment variables:") 
pprint.pprint(dict(env_var), width = 1) 

