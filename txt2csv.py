import glob
import csv
import json
from pickle import DICT
from tkinter.ttk import Separator


# note YHTB-D28R-5056.txt " CLIENT:	THE HOME DEPOT"
read_files = glob.glob('output/*')
arr = []

# with open("HD_SpringRadio.csv", mode="w", encoding="utf-8") as outfile:

#w = csv.writer(outfile)
count = 0
for f in read_files:
    if count < 1:

        infile = open(f, 'r')
        data = infile.read()

        # A list of each "line" and use this for step 2 of parsing the string
        lines = data.splitlines(False)

        # print(lines)

        # FXN that takes the data from each file and adds it to the global array
        def addToArr():
            dict = {}

            # i.e.['', '\tTHE HOME DEPOT']
            # Make reusable code and find the line in the list that starts with "CLIENT"
            clientVal = lines[0].split("CLIENT:")[1]
            dict["Client"] = clientVal

            jobVal = lines[1].split("JOB:")[1]
            dict["Job"] = jobVal

            titleVal = lines[2].split("TITLE:")[1]
            dict["Title"] = titleVal
            # print(dict)

            arr.append(dict)
            print(arr)

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
        addToArr()

        # with open("output.json", "w") as outfile:
        #     json.dump(arr, outfile)

        infile.close()
    count += 1

# At the end of looping thru read_files, dump into output.json
with open("output.json", "w") as outfile:
    json.dump(arr, outfile)

# with open(f, "r") as infile:
# #     if count < 1:
# #         # print(count)
# #         print("infile")
# #         print(infile)

#     w.writerow([line for line in infile])
