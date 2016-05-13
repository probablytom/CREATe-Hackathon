name_map = {}
bad_chars = ['\n','\r','\t']
with open("Variable_information_W4.csv") as varInfoFile:
    for line in varInfoFile.readlines()[1:]:
        line = line.replace("\"", "")
        parts = line.split(",")
        name_map[parts[0]] = ''.join(char for char in parts[1] if char not in bad_chars)

with open("W4_clean.csv") as dataFile:
    titles = dataFile.readline()
    titles = titles.split(",")
    for index in range(len(titles)):
        titles[index] = ''.join(char for char in titles[index] if char not in bad_chars)
        if titles[index] in name_map.keys():
            titles[index] = name_map[titles[index]]
    newTitleLine = ','.join(titles)
    print newTitleLine
    with open("better_data.csv", 'w+') as betterData:
        betterData.write(newTitleLine)
        for line in dataFile.readlines()[1:]:
            betterData.write(line + '\n')

print "Done!"
