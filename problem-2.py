#Encrypt the following code so that no one can get your strategy

# ord is used to find the ascii code for any character
# chr is used for convert anything to character

# data = "firebaby"

data = "firebaby"
shift = 1
output = ""
for character in data:
    output += chr(((ord(character)+shift-97) % 26 + 97))
print(output)
