import os

output_file = "../data/titles.txt"
output_mode = "w"

# iterate over all files in the directory
for filename in os.listdir("../data/reuters"):
    # check if the file is a TSV file
    if filename.endswith(".tsv"):
        try:
            with open(f"../data/reuters/{filename}", "r",  encoding="utf8") as tsv_file:
                # iterate over each line in the TSV file
                for line in tsv_file:
                    # split the line into its three components
                    ts, title, href = line.strip().split("\t")
                    # write the title to the output file
                    with open(output_file, output_mode) as output:
                        output.write(f"{title}\n")
                    # switch to append mode for subsequent writes
                    output_mode = "a"
        except:
            print('Could not read file\'s line')