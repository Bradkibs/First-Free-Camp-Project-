val = ["98 + 35", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(values,state = False):
    # split list
    new_lst = [x.strip().split() for x in values]
    first = []
    second = []
    not_first = []
    its_width = []
    second_width = []
    dashes =[]
    # checking if given digit does not exceed 4
    for item in new_lst:
        for j in item:
            if len(j)>4:
                return 'Error: Numbers cannot be more than four digits.'
        # checking if the values passed on do not contain non-integers
        if not (item[0].isdigit() and item[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
    # to return an error when the values exceed 5
    if len(values) >5 :
        return 'Error: Too many problems.'
    for inp in new_lst:
        if inp[1] != "+" and inp[1] != "-":
            return "Error: Operator must be '+' or '-'."
    # appending the items into their corresponding lists
    for i in new_lst:
        first.append(i[0])
        second.append(i[2])
        not_first.append(i[1:])
        # this will be the width of items in the first line
        width = max((len(i[0]),len(i[2]))) + 2
        its_width.append(width)
    # this will be the width of the digits in the second line
        new_width = width - 1
        second_width.append(new_width)
   
    for i in first:
        # using try to avoid errors when fewer items in the list are passed on
        try:
            if i == first[0]:
                first[0]=i.rjust(its_width[0])
            elif i == first[1]:
                first[1]=i.rjust(its_width[1])
            elif i == first[2]:
                first[2]=i.rjust(its_width[2])
            elif i == first[3]:
                first[3]=i.rjust(its_width[3])
            elif i == first[4]:
                first[4] = i.rjust(its_width[4])
        except IndexError:
            pass
    first_line = '    '.join(i for i in first)
    for i in not_first:
        try:
            if i[1] == not_first[0][1]:
                not_first[0][1]=i[1].rjust(second_width[0])
            elif i[1] == not_first[1][1]:
                not_first[1][1]=i[1].rjust(second_width[1])
            elif i[1] == not_first[2][1]:
                not_first[2][1]=i[1].rjust(second_width[2])
            elif i[1] == not_first[3][1]:
                not_first[3][1]=i[1].rjust(second_width[3])
            elif i[1] == not_first[4][1]:
                not_first[4][1] = i[1].rjust(second_width[4])
        except IndexError:
            pass
    joined = list(map(''.join, not_first))
    second_line = '    '.join(i for i in joined)
    
    for item in range(len(new_lst)):
        try:
            if item ==0:
                dashes.append(('-'*its_width[0]))
            elif item ==1:
                dashes.append(('-'*its_width[1]))
            elif item ==2:
                dashes.append(('-'*its_width[2]))
            elif item ==3:
                dashes.append(('-'*its_width[3]))
            elif item ==4:
                dashes.append(('-'*its_width[4]))
            
        except IndexError:
            pass
        joined_dashes = '    '.join(i for i in dashes)
    # checking the state to print out the answers
    if state:
        calc= []
        for item in new_lst:
            if item[1] == '+':
                calc.append(int(item[0])+int(item[2]))
            elif item[1] == '-':
                calc.append(int(item[0])-int(item[2]))
        for b in calc:
            calc = list(map(str,calc))
        for b in calc:
            try:
                if b == calc[0]:
                    calc[0] = b.rjust(its_width[0])
                elif b == calc[1]:
                    calc[1] = b.rjust(its_width[1])
                elif b == calc[2]:
                    calc[2] = b.rjust(its_width[2])
                elif b == calc[3]:
                    calc[3] = b.rjust(its_width[3])
                elif b == calc[4]:
                    calc[4] = b.rjust(its_width[4])        
            except IndexError:
                pass
            last_line = '    '.join(i for i in calc)
        return first_line+'\n'+second_line+'\n'+joined_dashes+'\n'+last_line
    else:        
        return first_line+'\n'+second_line+'\n'+joined_dashes

print(arithmetic_arranger(val,True))
