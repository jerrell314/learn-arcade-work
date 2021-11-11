import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def main():
    my_file = open("dictionary.txt")
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)

    my_file.close()
    print("--- Linear Search ---")
    my_book = open("AliceInWonderLand200.txt")
    current_line = 0
    for line in my_book:
        current_line += 1
        word_list = split_line(line)
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1
            if current_list_position == len(dictionary_list):
                print("line:", current_line, "Misspelled word:", word)
    my_book.close()
    print("--- Binary Search ---")
    my_book = open("AliceInWonderLand200.txt")
    current_line = 0
    for line in my_book:
        current_line += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line:", current_line, "Misspelled word:", word)





main()
