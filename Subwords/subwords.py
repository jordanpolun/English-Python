import time

def main():
    words_file = open('all_words.txt', 'r')
    words = words_file.readlines()
    words = [word.strip() for word in words]

    valid_words = []
    subwords = []

    for word in words:
        substrings = make_subwords(word)
        valid = False
        if substrings[0] in words:
            subwords.append(substrings[0])
            valid = True
        if substrings[1] in words:
            subwords.append(substrings[1])
            valid = True

        if valid:
            valid_words.append(word)

    sorted_valid_words = sorted(valid_words, key=len, reverse=True)

    print("Dictionary length: " + str(len(words)))
    print("Total subwords found: " + str(len(subwords)))
    print("Total words with subwords found: " + str(len(valid_words)))
    print("Longest ancestor word: " + sorted_valid_words[0])

    long_subword_count = 0
    for word in sorted_valid_words:
        if len(subwords[valid_words.index(word)]) >= 5:
            #print(word[:-1] + "-" + subwords[valid_words.index(word)])
            long_subword_count += 1
        else:
            break

    print("Total long subwords (length >= 5): ", str(long_subword_count))

def make_subwords(word):
    word_1 = ""
    word_2 = ""
    for index in range(0, len(word)):
        if index % 2 == 0:
            word_1 += word[index]
        else:
            word_2 += word[index]

    return (word_1, word_2)

if __name__ == "__main__":
    print("Starting up...")
    start = time.time()
    main()
    print("Run time:", round(time.time() - start, 3))
