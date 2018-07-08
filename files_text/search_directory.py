import os, sys
from os.path import isfile, join


path = 'C:\\Users\\Riley\\Desktop\\geocities\\'

def main():
	files = os.listdir(path)
	print(files)

	# Search just for .gif files
	matching = [s for s in files if ".gif" in s]
	print(matching)


	for file in os.listdir(path):
	    if file.endswith(".gif"):
	        print(os.path.join(path, file))
	        print(file)

	#for root, dirs, files in os.walk(path):
	#	print(root)



if __name__ == "__main__":
    # execute only if run as a script
    main()