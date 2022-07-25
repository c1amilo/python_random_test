import pyfiglet
str2convert = input("Enter the string to convert: ")
font = pyfiglet.figlet_format(str2convert)
print(font)