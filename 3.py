
with open('about.txt', 'r') as f:
    words = f.read().split()
    long_words = [word for word in words if len(word) >= 6]
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    most_frequent_word = max(word_frequency, key=word_frequency.get)
    print("The words with atleast 6 letters are: ", long_words)
    print('The most frequent word is: ', most_frequent_word)
