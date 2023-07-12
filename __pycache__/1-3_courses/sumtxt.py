## This code will use a RE to parse values from a text and sum them all together. 
import re
fname = input('Enter the name of the file: ')
if len(fname) < 1:
  fname = 'regex_sum_1832508.txt'
fh = open(fname)

tot = 0
val = None
for lines in fh: 
  nums = re.findall('[0-9]+', lines)
  
  if nums:
    for num in nums:
      if val is None:
        val = int(num)
      else:
        val = int(num)
      tot = tot + val
print(tot)


