# Q4
# Write a function that generates a random password. The password should have a random length of
# between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126
# in the ASCII table. Your function will not take any parameters. It will return the randomly generated
# password as its only result. Display the randomly generated password in your file’s main program.


import random

def generate_password():
    password =""
    length = random.randint(7,10)
    for i in range(length):
        char = random.randint(33,126)
        password += chr(char)
    return password

if __name__ == '__main__':
  password = generate_password()
  print("Password:",password)

# OUTPUT:
# Password: BfuJBY2NL
