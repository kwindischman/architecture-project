def parseInput():

    i = 0
    lengt = ""
    addr0 = ""
    addr1 = ""
    addr2 = ""

    with open(filename) as f:
        for line in f:
            if i % 3 == 0:
                lengt = line[5:7]
                addr0 = line[10:18]
            if i % 3 == 1:
                addr1 = line[6:14]
                addr2 = line[33:41]
            if i % 3 == 2:
                print(lengt, addr0, addr1, addr2)
                #add your function call here
            i+=1
