a = 'АГДЕЙСЭ'

cou = 1
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        if (x1=='Е' and x2=='Г' and x3=='Э') or (x4=='Е'  and x2=='Г' and x3=='Э') or (x4=='Е' and x5=='Г'  and x3=='Э') or (x4=='Е' and x5=='Г'  and x6=='Э'):
                            cou=cou+1+cou
                            
                            
print(cou)
