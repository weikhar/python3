# CREDIT: https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1_Basics.html

# wc - word count
# ~~~~~~~~~~~~~~~
# Similar to UNIX's wc utility - Read a file given in the command-line argument and print the number of
# lines, words and characters.
# Usage: ./wc.py <filename>
    # The above is the module's doc-string for documentation
    # Multi-line strings are delimited by triple single/double quotes

# To run the script:
# $ python wc.py <filename>  # Invoke Python Interpreter to run the script
# # OR
# $ chmod u+x wc.py      # Set the script executable
# $ ./wc.py <filename>   # Execute the script

# Check if a filename is given in command-line arguments
import sys              # Using 'sys.argv' and 'sys.exit()'
if len(sys.argv) != 2:  # Command-line arguments are kept in a list 'sys.argv'
    print('Usage: ./wc.py <filename>')
    sys.exit(1)         # Return a non-zero value to indicate abnormal termination
    # Note: Python uses indentation instead of {} for body block
 
# Python's variable has no type. No prior declaration needed.
# Variables are created via the initial assignments.
num_words = num_lines = num_chars = 0  # chain assignment
 
# Get input file name from 'sys.argv'
# sys.argv[0] is the script name, sys.argv[1] is the filename.
with open(sys.argv[1]) as infile: # 'with-as' closes the file automatically
    for line in infile:           # Process each line (including newline) in a for-loop
        num_lines += 1            # No ++ operator in Python?!
        num_chars += len(line)
        line = line.strip()       # Remove leading and trailing whitespaces
        words = line.split()      # Split into a list using whitespace as delimiter
        num_words += len(words)
 
# Print results
print('Number of Lines is %d' % num_lines)  # C-like printf()
print('Number of Words is %d' % num_words)
print('Number of Characters is %d' % num_chars)