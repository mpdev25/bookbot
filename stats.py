def words(file_contents):
    all_words = len(file_contents.split())
    return all_words

def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def sorted_letters(letter_counts):
    result = []
    for char, count in letter_counts.items():
        result.append({"char": char, "num": count})
        def sort_on(dict):
            return dict["num"]
    result.sort(reverse=True, key=sort_on)
    return result

    
   