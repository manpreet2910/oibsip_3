import random
import string

def password_generator(length,numbers=True,special_character=True) :
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation 

    characters=letters
    if numbers:
        characters+=digits
    if special_character:
        characters+=special

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd)<length:
        new_char=random.choice(characters)  
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        
        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if special_character:
            meets_criteria=meets_criteria and has_special

    return pwd
print("Welcome to Manpreet's Random Password Generator !")
length=int(input("Enter the minimum length of the password "))
number_choice=input("Do you want numbers in the password? (y/n)").lower()=="y"
special_choice=input("Do you want special characters in the password? (y/n)").lower()=="y"

pwd=password_generator(length,number_choice,special_choice)
print("The password generated for you is: ", pwd)