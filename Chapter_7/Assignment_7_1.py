fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    #print(line.rstrip())
    sline = line.rstrip()
    print(sline.upper())
quit()