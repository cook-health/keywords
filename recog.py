keywords = [x[0:-1].lower() for x in open('wordlist_selected.txt', 'r')]
positive = [x[0:-1].lower() for x in open('positive-words.txt', 'r')]
negative = [x[0:-1].lower() for x in open('negative-words.txt', 'r')]
keywords.append('feel')

def textrecog(text_list):
    shorter = []
    keyword = []
    determine = {}
    result = {}
    for word in text_list:
        if len(word) > 1:
            shorter.append(word)
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
    return result

def dataprocess(text):
    text_list = text.split()
    result = textrecog(text_list)
    result_rev = textrecog(text_list[::-1])
    for key in result_rev.keys():
        if key not in result.keys():
            result[key] = result_rev[key]
    return result
 
