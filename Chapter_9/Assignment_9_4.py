name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
ecount = dict()
elist = list()
bigemail = None
bigcount = 0
# create list for emailers
for line in handle:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    elist.append(email)
#print(elist)
# populate dictionary with emailers and the frequency counts
for emailer in elist:
    ecount[emailer] = ecount.get(emailer, 0) + 1
#print(ecount)
# identify which emailer is the most and the count
for emailer,count in ecount.items():
    if emailer is None or count > bigcount:
        bigemail = emailer
        bigcount = count
print(bigemail, bigcount)
quit()