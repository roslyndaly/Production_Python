# Command Line Arguments: Exercises

## Exercise: Word Counter Script

Write a Python script `word_counter.py` that counts the number of words in a given text file.

### Requirements

- The script should accept a filename as a command-line argument.
- It should read the content of the specified file.
- Count the number of words in the file.
- Print the total count of words to the console.

### Example

Suppose you have a text file named `sample.txt` with the following content:

``` text
This is a sample text file.
It contains some words to count.
```

Running the following from the command line:

``` text
python word_counter.py sample.txt
```

Will have the output:

``` text
Total words in 'sample.txt': 12
```

## Additional Challenges (Optional)

- Modify the script to accept multiple filenames as command-line arguments and count the total number of words in all files combined.
- Implement error handling for invalid file paths or unreadable files. (`FileNotFoundError`, `UnicodeDecodeError` and `IOError` are the possible errors which would be raised in these scenarios.)
