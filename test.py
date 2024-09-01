def check(array:list[list[str]]):
    probs = []
    for idx_i,i in enumerate(array):
        for idx_j,j in enumerate(i):
            if j == '0':
                continue
            else:
                for k in range(count(array,(idx_i,idx_j),(0,1))):
                    for l in range(count_range(array,(idx_i,idx_j),(idx_i,idx_j+k if idx_j+k < len(i) else (idx_j+k) - len(i)))):
                        ul = (idx_i,idx_j)
                        ur = (idx_i, idx_j+k if idx_j+k < len(i) else (idx_j+k)-len(i))
                        bl = (idx_i+l if idx_i+l < len(array) else (idx_i+l)-len(array),idx_j)
                        br = (idx_i+l if idx_i+l < len(array) else (idx_i+l)-len(array),idx_j+k if idx_j+k < len(i) else (idx_j+k)-len(i))
                        probs.append({'ul':ul,
                                    'ur':ur,
                                    'bl':bl,
                                    'br':br})

    probs = [dict(t) for t in {tuple(d.items()) for d in probs}]
    

    unique_dicts = []
    unique_combinations = set()
    for d in probs:
        combination = tuple(d[k] for k in ['ul', 'ur', 'bl', 'br'])
        if combination not in unique_combinations:
            unique_combinations.add(combination)
            unique_dicts.append(d)

    probs = sorted(probs,key = lambda x : area(array,x),reverse=True)
    probs = sorted(probs, key=lambda x: (x['ul'][0], x['ul'][1], x['br'][0], x['br'][1]))
    probs = unique_dicts



    probs = [i for i in probs if is_power_of_two(area(array,i))]
    probs = sorted(probs,key = lambda x : area(array,x))
    probs = sorted(probs, key=lambda x: (x['ul'][0], x['ul'][1], x['br'][0], x['br'][1]))


    
    probs = [[i,area(array,i)] for i in probs]
    probs = replace_dupes(array,probs)

    probs = sorted(probs,key = lambda x : area(array,x),reverse=True)

    probs = remove_cops(array,probs)
    

    
    return probs

def tempar(carray,coord):
    for t in coord:
        if carray[t[0]][t[1]] == '0':
            return True
    return False


def remove_cops(array,coords):
    checkarray = [['0' for _b in range(len(array[0]))] for _a in range(len(array))]
    remove = []
    for idxi,i in enumerate(coords):
        points = generate_coords(array,i)
        if tempar(checkarray,points):
            for j in points:
                checkarray[j[0]][j[1]] = '1'
        else:
            remove.append(idxi)
    coords = [a for idx,a in enumerate(coords) if idx not in remove]
    return coords

            

def replace_dupes(array,coords):
    dic = sorted(coords,key=lambda x:x[1],reverse=True) 
    dic = [i[0] for i in dic]
    remove = []
    for idx_i,i in enumerate(dic):
        for j in range(idx_i+1,len(dic)):
            a = generate_coords(array,i)
            b = generate_coords(array,dic[j])
            if a == b:
                remove.append(j)
            else:
                c = [t for t in a if t not in b]
                d = [t for t in b if t not in a]
                if c == [] or d == []:
                    remove.append(j)
    remove = list(set(remove))
    p = [_ for idx,_ in enumerate(dic) if idx not in remove]
    
    return p



def generate_coords(array,coord):
    ul = coord['ul']
    br = coord['br']
    row = list(range(len(array[0]))) #x
    column = list(range(len(array))) #y
    coords = []
    if ul[0] <= br[0]:
        column = list(range(ul[0],br[0]+1))
    else:
        column = list(range(0,br[0]+1))+list(range(ul[0],len(column)))
    if ul[1] <= br[1]:
        row = list(range(ul[1],br[1]+1))
    else:
        row = list(range(0,br[1]+1))+list(range(ul[1],len(row)))

    column,row = sorted(column),sorted(row)
    for i in column:
        for j in row:
            coords.append((i,j))
    return sorted(coords)


def is_power_of_two(n):
    """Check if a number is a power of 2."""
    return n != 0 and (n & (n - 1)) == 0

def count(array:list[int],coord:tuple[int,int],dir:tuple[int,int]) -> int:
    y,x = coord
    a = 1
    temp = [y,x]
    while True:
        tempco = next_check(array,temp,dir)
        if array[tempco[0]][tempco[1]] == "1" and a != len(array[0]):
            a+=1
            if temp[dir[1]] < len(array[0])-1:
                temp[dir[1]]+=1
            else:
                temp[dir[1]]=0
        else:
            break
    return a
            


def area(array,rect):
    ul = list(rect['ul'])
    br = list(rect['br'])
    row = len(array[0])-1
    column = len(array)-1
    y,x = 1,1
    if ul[0]>br[0]:
        y += (column-ul[0])+br[0]+1
    else:
        y += (br[0]-ul[0])

    if ul[1]>br[1]:
        x += (row-ul[1])+br[1]+1
    else:
        x += (br[1]-ul[1])


    return x*y




def extract_subset(array, index1, index2):
        row = list(range(len(array[0]))) #x
        column = list(range(len(array))) #y

        if index1 <= index2:
            row = list(range(index1,index2+1))
        else:
            row = list(range(0,index2+1))+list(range(index1,len(row)))
        return row
    

def count_range(array:list[int],t1:tuple[int,int],t2:tuple[int,int]) -> int:
    a = []
    dir = (0,1)
    v = extract_subset(array, t1[1], t2[1])
    for i in v:
        a.append(count(array,(t1[0],i),(1,0)))
    return min(a)
        

def next_check(array:list[list[int]],current_coord:tuple[int,int],dir:tuple[int,int],) ->  tuple[int,int]:
    temp = (0,0)


    if dir[0] == 1:
        if  current_coord[0] + 1 > len(array)-1:
            temp = (0,current_coord[1])
        else:
            temp = (current_coord[0]+1,current_coord[1])
    elif dir[1] == 1:
        if current_coord[1] + 1 > len(array[0])-1:
            temp = (current_coord[0],0)
        else:
            temp = (current_coord[0],current_coord[1]+1)

    return temp


temp_array = [['1', '0', '0', '1'], 
              ['0', '1', '1', '1'], 
              ['1', '1', '0', '1'], 
              ['1', '1', '1', '1']]

#print(count_range(temp_array,(3,0),(3,3)))

#print(count([['0', '0', '1', '1'],['1', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1']],(2,2),(1,0)))

#print(next_check([['0', '0', '1', '1'],['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1']],(1,3),(0,1)))


#print(area({'ul': (0, 3), 'ur': (0, 3), 'bl': (1, 3), 'br': (1, 3)}))


"""print(check([['0', '0', '1', '1'],
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1']]))"""

"""print(area([['0', '0', '1', '1'],
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1']],{'ul': (0, 2), 'ur': (0, 2), 'bl': (2, 2), 'br': (2, 2)}))"""
if __name__ == '__main__':
    for i in check(temp_array):
        print(i)


"""print(generate_coords([['0', '0', '1', '1'],
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1'], 
             ['0', '0', '1', '1']],{'ul': (0, 2), 'ur': (0, 2), 'bl': (2, 2), 'br': (2, 2)}))"""

