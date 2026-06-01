#importing random module let computer choose randomly
import random

#creating list list of option
item_list=["rock","paper","scissor"]

#input from user 
user_choice=input("Enter your mave=(rock ,paper,scissor)")

#comuter randomly choice one item from list
comp_choice=random.choice(item_list)

#display user choice and computer choice 
print(f"user choices={user_choice},computer choice={comp_choice}")

#if both user and computer choice same then match will be tie
if user_choice==comp_choice:
    print(" match tie")

# apply logical to print answer
elif user_choice == "rock":
    if comp_choice=="paper":
        print("paper covers rock and paper win")
    else:
        print("rock beats scissor and rock wins")

elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper and scissor wins")
    else:
        print("rock beat scissor and rock wins")

elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissor cuts paper and scissor win")
    else:
        print("rock beats scissor and rock wins")

# if user enter wrong input or away from defined list then output will be invalid input
else:
    print("invalid input")


