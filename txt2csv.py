import glob
import csv
from tkinter.ttk import Separator

read_files = glob.glob('output/*')
arr = []

with open("HD_SpringRadio.csv", mode="w", encoding="utf-8") as outfile:

    w = csv.writer(outfile)
    count = 0
    for f in read_files:
        if count < 1:
            infile = open(f, 'r')
            data = infile.read()

            # FXN that takes the data from each file and adds it to the global array
            def addToArr():
                dict = {}
                seps = ["CLIENT:", "JOB:", "TITLE:", "JOB#",
                        "SLATE #:", "DATE:", "ANNCR:", "LEGAL:"]
                seps_i = 0
                string = str(data)

                while seps_i < len(seps)-1:
                    # separate the line and add it to dict
                    line = string.split(seps[seps_i+1])[0]
                    val_arr = line.split(seps[seps_i])
                    dict[seps[seps_i]] = val_arr[1]

                    temp_str = string.split(line)[1]
                    string = temp_str

                    # print(val_arr[1])
                    # print("*******")
                    seps_i += 1

                # LEGAL
                # print(string)
                val_arr = string.split("LEGAL:")
                dict[seps[seps_i]] = val_arr[1]
                # print(dict)

                print(dict["ANNCR:"])
                # client_val = client.split("CLIENT:")
                # dict["CLIENT:"] = client_val[1]

                # separate "CLIENT: THE HOME DEPOT" and add it to dict
                # client = string.split("JOB:")[0]
                # client_val = client.split("CLIENT:")
                # dict["CLIENT:"] = client_val[1]

                # remove the first sep
                # temp_str = string.split(client)[1]
                # string = temp_str

                # REPEAT FOR "JOB:    :30 L&G Divisional Radio"
                # job = string.split("TITLE:")[0]
                # job_val = job.split("JOB:")
                # dict["JOB:"] = job_val[1]

                # temp_str = string.split(job)[1]
                # string = temp_str

                # print(job)
                # print(job_val)
                # print(dict)
                # print(string)

            # invoke addToArr fxn
            addToArr()

            infile.close()
        count += 1

    # with open(f, "r") as infile:
    #     if count < 1:
    #         # print(count)
    #         print("infile")
    #         print(infile)

    # w.writerow([line for line in infile])
