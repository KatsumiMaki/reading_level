import os
import sys
import textstat

def calculate_reading_level_gunning_fog(text_sample):
    # get number of sentences
    num_sentences = textstat.sentence_count(text_sample)
    # get number of words
    num_words = textstat.lexicon_count(text_sample)
    # get number of "big words"
    num_big_words = len([word for word in text_sample.split() if textstat.syllable_count(word) >= 3])
    # calculate average sentence length and percentage of big words
    avg_sentence_length = num_words / num_sentences
    perc_big_words = num_big_words / num_words * 100
    # calculate and return the Gunning Fog index
    gunning_fog_index = (avg_sentence_length + perc_big_words) * 0.4
    return gunning_fog_index

def calculate_reading_level_flesch(text_sample):
    # get number of sentences
    num_sentences = textstat.sentence_count(text_sample)
    # get number of words
    num_words = textstat.lexicon_count(text_sample)
    # get number of syllables
    num_syllables = textstat.syllable_count(text_sample)
    # calculate x and y as per the Flesch Formula
    x = (num_words / num_sentences) * 1.015
    y = (num_syllables / num_words) * 84.6
    # calculate and return the Reading Ease Score
    reading_ease_score = 206.835 - (x + y)
    return reading_ease_score

def calculate_reading_level_psk(text_sample):
    # get number of sentences
    num_sentences = textstat.sentence_count(text_sample)
    # get number of words
    num_words = textstat.lexicon_count(text_sample)
    # get number of syllables
    num_syllables = textstat.syllable_count(text_sample)
    # calculate x and y as per the Power Sumner Kearl Formula
    x = num_words / num_sentences
    y = num_syllables
    # calculate z
    z = (x * 0.0778) + (y * 0.0455)
    # calculate grade level and reading age
    grade_level = z - 2.2029
    reading_age = z + 2.7971
    return grade_level, reading_age

def interpret_reading_ease_score(score):
    if score <= 29:
        return 'Very Difficult', 'Post Graduate'
    elif score <= 49:
        return 'Difficult', 'College'
    elif score <= 59:
        return 'Fairly Difficult', 'High School'
    elif score <= 69:
        return 'Standard', '8th to 9th grade'
    elif score <= 79:
        return 'Fairly Easy', '7th grade'
    elif score <= 89:
        return 'Easy', '5th to 6th grade'
    else:
        return 'Very Easy', '4th to 5th grade'

def main():
    filename = 'text_sample.txt'

    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        sys.exit()

    # Check if file is not empty
    if os.path.getsize(filename) == 0:
        print(f"Error: The file {filename} is empty.")
        sys.exit()

    # Read the file
    with open(filename, 'r') as file:
        text_sample = file.read()

    # Check if text contains any sentences
    if textstat.sentence_count(text_sample) == 0:
        print("Error: The text does not contain any sentences.")
        sys.exit()

    # Check if text contains any words
    if textstat.lexicon_count(text_sample) == 0:
        print("Error: The text does not contain any words.")
        sys.exit()

    # Gunning Fog score
    gunning_fog_index = calculate_reading_level_gunning_fog(text_sample)
    
    print('High School')
    print('Gunning Fog Index: ', round(gunning_fog_index), 'th grade', sep='')
    print()
    
    # Flesch Reading Ease score
    score = calculate_reading_level_flesch(text_sample)
    difficulty, grade_level = interpret_reading_ease_score(score)
    
    print('Middle School')
    print('Flesch Reading Ease Score:', score)
    print('Difficulty:', difficulty)
    print('Flesch Grade Level:', grade_level)
    print()
    
    # Power Sumner Kearl score
    grade_level, reading_age = calculate_reading_level_psk(text_sample)
    
    print('Elementary School')
    print('Power Sumner Kearl Grade Level:', round(grade_level))
    print('Reading Age:', round(reading_age))
   
if __name__ == "__main__":
    main()
