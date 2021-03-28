import random
import string

def get_pass(length):
    passchr=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(passchr)for i in range(length))
    print("Your password is:",password)
get_pass(8)