fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
#lst = list()
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    email = line.split()
    print(email[1])
    count = count + 1
#print(lst)
print("There were", count, "lines in the file with From as the first word")
