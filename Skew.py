def Skew(Genome,length):
    counter = [0]
    running_total = 0
    counter_append = counter.append
    for values in range(length):
        if Genome[values] == "C":
            running_total -= 1
            counter_append(running_total)
        if Genome[values] == "G":
            running_total += 1
            counter_append(running_total)
        if Genome[values] == "A" or Genome[values] == "T":
            counter_append(running_total)        
    return counter
 
Genome =  "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
length = len(Genome)
    
'''    
print(Skew(Genome,14))
'''


File_Name = "datasets/Testing_File.txt"

def Min_Skew(File_Name):
    running_total = 0
    min_list = []
    minnimum = 0
    count = 1 
    with open(File_Name) as dataset:
        for lines in dataset:
            for values in lines:
                if values == "C":
                    running_total -= 1
                if values == "G":
                    running_total += 1
                if count == 1:
                    minnimum = running_total
                    min_list.append(count)
                if values == "A" or values == "T":
                    count += 1
                    continue
                elif running_total < minnimum:
                    minnimum = running_total
                    min_list = [count]
                elif running_total == minnimum:
                    min_list.append(count)
                count += 1
    Answer = open("datasets/Answer.txt",'w')
    for values in min_list:
        Answer.write(str(values)+" ")
    Answer.close()

Min_Skew(File_Name)
       