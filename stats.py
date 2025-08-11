
def get_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def count_characters(text):
    characters = {}
    for char in text:
        if char.lower() in characters.keys():
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1

    return characters

def sort_on(items):
    return items["count"]

def sorted_list(characters):
    new_chars = []
    for k, v in characters.items():
        new_chars.append({"char": k, "count": v})

    new_chars.sort(reverse=True, key=sort_on)

    return new_chars
    
