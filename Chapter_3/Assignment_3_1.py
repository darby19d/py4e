hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40.0:
    rt = 40
    ot = h-rt
    otr = r * 1.5
    print((rt * r)+(ot*otr))
else:
    print(h * r)
quit()