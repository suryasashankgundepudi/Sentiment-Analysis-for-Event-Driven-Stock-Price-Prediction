# Combining data files

with open('../data/titles_new.txt', 'r') as file1:
    # Read the contents of the file
    file1_contents = file1.read()

# Open the second file in read mode
with open('../data/FinancialPhraseBank-v1.0/Sentences_AllAgree.txt', 'r') as file2:
    # Read the contents of the file
    file2_contents = file2.read()

# Concatenate the contents of the two files
combined_contents = file1_contents + file2_contents
new_contents = combined_contents.replace('titile.@neutral', '')

# Open a new file in write mode to store the combined contents
with open('../data/final_pre_training_data.txt', 'w') as combined_file:
    # Write the combined contents to the new file
    combined_file.write(combined_contents)

