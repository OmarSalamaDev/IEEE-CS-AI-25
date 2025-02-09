'''
    Generate a random password of 8 characters,
    including a mix of uppercase letters, lowercase letters, and numbers.
'''

import random
import string

password = ""

for i in range(8):
    password += random.choice(string.ascii_letters + string.digits)

print(password)