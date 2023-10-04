s = '>' + 15 * '1' + 16 * '4' + 20 * '6'
while '>1' in s or '>4' in s or '>6' in s:
    if '>1' in s:
        s = s.replace('>1', '4161>', 1)
    if '>4' in s:
        s = s.replace('>4', '1611>', 1)
    if '>1' in s:
        s = s.replace('>6', '414>', 1)
sum = s.count('1') + s.count('4') * 4 + s.count('6') * 6
print(sum)
