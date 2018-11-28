import csv
#data = {}
#with open("config.json", "a") as f:
    #data_file = json.load(f)
    #data = '{"tota": "good girl", "adam": "good guy"}'
    #data["myname"] = "asaad"
    #data_string = json.loads(data)
    #data_dumps = json.dumps(data_string, indent=4, sort_keys=True, separators=(",", ":"))
    # it is used to dump Dic into file
    #json.dump(data, f, indent=4, separators=(",", ":"))
    #print(data_file)
    #print (data_string)
    #print(data_dumps)
    #print(type(data_dumps))
    #print (type(data_string))
    #print (type(data_dumps))


    #print type(data)
    #print (data["pid1"]["property3"])
    #print json.dumps(data, indent=2, sort_keys=True, separators=(":", ";"))

with open("comman.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open("new_file", "w") as csv_file1:
            csv_writer = csv.writer(csv_file1, delimiter=";")
            for line in csv_reader:
                csv_writer.writerow(line)

print " this is print\n"

