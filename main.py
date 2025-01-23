def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    seen_dict = get_char_count(text)
    
    print_report(book_path, seen_dict, num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text:str) -> dict[str,int]:
    seen = {}
    
    for c in text:
        c = c.lower().strip()
        if not c:
            continue
        seen[c] = seen.get(c,0) + 1

    return seen

def print_report(book_path:str, seen_dict:dict[str,int], word_count:int) -> None:
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document')

    for c in seen_dict.keys():
        if  c == " " or c == "." or c == "#":
            continue
        print(f"The '{c}' character was found {seen_dict[c]} times")

    print("--- End report ---")
    
    
main()