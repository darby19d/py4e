#def score_average(t, c):
    #return(t/c)
total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    #print(line)
    start = line.find(':')
    numnber = line[start+1:]
    total = total + float(numnber)
    count = count + 1
    #t = float(total)
    #c = float(count)
#print("Average spam confidence:", score_average(t, c))
print("Average spam confidence:", total/count)
quit()