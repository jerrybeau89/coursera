## This code takes in numbers and prints out the min and max numbers
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try: 
#       ival = int(num)
#     except: 
#       print('Invalid input')
#       continue

#     if smallest is None : 
#       smallest = ival
#       largest = ival
#     elif ival < smallest: 
#       smallest = ival
#     elif ival > largest:
#       largest = ival

# print("Maximum is ", largest)
# print("Minimum is ", smallest)


## This code takes in a file name, determines parses a number from a line and keeps a running total and prints the avg
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# tot = 0
# num = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     pos = line.find(':')
#     num = line[pos + 1: len(line)]
#     num = num.strip()
#     num = float(num)
#     tot = tot + num
#     count = count + 1

# print('Average spam confidence:', tot/count)


#This code takes in a file name, and creates a list of words in a file, it ensures no duplicate words are added
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# line1 = ''
# for line in fh:
#   if line == line :
#     line = line.strip()
#     line1 = line1 + " " + line
# line1 = line1.split()
# line1.sort()
# for word in line1:
#   if not word in lst:
#     lst.append(word)
# print(lst)


##This code takes in a file name and checks how many From emails were in the file
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# for lines in fh:
#   line = lines.strip()
#   if not lines.startswith('From'):
#     continue
#   if lines.startswith('From:'):
#     continue
#   emails = line.split()
#   count += 1
#   print(emails[1])

# print("There were", count, "lines in the file with From as the first word")


## creates a dictionary with a if statement
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#   # if name not in counts : 
#   #   counts[name] = 1
#   # else : 
#   #   counts[name] = counts[name] + 1
#   counts[name] = counts.get(name, 0) + 1
# print(counts)


## Creates a dictionary and adds the words and counts of the dict() and prints the largest word and count
# counts = dict()
# fname = input('Please enter a text file: ')
# fh = open(fname)
# for line in fh :
#   words = line.split()
#   for word in words :
#   # if name not in counts : 
#   #   counts[name] = 1
#   # else : 
#   #   counts[name] = counts[name] + 1
#    counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items() :
#   if bigcount is None or count > bigcount :
#     bigword = word
#     bigcount = count
# print(bigcount, bigword)


## Filters through a file and prints the most used email and count
# counts = dict()
# lst = list()
# # fname = input('Please enter a text file: ')
# fname = 'mbox-short.txt'
# fh = open(fname)
# for lines in fh :
#     line = lines.strip()
#     if not lines.startswith('From'):
#         continue
#     if lines.startswith('From:'):
#         continue
#     emails = line.split()
#     lst.append(emails[1])
      
# for email in lst :
#     counts[email] = counts.get(email, 0) + 1

# lgcount = None
# lgemail = None
# for addr,count in counts.items() :
#   if lgcount is None or count > lgcount :
#     lgemail = addr
#     lgcount = count
# print(lgemail, lgcount)
 

# d = {'a':10, 'c':22, 'b':1}
# t = sorted(d.items())
# tmp = list()
# print(t)
# for k, v in t:
#   tmp.append( (v, k))
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# count = dict()
# lst = list()
# fname = 'mbox-short.txt'
# fh = open(fname)
# for lines in fh:
#     line = lines.strip()
#     if not lines.startswith('From'):
#         continue
#     if lines.startswith('From:'):
#         continue
#     emails = line.split()
#     time = emails[5]
#     time = time.split(':')
#     hour = time[0]
#     lst.append(hour)

# for hours in lst:
#     count[hours] = count.get(hours, 0) + 1

# dist = sorted(count.items())
# for key, value in dist:
#   print(key, value)
# print(dist)


# class Solution:
#     # prices = [7,6,5,4,2,1]
#     prices = [7, 1, 5, 3, 6, 4]
#     def maxProfit(prices):
#         profit = 0
#         price = prices

#         print(prices)
#         price.sort(reverse=True)
#         print(prices)
#         if price == prices:
#             print(price)
#             print(profit)

#     maxProfit(prices)
