def create_melon_report(day_num, file):
    print()
    print("Day", day_num)

    # open the file 
    the_file = open(file)
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


create_melon_report(day_num = 1, file = "um-deliveries-20140519.txt")
create_melon_report(day_num = 2, file = "um-deliveries-20140520.txt")
create_melon_report(day_num = 3, file = "um-deliveries-20140521.txt")
