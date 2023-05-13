# Reading Level Analysis Tool

This is a Python script that calculates the reading level of a text file using three different methods: The Flesch Reading Ease Score, The Power Sumner Kearl Formula, and the Gunning Fog Index. 

## Dependencies

The script requires Python 3 and the `textstat` library to run. You can install the `textstat` library using pip:

```bash
pip install textstat
```

## Usage

To use this script, follow these steps:

1. Prepare your text sample in a file named `text_sample.txt`. Place this file in the same directory as the `reading_level.py` script.

2. Run the script using Python 3:

```bash
python3 reading_level.py
```

The script will read the text from `text_sample.txt` and calculate the reading level according to each of the three methods. It will then print out the results:

- The Flesch Reading Ease Score, along with the corresponding difficulty level and grade level.
- The Power Sumner Kearl grade level and reading age, rounded to the nearest whole number.
- The Gunning Fog Index, rounded to the nearest whole number.

## Note

The readability measures calculated by this script are estimates and should be used as guidelines. They can help identify texts that may be more difficult for certain audiences to read, but they cannot definitively measure how easy a text is to understand. Other factors, such as the content of the text and the reader's prior knowledge, also play a significant role in readability.
