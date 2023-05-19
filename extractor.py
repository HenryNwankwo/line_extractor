import os

# Prompt the user to enter the name of the original file
original_filename = input("Enter the name of the original file (including the file extension): ")

# Open the original file for reading
with open(original_filename, 'r') as original_file:

    # Read all lines of the original file and store them in a list
    original_lines = original_file.readlines()

    # Loop over each line in the original file
    for line in original_lines:

        # Extract the portions of the line
        first_part = line[:16]
        second_part = line[46:58]
        third_part = line[135:138]

        if third_part[-1] == ")":
            third_part = third_part[:-1]

        else:
            third_part = line[135:138]

        # Initialize a variable to keep track of whether the portions were found in any of the other files
        portions_found = False

        # Loop over each file in the directory
        for filename in os.listdir():

            # Check if the file is a text file, is not the original file, and doesn't end with "new.txt"
            if filename.endswith(".txt") and filename != original_filename and not filename.endswith("new.txt"):

                # Open the file for reading
                with open(filename, 'r') as other_file:

                    # Read all lines of the file and store them in a list
                    other_lines = other_file.readlines()

                    # Loop over each line in the file
                    for other_line in other_lines:

                        # Check if all three portions are present in the line
                        if first_part in other_line and second_part in other_line and third_part in other_line:

                            # If the portions are found, set the flag to True and break out of the loop
                            portions_found = True
                            break

                # If the portions are found, break out of the loop over files
                if portions_found:
                    break

        # If the portions are not found in any of the other files, write them to a new file and also write the original line to another file
        if not portions_found:
            with open('missing_portions.txt', 'a') as missing_portions_file:
                missing_portions_file.write(line)
            with open('missing_lines.txt', 'a') as missing_lines_file:
                missing_lines_file.write(line)


# Print "Completed successfully" to the console
print("Completed successfully")