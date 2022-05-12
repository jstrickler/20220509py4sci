

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for raw_word in words_in:
        word = raw_word.rstrip()
        if len(word) != 5:
            continue
        first_letter = word[0]

        if first_letter in letter_counts:
            letter_counts[first_letter] = letter_counts[first_letter] + 1
            # letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1


def by_value(element):
    return element[1], element[0]

for letter, count in sorted(letter_counts.items(), key=by_value, reverse=True):
    print(letter, count)

