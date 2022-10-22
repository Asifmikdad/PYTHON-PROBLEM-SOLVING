# Clean the data and get a String output 'a e i o u'

from xml.dom.minidom import CharacterData


data = "aNtEriOur\n\t>>"

new_data = data.lower()
output_data = ""


for vowel in new_data:
    if (vowel == "a") or (vowel == "e") or (vowel == "i") or (vowel == "o")or (vowel == "u"):
        output_data += vowel + " "
        
print(output_data)