#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

pw_length = nr_letters + nr_symbols + nr_numbers
#once we have the password length, we will "generate" random characters by sampling from the list randomly,

#time to add randomly generated values to our list.
letters_list = random.sample(letters, nr_letters)
numbers_list = random.sample(numbers, nr_numbers)
symbols_list = random.sample(symbols, nr_symbols)

#Now that we have all of our character types and their lists, we add them together to one "master list", and shuffle them. That will make a new list that will be our pw
pw_char_list = letters_list + numbers_list + symbols_list
random.shuffle(pw_char_list)

#we want our final pw to be a string, not a list, so let's convert each element in the list to a str using a for loop.
pw_string = [str(char) for char in pw_char_list]

#Now we convert our pw_char_list to a string using the .join method. We don't want anything inbetween our pw characters, so we use an empty string '' before the .join
final_pw = ''.join(pw_string)
print(final_pw)

'''
Logic Recap:
1. import random.
2. Make 3 lists, 1 for each character type (number, symbol, letter)
3. Prompt the user for input.
3. Generate random characters based on the user input. Do this by 
count how many # of letters, symbols or numbers we have left to generate 
generate random character aka select from the list randomly
add all three lists together to make another list. 
suffle the list. 
convert list to a str

random order select from the list (letter, symbol, number)
'''

#my_list = ["dog", 'cat', 'rat']
#print(my_list)


#first idea was to use a while loop to generate characters while we subttract from the total pw_length, but that's all unneccessary if we're just working with lists
#could use a loop to count # of items picked per char type, OR random sample with a parameter (prefered way)
#we will subtract from these after we generate a character
# nr_letters_left = nr_letters
# nr_symbols_left = nr_symbols
# nr_numbers_left = nr_numbers
#password = random.letters
