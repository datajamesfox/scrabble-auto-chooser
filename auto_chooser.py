# -- Dev Notes --
# Add correct documentation 
# Bring in full word list
# Make letter_score a module
# Optimisation

letter_score = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}

# Horizontal scoring

word = 'PLATE'
hand = 'SFAEFLD'

score = 0
for letter in word:
    score += letter_score[letter]

# print(score)

# with open('words.txt', mode='r') as file:   
#     word_list = file.read().splitlines()[6:]

# print(word_list[0:2])

word = 'PLATE'

word_list = ['PLATES', 'TEMPLATE', 'PLATED', 'UNPLATED', 'TEST', 'NOT', 'THIS', 'PLATITUDE']

potential_words = {}

for words in word_list:
    if word in words:
        temp_score = 0
        for letter in words:
            temp_score += letter_score[letter]
        potential_words[words] = temp_score


required_letters = {key: (key.replace(word, '')) for key, value in potential_words.items()}

scoring_letters = dict((required_letters[key], value) for (key, value) in potential_words.items())


# sorted_dict = sorted(potential_words.items(), key=lambda x: x[1])
# print(sorted_dict[0])

choose_letters = {}

for i in scoring_letters:
    if set(i).issubset(set(hand)) == True:
        choose_letters[i] = scoring_letters[i]

print(choose_letters)

# Vertical Scoring