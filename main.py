def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(f"See all chars: \n{num_chars}")


def get_num_words(text) -> int:
    words = text.split()
    return len(words)


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def get_num_characters(text) -> dict:
    num_characters_dict = {}
    for char in text.lower():
        if char not in num_characters_dict:
            num_characters_dict[char] = 0
        num_characters_dict[char] += 1
    return num_characters_dict


if __name__ == '__main__':
    main()
