def create_melon_report(file):
    # open the file 
    the_file = open("um-deliveries-20140519.txt")
    # read each line in file
    for line in the_file:       
        # remove excess whitespace and split into tokens
        line = line.rstrip()    
        words = line.split('|') 
        # assign the list items to separate variables
        melon, count, amount = words
        # print a line about the delivery using those variables
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    # close the file
    the_file.close()

# day 1 report
print()
print("Day 1")
create_melon_report("um-deliveries-20140519.txt")

# day 2 report 
print()
print("Day 2")
create_melon_report("um-deliveries-20140520.txt")

# day 3 report
print()
print("Day 3")
create_melon_report("um-deliveries-20140521.txt")
