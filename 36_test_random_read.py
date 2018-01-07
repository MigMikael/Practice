import random


def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2):
            continue
        line = aline
    return line


data_file = open("C:\\Users\\Mig\\Desktop\\test_data.txt", "r")
for i in range(20):
    line = random_line(data_file)
    print(line)
