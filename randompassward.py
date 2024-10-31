import secrets
import string
chars = string.ascii_letters
nos = string.digits
specialchars = string.punctuation
alphabet = chars + nos + specialchars 
pwd_length = 8
while True:
  pwd = ' '
  for i in range(pwd_length):
    pwd += ' '.join(secrets.choice(alphabet))
  if (any(char in specialchars for char in pwd) and 
      sum(char in nos for char in pwd)>=2):
          break
print(pwd)