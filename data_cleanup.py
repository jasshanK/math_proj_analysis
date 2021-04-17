# Description: Twitter data cleanup
# Author: jasshanK
# Created on: 260321

import csv
import pickle

# open and read csv file
data_clean = {}
with open(r"C:\Users\Jassh\Documents\uni_material\MA1508E\MA1508E_proj_data\data.csv") as fhr:
    ptr_read = csv.reader(fhr)
    for row in ptr_read:
        count = 0
        temp_list = []
        for entry in row:
            if row[9] != "[]":
                if count == 0:
                    temp_list.append(entry.strip(" '\""))
                    # print("{}".format(entry))
                elif count == 9:
                    temp_list.append(entry.strip(" ['\""))
                    # print("{}".format(entry.lstrip("[ ")))
                elif 9 < count < (len(row) + 1):
                    temp_list.append(entry.strip(" '\"]"))
                    # print("{}".format(entry))
                count += 1

        if len(temp_list) > 0:
            # id is key, friends are the value
            data_clean[temp_list[0]] = temp_list[1:]

# save dictionary
try:
    dict_file = open('friend_list.pickle', 'wb')
    pickle.dump(data_clean, dict_file)
    dict_file.close()
except Exception as e:
    print(e)
    print("Could not save dictionary")

# #cleaned up data is written to a text file
# with open(r"C:\Users\Jassh\Documents\uni_material\MA1508E\MA1508E_proj_data\clean_data.csv", 'w', newline='') as fhw:
#     ptr_write = csv.writer(fhw, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     ptr_write.writerows(data_clean)
