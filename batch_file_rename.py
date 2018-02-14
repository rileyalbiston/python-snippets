
#file_path = "C:/Users/Riley/OneDrive/1_github/python_snipets/test"

import sys, os


def batch_append():

	file_path = str(input("Please enter the full file path: "))
	append_string = str(input("Please enter the name you want to append to begining of the file name: "))

	for root, dirs, files in os.walk(file_path, topdown=False):
	    for name in files:
	        print("Original name:", os.path.join(root, name))

	        new_name = append_string + name
	        os.rename(os.path.join(root, name) , os.path.join(root, new_name))

	        print("New name:", os.path.join(root, new_name))


def batch_rename():

        count = 0

        file_path = str(input("Please enter the full file path: "))
        user_input = str(input("Please enter the new name for the files: "))

        for root, dirs, files in os.walk(file_path, topdown=False):
                for name in files:

                    count += 1
                    extension = os.path.splitext(name)[1]
                    new_name = user_input + "_" + str(count) + extension
                        
                    print("Original name:", os.path.join(root, name))

                    os.rename(os.path.join(root, name) , os.path.join(root, new_name))

                    print("New name:", os.path.join(root, new_name))


def exit_program():
        exit()

menu_options = {
                "append" : batch_append,
                "rename" : batch_rename, 
                "exit"   : exit_program,
        }


while True:
        print("\n")
        print("//  ==============  menu  ==============  //")
        print("Please choose one of the following options:\n1) append\n2) rename\n3) exit")

        
        try: 
                user_input = input(str("Input:\n")).lower()

                menu_options[user_input]()

        # the key error exception is important. Always include.
        except KeyError:
                print("Invalide option. Please try again.")
