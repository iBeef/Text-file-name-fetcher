#! python3

'''Text_file_name_fetcher.py - Fetches the filenames of text files that need
importing into a results spreadsheet and copies them to the clipboard.'''

# Created by iBeef - 06/04/18 - ibeef1990@gmail.com

import os
import pyperclip

def text_file_name_fetcher():

    text_files = []

    # Iterate through each file in the scripts current working directory.
    for filename in os.listdir(os.getcwd()):

        # Check to see if the file extension is 'txt'
        if filename.split('.')[1] == 'txt':
            text_files.append(filename)
        else:
            pass

    # Copy the '.txt' files to the clipboard.
    pyperclip.copy('\r\n'.join(text_files))
    
text_file_name_fetcher()
