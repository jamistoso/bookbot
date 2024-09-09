from collections import Counter

def main():
    book_path = 'books/frankenstein.txt'
    file_contents = get_book_text(book_path)
    num_words = word_count(file_contents)
    char_dict = dict(character_count(file_contents.lower()))
    sorted_char_list = [(char_dict[x], x) for x in char_dict.keys()]
    sorted_char_list.sort(reverse=True)
    print_report(book_path, num_words, sorted_char_list)

def print_report(path, num_words, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in document")
    print()
    for char in char_list:
        if char[1].isalpha():
            print(f"The \'{char[1]}\' character was found {char[0]} times")

def character_count(text):
    cnt = Counter()
    for word in text.split():
        for char in word:
            cnt[char] += 1
    return cnt

def word_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()