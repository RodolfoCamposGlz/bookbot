
def open_book (file_path):
 with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def sort_on(dict):
    return dict["count"]

def count_characters(file_path):
        dictionary = {}
        with open(file_path) as f:
            file_contents = f.read()
            file_contents = file_contents.lower()
            for char in file_contents:
                ascii_val = ord(char)
                if ascii_val >= 97 and ascii_val <=122:
                        if char in dictionary:
                            dictionary[char] = dictionary[char] + 1
                        else:
                            dictionary[char] = 1
        list_dictionary = []
        for char in dictionary:
             list_dictionary.append({"letter": char, "count": dictionary[char]})
        list_dictionary.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        for char in list_dictionary:
             print(f"The {char['letter']} character was found {char['count']} times")
        print("--- End report ---")

def main():
    file_path = "books/frankenstein.txt"
    open_book(file_path)
    count_characters(file_path)

main()