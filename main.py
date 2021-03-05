# create an anagram
# read the data
# create a collection

from collections import defaultdict


def map_of_word(filename):
    words_dict = defaultdict(list)
    for item in filename:
        word = sorted(item.lower().strip())
        word = "".join(word)
        words_dict[word].append(item.strip())

    return words_dict


def words_from_user_file(filepath):
    with open(filepath) as input_file:
        entity = input_file.readlines()
        result = map_of_word(entity)
    return result


# print(map_of_word(["restful", "fluster", "Easter", "teaser", "trace", "caret"]))
print(words_from_user_file("/usr/share/dict/words"))
