#2129. Capitalize the Title
def capitalizeTitle(title):
    titles = title.split()
    result = []
    for word in titles:
        if len(word) < 3:
            w = word.lower()                       # short words stay lowercase
        else:
            w = word[0].upper() + word[1:].lower()  # capitalize first letter only

        result.append(w)
    return " ".join(result)
