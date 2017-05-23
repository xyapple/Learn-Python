'''
7.2 Write a program that prompts for a file name, 
then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.

'''
# fname = input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
total = 0
for line in fh:    
    if not line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        continue
    # print(line)
    pos = line.find(':')
    num = float(line[pos+1:])
    # print(num)

    count = count + 1
    total = total + num

print (total/count)  
       
print("Done!")

'''
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        
        line = line.rstrip()
        
        continue
    #print line
    pos = line.find(':')
    num = float(line[pos+1:])
    
    count = count + 1
    total = total + num
   
print "Average spam confidence:", total/count
'''