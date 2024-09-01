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
                combs.append(f'{i[0].replace("!","")}&{j[0].replace("!","")}')
    lst = [i for idx,i in enumerate(lst) if idx not in remove]
    combs = [[x] for x in combs]
    lst += combs
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    return lst

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
                combs.append(f'{i[0].replace("!","")}!&{j[0].replace("!","")}')
    lst = [i for idx,i in enumerate(lst) if idx not in remove]
    combs = [[x] for x in combs]
    lst += combs
    lst = [sorted(i) for i in lst]
    lst = sorted(lst,key=lambda x:x[0])
    return lst

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




# Example usage:
lst = [['a', '!b'], ['b', '!a'],['!e','!f']]
lst = [AND(i) for i in lst]
lst = []
print(lst)