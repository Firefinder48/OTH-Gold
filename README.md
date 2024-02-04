# OTH-Gold
OTH (Over the Horizon)-Gold Rev C

This script performs two main tasks:

    Modify line endings: The script reads an input file in binary mode, looks for sequences of two consecutive newline characters, and replaces them with a specified byte sequence (CR, CR, LF). This step ensures that the file has consistent line endings.

    Process based on first character: After modifying the line endings, the script reads the modified file in text mode, categorizing each line based on its first character. The script updates counters for various categories and writes specific information to an output file for some categories. The script prints a summary of the counts for each category.
    
