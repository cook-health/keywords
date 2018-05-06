keywords = [x[0:-1].lower() for x in open('wordlist_selected.txt', 'r')]
positive = [x[0:-1].lower() for x in open('positive-words.txt', 'r')]
negative = [x[0:-1].lower() for x in open('negative-words.txt', 'r')]
keywords.append('feel')
freq = ['before','after','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','fifteen','meal','1','2','3','4','5','6','7','8','9','10','11','12','per','day','days','hour','hours','minute','once','twice','times','time','daily','15','half']
test = [x[0:-1] for x in open("drug.txt", mode='r', errors='ignore')]
disease = [x[0:-1] for x in open('disease.txt','r',encoding = 'utf-8')]

def textrecog(text_list):
    shorter = []
    keyword = []
    determine = {}
    result = {}
    empty = []
    medicine = []
    mode = False
    record = 0
    for word in text_list:
        for t in disease:
            if len(word) > 3 and word in t.split(' '):
                result[word] = 'diagnose'
                break
    for index in range(len(text_list)):
        if len(text_list[index]) > 1:
            shorter.append(text_list[index])
        if text_list[index] in test:
            mode = True
            record = index
    if mode:
        d = ''
        for i in text_list[record:]:
            if i in freq:
                d = d + i + ' '
        result[text_list[record]] = d
    else:
        for i in range(len(shorter)):
            w = shorter[i]
            if w in negative:
                determine[i] = 0
            elif w in positive:
                determine[i] = 1
            elif w.isdigit():
                determine[i] = 2
            if w in keywords:
                keyword.append(i)
        key = []
        for i in determine.keys():
            key.append(i)
        for index in range(len(keyword)):
            i = keyword[index]
            choose = -1
            for j in key:
                if (j - i > 0 or i - j == 1):
                    if index + 1 == len(keyword):
                        choose = j
                        break
                    elif j <= keyword[index + 1]:
                        choose = j
                        break
            if choose != -1 and determine[choose] == 0:
                if shorter[i] not in result.keys():
                    result[shorter[i]] = shorter[choose]
            elif choose != -1 and determine[choose] == 1:
                if (choose+1) in key:
                    if determine[choose+1] == 2:
                        if shorter[i] not in result.keys():
                            result[shorter[i]] = shorter[choose+1]
                elif (choose+2) in key:
                    if determine[choose+2] == 2:
                        if shorter[i] not in result.keys():
                            result[shorter[i]] = shorter[choose+2]
                else:
                    if shorter[i] not in result.keys():
                        result[shorter[i]] = shorter[choose]
            elif choose != -1 and determine[choose] == 2:
                if shorter[i] not in result.keys():
                    result[shorter[i]] = shorter[choose]
            if choose == -1:
                empty.append(shorter[choose])
    return (result,empty)

"""
Returns a dictionary of (keyword, location)
"""
def dataprocess(text):
    text_list = text.split()
    result, empty = textrecog(text_list)
    result_rev, empty_rev = textrecog(text_list[::-1])
    for key in result_rev.keys():
        if key not in result.keys():
            result[key] = result_rev[key]
    for e in empty:
        if e not in result.keys():
            result[e] = True
    return result
