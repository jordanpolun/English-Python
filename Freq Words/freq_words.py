import time

def main():
    words_file = open('all_words.txt', 'r')
    words = words_file.readlines()
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_freq = "ETAONRISHDLFCMUGYPWBVKJXZQ"

    for word in words:
        new_word = "" # Form new word
        for char in word:
            letter_index = letters.find(char)
            new_char = char

            # Swap out letter if possible
            if letter_index != -1:
                new_char = letters_freq[letter_index]
            new_word += new_char

        # See if this new word is actually a word
        if new_word in words:
            print(word + " -> " + new_word)



if __name__ == "__main__":
    print("Starting up...")
    start = time.time()
    main()
    print("Run time:", round(time.time() - start, 3))
