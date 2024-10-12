def lister(lst):
    retstr = ''
    for i in range(len(lst)):
        retstr = retstr + str(i+1) + ' -> ' + str(lst[i]) + '\n'
    return retstr