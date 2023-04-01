# This is used for adding labels with vaderSentiment's sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Import the SentimentIntensityAnalyzer class from the vaderSentiment library

analyzer = SentimentIntensityAnalyzer()  # Create an instance of the SentimentIntensityAnalyzer class

# Open the file containing the text data to be labeled
with open("../data/titles.txt", "r") as f:
    lines = f.readlines()  # Read all lines of the file and store them in the list 'lines'

# Open a new file to write the labeled data
with open("../data/titles_new.txt", "w") as f:
    for line in lines:  # Loop through each line in the list 'lines'
        sentiment = analyzer.polarity_scores(line)  # Use the analyzer to get the sentiment scores for the current line
        if sentiment["compound"] >= 0.05:  # If the compound sentiment score is greater than or equal to 0.05, label as positive
            label = "@positive"
        elif sentiment["compound"] <= -0.05:  # If the compound sentiment score is less than or equal to -0.05, label as negative
            label = "@negative"
        else:  # Otherwise, label as neutral
            label = "@neutral"
        f.write(f"{line.strip()}.{label}\n")  # Write the labeled data to the new file
