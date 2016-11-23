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

a = ['aa','Aa','aA','bb']
a = list(set(a))
print(a)
