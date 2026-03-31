# \# P1: Data Detective

# 

# \## Summary

# This project analyzes a text file, counts word frequencies, shows the top N words, and reports an extra insight.

# 

# \## Dataset

# File: sample.txt  

# Why I chose it: It is simple and useful for testing word frequency logic.

# 

# \## How to run

# python -m src.project

# 

# \## How to test

# pytest -q

# 

# \## Approach

# \- Load text from a file  

# \- Normalize the text (lowercase, remove punctuation)  

# \- Split into words  

# \- Count word frequencies using dictionary  

# \- Sort and display top N words  

# 

# \## Complexity

# 

# \### count\_words

# Time: O(n)  

# Space: O(n)  

# Why: We go through each word once  

# 

# \### top\_n\_words

# Time: O(n log n)  

# Space: O(n)  

# Why: Sorting is required  

# 

# \## Edge-case checklist

# \- empty file  

# \- punctuation-heavy input  

# \- repeated words  

# \- uppercase/lowercase differences  

# \- n <= 0  

# 

# \## Design note (150–250 words)

# In this project, I used a simple text file as a dataset to analyze word frequencies. I designed the program to first normalize the text by converting all words to lowercase and removing punctuation, which helps ensure accurate counting. Then, I split the text into words and used a dictionary to count how many times each word appears.

# 

# The most straightforward part was counting word frequencies using a dictionary. The challenging part was handling edge cases like punctuation and ensuring the program works for empty input or invalid values of N. I also had to think about efficiency when sorting the words to find the top N most frequent ones.

# 

# If I had more time, I would improve the program by allowing users to input their own files and adding better visualization of results, such as charts or graphs.

