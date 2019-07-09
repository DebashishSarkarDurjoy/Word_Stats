def make_stats(filename, new_filename, give_object=False):
    print("Loading....\n")
    record = {}
    with open(filename, encoding="utf-8") as file_object:
        for line in file_object:
            line = clean_string(line).lower()
            line_list = line.split()
            for word in line_list:
                if word not in record:
                    record[word] = 1
                else:
                    record[word] += 1
    if give_object:
        return record

    total_words = count_total_words(record)
    total_unique_words = len(record)

    with open(new_filename, "w") as new_file_object:
        new_file_object.write(f"\tTotal Number of Words: {total_words} \n")
        new_file_object.write(f"\tTotal Number of Unique Words: {total_unique_words} \n")
        new_file_object.write("\n")        

        for word, count in record.items():
            new_file_object.write(f"{word} : {count} \n")
    

def count_total_words(record):
    total = 0
    for values in record.keys():
        total += record[values] 
    return total


def make_alphabet_list():
    alphabets = []
    for i in range(ord("A"), ord("Z") + 1):
        alphabets.append(chr(i))
    for i in range(ord("a"), ord("z") + 1):
        alphabets.append(chr(i))
    return alphabets


def clean_string(string):
    """Take a string and return it removing all alphanumeric characters"""
    contents_arr = [(char) for char in string]
    i = 0
    while not i == (len(contents_arr) - 1):
        if contents_arr[i] not in alphabets:
            contents_arr.pop(i)
        else:
            i += 1   
    contents_string = "".join(contents_arr)
    return contents_string.lower()



alphabets = make_alphabet_list()
alphabets.append(" ")

filename = "WarAndPeace.txt"
new_filename = f"{filename[:-4]}_stats.txt"
make_stats(filename, new_filename)