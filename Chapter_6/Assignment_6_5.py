text = 'X-DSPAM-Confidence:    0.8475'
start = text.find('0')
end = start + 6
final = text[start:end]
final = float(final)
print(final)
quit()