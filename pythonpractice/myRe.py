# encoding: UTF-8

def getPattern(patternStr):
    pattern = []
    for i in range(len(patternStr)):
        if i==0 and patternStr[i] == '*':
            return ''
        elif patternStr[i] == '*':
            pattern[i-1] += patternStr[i]
        else:
            pattern.append(patternStr[i])
    return pattern

def applyPattern(pattern, str):
    result = []
    i = 0
    j = 0
    for i in range(len(pattern)):
        if len(pattern[i])==1:
            if pattern[i]=='.' or str[j]==pattern[i]:
                result.append(str[j])
                j += 1
                i += 1
            else:
                return False
    return result

# print(getPattern('a*bcd'))
print(applyPattern(getPattern('abc'), 'abc'))
