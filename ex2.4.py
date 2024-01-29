import timeit

def count_vowels(word):
    vowels = "aeiouy"
    return sum(1 for char in word.lower() if char in vowels)

def average_vowels_per_word(file_name, start_at='CHAPTER 1. Loomings.'):
    total_words = 0
    total_vowels = 0


    with open(file_name, 'r') as text:

        for line in text: 
                if start_at in line:
                    words = line.split()
                    total_words += len(words)
                    total_vowels += sum(count_vowels(word) for word in words)
                    break  

    if total_words > 0:
            average_vowels = total_vowels / total_words
            return average_vowels
    else:
            return 0



if __name__ == "__main__":
    file_name = 'pg2701.txt'

    average_vowels = average_vowels_per_word(file_name)

    if average_vowels is not None:
        print(f"The average number of vowels per word in the text file is: {average_vowels}")