# Line Extractor

A Python program that accepts a file, extracts some portion of each line in the file, compares if the extracted portion matches any line in multiple files present in the directory. It writes and appends any line whose extracted portion is does not match any line in the series of files being checked.

## How to use

1. Copy the file that contains the lines of text that you want to extract and check into the same directory as the `checker.py` file.
2. Copy all the files that you are trying to match its content into the same directory with the `extractor.py` file.
3. Run the `extractor.py` file.
4. Enter the name of the file you want to extract its lines and press `ENTER` on the keyboard.
5. Wait for the program to complete and it will generate a file named **`missing_lines.txt`** in the same directory as all the other files.

:rocket: :success:
