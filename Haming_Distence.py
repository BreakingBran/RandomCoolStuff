'''
Global Values:
'''
mismatch_list = [] # list of all values in Neighbours

'''
This function determines how closely two strings match each other
'''

def Hamming_Distance(string1,string2,threshold):
    mistakes = 0
    for values in range(len(string1)):
        if string1[values] != string2[values]:
            mistakes += 1
    if mistakes > threshold:
        return False
    else:
        return True

'''
This function looks through a file to see how many patterns in the file are close enough to the pattern given
'''

def Hamming_Distance_Mismatch(pattern,data,error_margin,Output=False,Output2 = False):
    index_list = []
    value_list = []
    length_of_pattern = len(pattern)
    if data.startswith('data'):     
        with open(data) as data_set:
            data_info = data_set.read()        
            data_info = data_info.replace('\n','')        
            for values in range(len(data_info)):
                if values > len(data_info) - len(pattern):
                    continue
                data_patterns = data_info[values:length_of_pattern]
                if Hamming_Distance(pattern,data_patterns,error_margin):                
                    index_list.append(values)
                    value_list.append(data_patterns)
                length_of_pattern += 1
    else:
        for values in range(len(data)):
                if values > len(data) - len(pattern):
                    continue
                data_patterns = data[values:length_of_pattern]
                if Hamming_Distance(pattern,data_patterns,error_margin):                
                    index_list.append(values)
                    value_list.append(data_patterns)
                length_of_pattern += 1
    if not Output:
        Answer = open("datasets/Answer.txt",'w')
        for values in index_list:
            Answer.write(str(values)+" ")
        Answer.close() 
    elif Output:
        if Output2:
            return value_list  
        index_list = len(index_list)                      
        return  index_list  
    
'''
This function counts how many patterns the above function returns
'''
    
def Count_Hamming(data,pattern,error_margin):     
    count = Hamming_Distance_Mismatch(pattern,data,error_margin,True)   
    return count 

'''
This reverses the strings of a pattern
'''    

def Reverse(pattern):
    word = pattern
    word = word[::-1]
    return word
'''
This function turns a pattern of nucleotides "CATG" into a numerical value
'''

def PatterntoNumber(pattern):
    pattern_num = []
    answer_list = 0
    len_pattern = len(pattern)
    for values in range(len_pattern):
        if pattern[values] == 'A':
            pattern_num.append(0)
        elif pattern[values] == 'T':
            pattern_num.append(3)
        elif pattern[values] == 'C':
            pattern_num.append(1)    # This creates a list of base 4 with all the letters having a value 
        elif pattern[values] == 'G':
            pattern_num.append(2)
    multplication_agent = 4**(len_pattern-1)  #This creates a variables which i multiply all the elements of the list pattern_num to get a decimal value/ index '''
    for numbers in range(len_pattern):
        test = pattern_num[numbers]
        answer_list += test*multplication_agent
        multplication_agent = multplication_agent/4
    return int(answer_list)

'''
This function turns the numbers returned by the above function into a pattern
'''

def NumbertoPattern(index,length):
    def NumberToSymbol(number):
        if number == 0:
            symbol = "A"
        elif number == 1:
            symbol = "C"
        elif number == 2:
            symbol = "G"
        elif number == 3:
            symbol = "T"
        return symbol
    digits = []
    Pattern = []
    while index > 0:
        digits.insert(0, index % 4)
        index  = index // 4
    digits.reverse()
    for values in range(length-1,-1,-1):
        try:
            Pattern.append(NumberToSymbol(digits[values]))
        except:
            Pattern.append("A")
    Pattern = "".join(Pattern)
    return Pattern

'''
Finds neighbors of strings
'''

def Letter_Applier(string):
    letters = ['A','C','T','G']
    rearanged_list = [string]
    string2 = list(string)
    for values1 in range(len(string2)):
        for values2 in letters:
            string2 = list(string)
            string2[values1] = values2
            string2 = ''.join(string2)
            if not string2 in rearanged_list:
                rearanged_list.append(string2)
    return rearanged_list

def Neighbours(pattern,mismatches):
    if mismatches <= 0:
        return []
    elif not isinstance(pattern, list):
        temp = pattern
        pattern = []
        pattern.append(temp)
    mismatch_list = []
    for values in pattern:
        mismatch_list = mismatch_list + Letter_Applier(values)
    return mismatch_list + Neighbours(mismatch_list,mismatches-1)   
        
'''
This function looks for frequent patterns in a  file, but also counts patterns that have mistakes
'''

def Frequent_Words_Hamming(data, k_mer_length,error_margin):    
    Frequencies = {-1:0} #This is a dictionary with all the numerical values of the strings possible
    max_value = -1
    mismatch_list = []
    frequent_words = []
    with open(data) as text:
        text = text.read()
        text = text.replace("\n","")
        for values in range(len(text)-k_mer_length+1):
            pattern_test = text[values:values+k_mer_length]           
            mismatch_list = Neighbours(pattern_test,error_margin)  
            mismatch_list = list(set(mismatch_list))          
            for values in mismatch_list:
                try:
                    pattern_number = PatterntoNumber(values)
                except:
                    print(values)
                    return
                Frequencies[pattern_number] = Frequencies.get(pattern_number, 0) +1
                if max_value == -1:
                    max_value = Frequencies[pattern_number]
                    frequent_words.append(values)
                elif Frequencies[pattern_number] > max_value:
                    max_value = Frequencies[pattern_number]
                    frequent_words = []
                    frequent_words.append(values)
                elif Frequencies[pattern_number] == max_value:
                    frequent_words.append(values)
    Answer = open("datasets/Answer.txt",'w') 
    for values in frequent_words :
        Answer.write(values+" ")
    Answer.close() 

"""print(mismatch_list)
 print(len(mismatch_list))
 for values in mismatch_list:
     if not Hamming_Distance(pattern,values,mismatch):
         print(values)


    sum = 0
    for lines in text:
        sum += 1
    print(sum-3
 pattern = 'ACG' 
 mismatch = 2
 Neighbours(pattern,mismatch)
"""
'''
This function finds the most reccuring k-mer with mismatches in a genome
'''

def Ultimate_Frequent_Words(Genome,k_mer_length,mismatches):
    Frequencies = {}
    max_value = -1
    frequent_words = []
    if Genome.startswith('data'):
        with open(Genome) as text:
            text = text.read()
            text = text.replace('/n','')            
            for values in range(len(Genome)-k_mer_length+1):
                pattern = text[values:values+k_mer_length]
                mismatch_list = [pattern]
                mismatch_list = mismatch_list + Neighbours(mismatch_list,mismatches)
                for values in mismatch_list:
                    values2 = list(values)
                    values2 = values2[::-1]
                    values2 = ''.join(values2)
                    pattern_number = PatterntoNumber(values)
                    pattern_number2 = PatterntoNumber(values2)
                    Frequencies[pattern_number] = Frequencies.get(pattern_number, 0) +1
                    Frequencies[pattern_number2] = Frequencies.get(pattern_number, 0) +1
                    if max_value == -1:
                        max_value = Frequencies[pattern_number]
                        frequent_words.append(values)
                    elif Frequencies[pattern_number] > max_value:
                        max_value = Frequencies[pattern_number]
                        frequent_words = []
                        frequent_words.append(values)
                    elif Frequencies[pattern_number] == max_value:
                        frequent_words.append(values)
                    if Frequencies[pattern_number2] > max_value:
                        max_value = Frequencies[pattern_number2]
                        frequent_words = []
                        frequent_words.append(values2)
                    elif Frequencies[pattern_number2] == max_value:
                        frequent_words.append(values2)
    print(Frequencies)
    Answer = open("datasets/Answer.txt",'w') 
    for values in frequent_words :
        Answer.write(values+" ")
    Answer.close() 
            
#Genome = 'datasets/Testing_File.txt'
#Ultimate_Frequent_Words(Genome,4,1)

a = 'Hello How are you'






