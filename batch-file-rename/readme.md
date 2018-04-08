# Batch File Rename

This program lets you rename all the files in a directory.

It operates in a terminal window.

Using the text menu you must first choose to append to the exisiting filename or create a new name for each file.

You will then be promted to enter the path to the directory containing the files you would like to rename.

If appending to the exisiting name that text entered will be added to the begining of the filename.

If giving files a new name a counter will be added to the end of each file to make the names unique e.g. filename_1, filename_2, filename_3 etc

## To run the program: 

```>``` ```cd \path\to\directory\python-snippets\batch-file-rename>```

```python-snippets\batch-file-rename>``` ```python batch_file_rename.py```

## Example:

```
//  ==============  menu  ==============  //
Please choose one of the following options:
1) append
2) rename
3) exit
Input:
append
Please enter the full file path: D:\python-snippets\batch-file-rename\test
Please enter the name you want to append to begining of the file name: aaa_
Original name: D:\python-snippets\batch-file-rename\test\2018_file_1.txt
New name: D:\python-snippets\batch-file-rename\test\aaa_2018_file_1.txt
Original name: D:\python-snippets\batch-file-rename\test\2018_file_2.txt
New name: D:\python-snippets\batch-file-rename\test\aaa_2018_file_2.txt
Original name: D:\python-snippets\batch-file-rename\test\2018_file_3.md
New name: D:\python-snippets\batch-file-rename\test\aaa_2018_file_3.md


//  ==============  menu  ==============  //
Please choose one of the following options:
1) append
2) rename
3) exit
Input:
exit
```
