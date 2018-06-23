import os

# Write
# Note: This will overwrite an exisiting file

text = 'This string of text was written\n'

file = open('test_file.txt', 'w')
file.write(text)
file.close()

# Append

text = 'And this string of text was appended.\n'

file = open('test_file.txt', 'a')
file.write(text)
file.close()

# Read

file_read = open('test_file.txt', 'r').read()
print('This is using the .read() function:\n')
print(file_read)

file_readlines = open('test_file.txt', 'r').readlines()
print('This is using the .readlines() function:\n')
print(file_readlines)

# Rename file

old_name = 'test_file.txt'
new_name = 'file_with_new_name.txt'
os.rename(old_name, new_name)