def highest_frequency_char(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    sorted_string = sorted(char_frequency.items(),
                           key=lambda keyvalue: keyvalue[1], reverse=True)
    print('Frequencies of all characters:', '\n', sorted_string)

    character = []  # defining empty list
    for t in sorted_string:  # iterating over the sorted string to get each tuple
        # the first index[0] of each tuple i.e the characters is added in the list :character
        character.append(t[0])

    return character[0]


highest_frequency = highest_frequency_char(
    'Program to find most repeated character')
print('Most repeated character in the text is : ',
      '\n', '|', highest_frequency, '|')  # vertical bar is used in case space came out to be the character with highest frequency
