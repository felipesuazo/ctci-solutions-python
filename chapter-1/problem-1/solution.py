def is_unique(word: str) -> bool:
    word = word.lower()
    return len(set(word)) == len(word)
