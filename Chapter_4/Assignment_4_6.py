def computepay(h, r):
    if h > 40.0:
        rt = 40
        ot = h - rt
        otr = r * 1.5
        return((rt * r) + (ot * otr))
    else:
        return(h * r)
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay", p)
quit()