def count_words(book):
    return len(book.split())

def count_characters(book):
    letters = {}
    for letter in book:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def sort_characters(letters):
    result = []
    for l in letters:
        result.append({"char": l, "num": letters[l]})
    result.sort(reverse=True, key=sort_on)
    return result