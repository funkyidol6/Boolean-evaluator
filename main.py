import test

print("enter truth table in format INA,INB,INC,IND,etc : O1,O2,O3,O4,O5 (when finished press Enter on an empty line):")
table = []
while True:
    temp = input()
    if temp:
        table.append(temp)
    else:
        break

def XNOR(lst):
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    remove = []
    combs = []
    for idx_i,i in enumerate(lst):
        for idx_j,j in enumerate(lst[idx_i:len(lst)]):
            if len(i)!=2 or len(j)!=2:
                continue
            if (i[0] == f'!{j[0]}' and i[1] == f'!{j[1]}') or (j[0] == f'!{i[0]}' and j[1] == f'!{i[1]}'):
                remove.append(idx_i)
                remove.append(idx_j)
                combs.append(f'{i[0].replace("!","")} !& {i[1].replace("!","")}')
    lst = [i for idx,i in enumerate(lst) if idx not in remove]
    combs = [[x] for x in combs]
    lst += combs
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    return lst

def combine_expressions(lst):
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    remove = []
    combs = []
    for idx_i,i in enumerate(lst):
        for idx_j,j in enumerate(lst[idx_i:len(lst)]):
            if len(i)!=2 or len(j)!=2:
                continue
            if (i[0]==f'!{j[1]}' and j[0]==f'!{i[1]}') or (i[1]==f'!{j[0]}' and j[1]==f'!{i[0]}'):
                remove.append(idx_i)
                remove.append(idx_j)
                combs.append(f'{i[0].replace("!","")} & {j[0].replace("!","")}')
    lst = [i for idx,i in enumerate(lst) if idx not in remove]
    combs = [[x] for x in combs]
    lst += combs
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    return lst

def colonize(array:list[str]):
    t = [[j[i] for j in array] for i in range(len(array[0]))]
    t = [list(set(i)) for i in t]
    a = []
    for idx,i in enumerate(t):
        if i == ['1'] or i == ['0']:
            boo = True
            if i == ['0']:
                boo = False
            a.append((idx,boo))
    return a

def AND(lst):
    remove = []
    add = []
    for idx,i in enumerate(lst):
        if idx!=len(lst)-1:
            if '!' in i and '!' in lst[idx+1]:
                remove.append(idx)
                remove.append(idx+1)
                add.append(f'{i.replace("!","")} !* {lst[idx+1].replace("!","")}')
    lst = [i for idx,i in enumerate(lst) if idx not in remove]
    lst += add
    lst = sorted(lst,key=lambda x:x[0],reverse=True)
    return lst

def gray_codes(n):

        if n == 0:
            return ['']
        first_half = gray_codes(n-1)
        second_half = first_half.copy()

        first_half = ['0' + code for code in first_half]
        second_half = ['1' +code for code in reversed(second_half)]

        return first_half + second_half

temp = table[0].rsplit(":")[0]
if len(temp)%2==0:
    x_label , y_label = gray_codes(len(temp)/2),gray_codes(len(temp)/2)
else:
    x_label , y_label = gray_codes((len(temp)/2)-0.5),gray_codes((len(temp)/2)+0.5)

out = [x.rsplit(':')[1] for x in table]
table = {x.rsplit(':')[0]:x.rsplit(':')[1] for x in table}
table2 = {}


ALPHA_U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA_L = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(out[0])):
    ans = []
    temp2 = [x[i] for x in table.values()]
    for key,val in zip(table.keys(),temp2):
        table2[key] = val

    spot = []

    for idx_y,y in enumerate(y_label):
        temp = []
        for idx_x,x in enumerate(x_label):
            a = x+y
            temp.append(table2[a])
        spot.append(temp)
    for j in test.check(spot):
        coords = test.generate_coords(spot,j)

        temp = [x_label[t[1]]+y_label[t[0]] for t in coords]

        a = []
        for q in colonize(temp):
            a.append(ALPHA_L[q[0]] if q[1] else f'!{ALPHA_L[q[0]]}')
        ans.append(a)  
    ans = combine_expressions(ans)
    ans = XNOR(ans)
    ans = [AND(i) for i in ans]
    ans = [' * '.join(i) for i in ans]
    t = f'({") + (".join(ans)})'
    print(f'The logic for {ALPHA_U[i]} is {t}')