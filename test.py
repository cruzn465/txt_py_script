import glob

read_files = glob.glob('output/*')
total = len(read_files)

# NEEDS BETTER NAMING CONVENTIONS
each_str = ["CLIENT", "JOB", "TITLE"]

# MAYBE NEEDS TO BE A SET INSTEAD OF A LIST??
comp_str = ["ANNCR", "ANNC", "VO", "ALT", "ED"]

count = 0
# NO_COUNT LIST CO-RELATES TO EACH_STR LIST ["CLIENT", "JOB", "TITLE"]
total_no_count = [0, 0, 0]
total_no_comp = 0

for f in read_files:
    if count < 10:
        # print(count)

        infile = open(f, 'r')
        data = infile.read()

        # LOOP THROUGH each_st
        for i in range(len(each_str)):
            # check for the string CLIENT
            find_result = data.find(each_str[i])
            if find_result == -1:
                total_no_count[i] += 1

        sub_comp_res = 0
        # LOOP THRU COMP_STR TO SEE IF ONE EXISTS
        for j in range(len(comp_str)):
            find_comp_result = data.find(comp_str[i])
            # IF AT LEAST 1 COMP STR EXISTS, ADD TO SUB_COMP_RES
            if find_comp_result != -1:
                sub_comp_res += 1
        # IF SUB_COMP_RES DOESN'T CHANGE, ADD 1 TO THE TOTAL_NO_COMP
        if sub_comp_res == 0:
            total_no_comp += 1
    # count += 1

print("Total number of txt files without CLIENT: ",
      total_no_count[0], "/", total)
print("Total number of txt files without JOB: ", total_no_count[1], "/", total)
print("Total number of txt files without TITLE: ",
      total_no_count[2], "/", total)
print("Total number of txt files without COMP_STR: ", total_no_comp, "/", total)
