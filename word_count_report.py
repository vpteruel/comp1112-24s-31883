from collections import Counter
import re

def count_words_in_file(input_file, output_file):
    # Read the content of the file
    with open(input_file, 'r') as file:
        text = file.read()
    
    # Use regex to find words (considering words as sequences of alphanumeric characters)
    words = re.findall(r'\b\w+\b', text.lower())  # Convert text to lowercase for case insensitive counting
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Sort the word counts by frequency in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Write the report to the output file
    with open(output_file, 'w') as file:
        file.write('Word | Frequency\n')
        for word, count in sorted_word_counts:
            file.write(f'{word} | {count}\n')

# Specify the input and output file names
input_file = 'word_count_report_sample.txt'
output_file = 'word_count_report_report.txt'

# Call the function to count words and generate the report
count_words_in_file(input_file, output_file)
