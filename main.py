def count_words(s: str) -> int:
    word_count = 0
    words_list = s.split()

    for word in words_list:
        word_count += 1
    
    return word_count


def count_characters(s: str) -> dict:
    characters = {}

    for c in s:
        if not c.isalpha():
            continue
        
        c = c.lower()

        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    
    return characters


def print_report(book_path: str) -> None:
    with open(book_path) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)

    character_count = count_characters(file_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for k in character_count:
        print(f"The '{k}' character was found {character_count[k]} times")
    
    print("--- End report ---")


def main() -> None:
    print_report("books/frankenstein.txt")    


main()