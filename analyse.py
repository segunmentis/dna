files = "newsequence.txt"
write = "compress.txt"
reverse = "reversed.txt"
seq = dict()
global key_max


#Stores the sequence in a dictionary
def store_seq(key, value):
    if key not in seq:
        seq.update({key:value})


#breaks each line down into sequences and counts the number of occurence of each sequence
def check_exists(data):
    data = data.strip()
    size = len(data)
    start = 0
    endpoint = size - 7
    dna = open(files, "r")
    info = dna.read()
    while start < endpoint:
        end = start+8
        curr = data[start:end]
        count = info.count(curr)
        store_seq(curr, count)
        start = start+1
    dna.close()


#reads the dna data from the file line by line
def read_file(file_name):
    f = open(file_name, "r")
    for content in f:
        check_exists(content)
    f.close()


#prints out the sequence with the maximum occurence
def show_max_val():
    global key_max
    key_max = max(seq.keys(), key=(lambda k: seq[k]))
    print("The sequence "+key_max+" has the highest occurence of ", seq[key_max])


#Reads the dna file and replaces the sequence with the highest occurence with a define letter
def compress_file():
    w = open(write, "a")
    dna = open(files, "r")
    info = dna.read()
    if info.find(key_max) != -1:
        info = info.replace(key_max, 'P')
    w.write("%s\r\n" % info)
    w.close()
    dna.close()


#Reverses the file from the function above
def reverse_data():
    global key_max
    f = open(write, "r")
    data = f.read()
    data = data.replace('P', key_max)
    w = open(reverse, "a")
    w.write("%s\r\n" % data)
    w.close()
    f.close()


if __name__ == "__main__":
    read_file(files)
    show_max_val()
    compress_file()
    reverse_data()


    