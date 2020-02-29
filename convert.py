
files = "newsequence.txt"
write = "sequence.txt"


# opens the file and reads it line by line
def read_file(file_name):
    # reads file
    f = open(file_name, "r")

    # checks the file mode
    if f.mode == "r":
        # read file line by line
        content = f.readlines()
        # takes content of file and passes it to replace string line by line
        for x in content:
            b = replace_string(x)
            w = open(write, "a")
            w.write("%s\r\n" % b)
            w.close()

    f.close()


# Counts the number of occurrence of each letter on a line
def count_occurrence(test, index, length):
    count = 1
    compare = index + 1
    while count < 4 and compare < length:
        if test[index].upper() == test[compare].upper():
            count += 1
            compare += 1
        else:
            break

    return count


# collects the count of occurrence of each character and returns the code for each occurrence
def count_string(count):
    if count == 1:
        code = '0001'
    elif count == 2:
        code = '0010'
    elif count == 3:
        code = '0011'
    else:
        code = '0100'

    return code


# replaces letter a based on the count
def replace_a(data, count):
    str_a = '00'
    code = str_a + count_string(count)
    if count == 1:
        data = data.replace('A', code)
    elif count == 2:
        data = data.replace('AA', code)
    elif count == 3:
        data = data.replace('AAA', code)
    else:
        data = data.replace('AAAA', code)

    return data


# replaces letter c based on the count
def replace_c(data, count):
    str_c = '01'
    code = str_c + count_string(count)
    if count == 1:
        data = data.replace('C', code)
    elif count == 2:
        data = data.replace('CC', code)
    elif count == 3:
        data = data.replace('CCC', code)
    else:
        data = data.replace('CCCC', code)

    return data


# replaces letter t based on the count
def replace_t(data, count):
    str_t = '10'
    code = str_t + count_string(count)
    if count == 1:
        data = data.replace('T', code)
    elif count == 2:
        data = data.replace('TT', code)
    elif count == 3:
        data = data.replace('TTT', code)
    else:
        data = data.replace('TTTT', code)

    return data


# replaces letter g based on the count
def replace_g(data, count):
    str_g = '11'
    code = str_g + count_string(count)
    if count == 1:
        data = data.replace('G', code)
    elif count == 2:
        data = data.replace('GG', code)
    elif count == 3:
        data = data.replace('GGG', code)
    else:
        data = data.replace('GGGG', code)

    return data


# replaces each letter line by line
def replace_string(s):
    seq = ''
    size = len(s) - 1
    index = 0
    while index < size:
        num = count_occurrence(s, index, size)
        end = index + num
        current = s[index:end]
        if current.count('A') > 0:
            current = replace_a(current, num)
        elif current.count('C') > 0:
            current = replace_c(current, num)
        elif current.count('T') > 0:
            current = replace_t(current, num)
        elif current.count('G') > 0:
            current = replace_g(current, num)
        seq = seq + current
        index += num

    return seq


if __name__ == "__main__":
    read_file(files)















