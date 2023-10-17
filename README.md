# Impledge-Search-the-longest-compounded-word
# Impledge Technologies interview coding test 2024
The problem statement can be found in the https://github.com/Hiteker67/Impledge-Search-the-longest-compounded-word/blob/main/Exercise_Fresher_Word_Problem.pdf file
# Code Execution Procedure:
1.	Make sure you have Python 3.7 or a newer version installed on your machine.
2.	Download or clone the repository.
3.	Open Solution.py and locate the code section marked with # Specify the input file path here.
4.	Replace the placeholder with the relative path to the input file with respect to the Solution.py file.
5.	Run the script by executing Solution.py.
# Problem Overview:
•	Compounded words are those formed by combining valid words from the given file.
•	As the input files are already alphabetically sorted and contain one word per line, valid words for compounded words usually appear before the compounded words.
•	Compounded words are a combination of previously read words, acting as prefixes and suffixes.
•	A word cannot be considered a compounded word if it contains characters that are not part of any valid word in the file.
# Approach and Algorithm:
1.	Build a Trie data structure while reading each word from the input file.
2.	Simultaneously, create a deque of <word, suffix> pairs related to valid words in the Trie.
3.	Initialize variables for the longest, second_longest compounded words, and the maximum length.
4.	Continue processing until the deque is empty:
•	a) Check if the suffix of the word contains any valid word (prefix) from the Trie. If the length of the word is greater than the maximum length, update second_longest and longest words.
•	b) If not, generate prefixes from the current suffix of the word and find new suffixes for each prefix length. Add new <word, suffix> pairs to the deque.
5.	Return the longest and second longest compounded words.
This simplified version maintains the essential instructions while making them more concise and easier to follow.

# Answer and Result
Machine Specifications
OS: Windows 11
CPU: Intel Core i5
RAM: 16 GB DDR4

Output 1:- https://github.com/Hiteker67/Impledge-Search-the-longest-compounded-word/blob/main/Output_1.png

Output 2:- https://github.com/Hiteker67/Impledge-Search-the-longest-compounded-word/blob/main/Output_2.png

