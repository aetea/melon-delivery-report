# create first day report

print("Day 1")
the_file = open("um-deliveries-20140519.txt")
for line in the_file:       # read each line in the file
    line = line.rstrip()    # remove excess whitespace at the end of the line
    words = line.split('|') # break the line at pipes and create a "words" list

    melon = words[0]        # first item in words
    count = words[1]        # first item in words >> should be second
    amount = words[2]       # first item in words >> should be third

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


# second day report -- identical to first day except for file name

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


# third day report -- identical to first day except for file name

print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
