#!/usr/bin/env python
# coding: utf-8

# #### After creating each function specified below, write the necessary code in order to test your function.
# 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# 

# In[6]:


#this function is extremely simple, it simply returns true if a number is 2, and false otherwise
def is_two(numb):
    #this is how it determines if a number is 2
    if numb == 2 or numb == '2':
        
        return True
    
    else:
        
        return False


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[127]:


#This function determines whether or not a letter is a vowel
def is_vowel(n):
#using an if/else statement to return true if a letter is a vowel, and false otherwise    
    if n.lower() in 'aeiou':
        
        return True
    
    else:
        
        return False
    


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[8]:


#same as above, but this function is calling the vowel function, and if it returns true, 
#this function returns false
def is_consonant(letter):
#using an if/else statement to run the vowel function and determine if its true or false    
    if is_vowel(letter) is True:
        
        return False
    
    else:
    
        return True


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[73]:


#function to capitalize the first letter of a word if the word starts with a consonant
def str_as_word(s):
#creating input to get our word    
    s = input('Enter word here: ')
#slicing the first index of the string and lowercasing to compare to our vowels    
    if s[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        #if letter is a vowel, prints a statement
        print('Word starts with vowel')
#if our letter is not a vowel, it returns the word with the first letter capitalized
    else:
        
        return s.capitalize()
      


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[39]:


#simple function that intakes a total and desired tip percentage to output your total with tip
def calculate_tip():
#getting our total via input    
    before_tip = float(input('Enter your total here ($$.cc): '))
#getting our desired tip percentage    
    tip = float(input('Enter desired tip amount (in decimal format): '))
#caluculating what our tip and total before tip adds up to    
    total = before_tip + (before_tip * tip)
#returning total with tip, rounded so it is comparable to a dollar/cent value    
    return round(total, 2)


# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[42]:


#function to determine a total cost after a discount
def apply_discount():
#input to get our original price as as float    
    original_price = float(input('Enter full price here ($$.cc): '))
#input to get what our discount is as a float    
    discount = float(input('Enter discount (in decimal format): '))
#caluclating end total price by adding the original price to the discount multiplied by the original price    
    price_after_discount = original_price - (original_price * discount)
#returns our end price rounded so it is comparable to a dollar/cent value    
    return round(price_after_discount, 2)



# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[50]:


#function to remove commas in a string
def handle_commas():
#input to get our string    
    num = input('Enter numbers here: ')
#returns our string, replacing all commas with nothing, thus erasing them    
    return num.replace(',', '')


# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[51]:


#function to get a number grade and converting it into a letter grade
def get_letter_grade():
#input to get our number grade    
    num_grade = int(input('Enter whole number grade here (1-100): '))
#starting with the highest values and moving down, using an if/elif/else statement to filter out each grade and
#printing what our letter grade would be
    if num_grade >= 88:
        
        print('A')
        
    elif num_grade >= 80:
        
        print('B')
        
    elif num_grade >= 70:
        
        print('C')
        
    elif num_grade >= 60:
        
        print('D')
        
    else:
        
        print('F')


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[124]:


#function to remove vowels from a string
def remove_vowels():
#input to get our string    
    s = input('Enter word or phrase here: ')
#replace statements to replace all vowels with nothing, which essentially erases them    
    return s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')



# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# 
# For example:
# - Name will become name
# - First Name will become first_name
# - % Completed will become completed

# In[60]:


#Could not get to function as intended, see below

def normalize_name():
    
    s = input('Enter word or phrase here: ')
    
    if s in (['!, @, #, $, %, ^, &, *, (, ), -, =, +, [, ] \, {, }, /, ?']):
        
        replace(['!, @, #, $, %, ^, &, *, (, ), -, =, +, [, ] \, {, }, /, ?'], '')
    
    return s.lower().strip().replace(' ','_')



# In[66]:


#function to standardize a name, by removing capitalizations, trailing and leading white space, 
#replacing spaces in between with underscores, and removing python identifiers
def normalize_name():
#input to get our name    
    s = input('Enter name here: ')
#return statement to lowercase and strip our names of whie spaces, replacing spaces in between with underscores,
#and replacing various non letter characters with nothing
    return s.lower().strip().replace(' ','_').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace("(","").replace(")","")


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[123]:


#function to create a list from an input, convert it to list of integers, and add eat integer together
def cumulative_sum():
#input to get our numbers    
    input_list = input('Enter your numbers separated by a space: ')
    
    #print(input_list)
#converting the input string into a list of strings   
    func_list = input_list.split()
    
    #print(func_list)
#turning the list of strings into a list of integers   
    func_list = list(map(int, func_list))
    
    return sum(func_list)


# In[ ]:




