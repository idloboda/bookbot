def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    report(book_path, num_words, num_chars)
    # print(f"{num_words} words found in the document")
    # print(f"See all chars: \n{num_chars}")


def get_num_words(text) -> int:
    words = text.split()
    return len(words)


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def get_num_characters(text) -> dict:
    num_characters_dict = {}
    for char in text.lower().strip():
        if char.isalpha():
            if char not in num_characters_dict:
                num_characters_dict[char] = 0
            num_characters_dict[char] += 1
    return num_characters_dict

def sort_on(dict):
    return dict["num"]

def report(book_path: str, num_words: int, num_chars:dict) -> None:
    # num_chars.sorted(reversed = True, key=lambda item: item[1])
    # sort_on(num_chars)
    num_chars = dict(sorted(num_chars.items(), key=lambda item: item[1], reverse= True))       
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for key in num_chars:
        print(f"The '{key}' character was found {num_chars[key]} times")
    print("--- End report ---")
    

if __name__ == '__main__':
    main()
