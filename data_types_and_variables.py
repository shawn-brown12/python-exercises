#Write some Python code, that is, variables and operators, to describe the following scenarios. 
#Do not worry about the real operations to get the values, the goal of these exercises is to 
#understand how real world conditions can be represented with code:

#You have rented some movies for your kids: The little mermaid (for 3 days),
#Brother Bear (for 5 days, they love it), and 
#Hercules (1 day, you don't know yet if they're going to like it). 
#If price for a movie per day is 3 dollars, how much will you have to pay?

movie1 = dict(title = 'The Little Mermaid', duration = 3)
movie2 = dict(title = 'Brother Bear', duration = 5)
movie3 = dict(title = 'Hercules', duration = 1)

days = movie1['duration'] + movie2['duration'] + movie3['duration']

per_day = 3

days * per_day

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
#Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350

weekly_pay = google * 6 + amazon * 4 + facebook * 10

print(weekly_pay)

#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_not_full = True
schedule_conflict = False

student_enrolled = True if class_not_full == True and schedule_conflict == False else False

print(student_enrolled)

#Class example
class_is_not_full = True
schedule_does_not_conflict = True
enroll = class_is_not_full and schedule_does_not_conflict
print(enroll)

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
#Premium members do not need to buy a specific amount of products.

premium_member = True
offer_expired = True
items_bought = 1
bought_enough = True if items_bought > 2 else False

gets_offer = True if items_bought > 2 and offer_expired == False or premium_member == True else False

print(gets_offer)

#Class example

purchase_more_than_two = True
product_not_expired = True
premium_member = False
discount_eli = product_not_expired and (purchase_more_than_two or premium_member)
print(discount_eli)

#Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters

at_least_five = len(password) >= 5

len(password)

print(at_least_five)

#the username must be no more than 20 characters

no_more_than_twenty = len(username) <= 20
print(no_more_than_twenty)

#the password must not be the same as the username

password_is_not_username = False if password == username else True
print(password_is_not_username)

#bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

no_spaces_pass = True if password.strip() == password else False
print(no_spaces_pass)
no_spaces_user = True if username.strip() == username else False
print(no_spaces_user)
both_correct = no_spaces_pass and no_spaces_user == True
print(both_correct)

#Class Example

no_whitespace_username = not(username.startswith(' ') or username [-1] == ' ')
no_whitespace_password = not(password.startswith(' ') or password [-1] == ' ')
user_and_password_valid = no_whitespace_username or no_whitespace_password
print(user_and_password_valid)

