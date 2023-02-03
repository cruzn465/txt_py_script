import jsonlines
import glob
import csv
import json
from pickle import DICT
from tkinter.ttk import Separator


# note YHTB-D28R-5056.txt " CLIENT:	THE HOME DEPOT"
read_files = glob.glob('output/*')
# MADE A FOLDER TO TEST OUTLIERS
# read_files = glob.glob('outliers/*')

arr = []
# NEEDS BETTER NAMING CONVENTIONS
# each_str = ["CLIENT", "JOB", "TITLE"]
each_str = ["TITLE"]

comp_str = ["ANNCR", "ANNC", "VO", "ALT", "ED"]

# with open("HD_SpringRadio.csv", mode="w", encoding="utf-8") as outfile:

# w = csv.writer(outfile)
count = 0
for f in read_files:
    if count < 400:
        # print("*********COUNT: ", count)
        infile = open(f, 'r')
        # print(infile)
        data = infile.read()

        # A list of each "line" and use this for step 2 of parsing the string
        lines = data.splitlines(False)
        # FILTERS OUT "" AND " "
        filt_list1 = list(filter(lambda str: str != "", lines))
        filt_list = list(filter(lambda str: str != " ", filt_list1))

        # print("FILT_LIST", filt_list)

        # FXN that takes the data from each file and adds it to the global array
        def addToArr():
            dict = {}

            # LOOP THRU EACH_STR AND FOR EACH, LOOP THRU FILT_LINES AND FIND THE ONE THAT STARTS WITH EACH_STR[i]
            for i in range(len(each_str)):
                for j in range(len(filt_list)):
                    if filt_list[j].find(each_str[i]) != -1:
                        val = filt_list[j].split(each_str[i])[1]
                        # print(val)
                        dict["prompt"] = ""
                        # dict["prompt"] = val.replace(":", "").replace("\t", "")+"\n\n###\n\n"
                        break

            # COUNT IS THE AMOUNT OF TIMES A COMP_STR APPEARS
            comp_count = 0
            curr_comp = ""
            while len(filt_list) > 0 and comp_count < 1:
                # FOR EACH FILT_LINE, LOOP THROUGH COMP_STR
                for i in range(len(comp_str)):
                    # IF THERE IS A COMP_STR, ADD TO COUNT TO BREAK OUT OF OUTER LOOP
                    if filt_list[0].find(comp_str[i]) != -1:
                        # print(filt_list[0])
                        curr_comp = comp_str[i]
                        comp_count += 1
                        break
                # POP THE LINE IF THERE ARE NO COMP_STR PRESENT
                if comp_count == 0:
                    filt_list.pop(0)

            # print("after while loop", filt_list)

            # DELETE LEGAL
            idx_legal = 0
            if len(filt_list) != 0:
                # INSTEAD OF JUST CHECKING THE LAST INDEX, LOOP THROUGH THE FILT_LIST AND FIND "LEGAL", SAVE THE IDX AND DELETE IT AFTER THE LOOP IS OVER
                for k in range(len(filt_list)):
                    if filt_list[k].find("LEGAL") != -1:
                        idx_legal = k
                        break
                if idx_legal != 0:
                    filt_list.pop(idx_legal)

                # JOIN THE FILT_LIST, SEPARATE THE CURR_COMP AND ADD TO DICT UNDER COMPLETION
                joined_str = " ".join(filt_list)
                # print(joined_str)
                val_str = joined_str.split(curr_comp)[1]

                if val_str.find(":") != -1:
                    val_str = val_str.replace(":", "")
                if val_str.find("\t") != -1:
                    val_str = val_str.replace("\t", "")

                # ADD TO DICT:
                dict["completion"] = " " + val_str + "END"
            # print(val_str)
            if len(dict) == 2:
                arr.append(dict)
            # print(arr)

        addToArr()

        infile.close()
    count += 1

# At the end of looping thru read_files, dump into output.json
# with open("output.json", "w") as outfile:
#     json.dump(arr, outfile)

# write to file
with jsonlines.open('sample2_op2.jsonl', 'w') as outfile:
    outfile.write_all(arr)
# read the file
# with jsonlines.open('sample2_op2.jsonl') as reader:
#     for obj in reader:
#         print(obj)

# with open(f, "r") as infile:
# #     if count < 1:
# #         # print(count)
# #         print("infile")
# #         print(infile)

#     w.writerow([line for line in infile])

# ********OLD CODE******
    # seps = ["CLIENT:", "JOB:", "TITLE:", "JOB#",
    #         "SLATE #:", "DATE:", "ANNCR:", "LEGAL:"]
    # seps_i = 0
    # string = str(data)

    # # Separates lines and removes from string
    # while seps_i < len(seps)-1:

    #     # line: everything before 2nd separator i.e. 1st loop is "JOB:"
    #     # 1st line: "CLIENT:\tTHE HOME DEPOT\n"

    #     # 1st val_arr: ['', '\tTHE HOME DEPOT\n']
    #     line = string.split(seps[seps_i+1])[0]
    #     val_arr = line.split(seps[seps_i])

    #     dict[seps[seps_i]] = val_arr[1]

    #     temp_str = string.split(line)[1]
    #     string = temp_str

    #     seps_i += 1

    # # LEGAL
    # val_arr = string.split("LEGAL:")
    # dict[seps[seps_i]] = val_arr[1]
