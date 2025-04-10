#A useful fact about ASCII is that all the lowercase letters are in the range 97-122, 
# and appear sequentially from 'a' to 'z'. To find if is_lowercase(c), we can chec if 
#c is in that range 

def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

#Uppercase letters are in the range 65-90, and appear sequentially from 'A' to 'Z'.
def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')
#To find if is_digit(c), we can check if c is in the range 48-57, which are the ASCII
#values for the digits '0' to '9'.
def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')
#To find if is_alphanumeric(c), we can check if c is in the range 48-57 (digits) or
#65-90 (uppercase letters) or 97-122 (lowercase letters).
def is_alphanumeric(c):
    return (ord(c) >= ord('0') and ord(c) <= ord('9')) or \
           (ord(c) >= ord('A') and ord(c) <= ord('Z')) or \
           (ord(c) >= ord('a') and ord(c) <= ord('z'))

def is_alphabetic(c):
    return is_lowercase(c) or is_uppercase(c) or is_digit(c)

def to_uppercase(c):
    if not is_lowercase(c):
        return c
    return chr(ord(c) - ord('a') + ord('A'))
#if c is a lowercase letter, we can convert it to uppercase by subtracting the ASCII value of 'a'
#to obtain a number between 0 and 25 representing the position of c in the alphabet. Then, if
#we add the ASCII code of 'A', we get the ASCII value of the corresponding uppercase letter