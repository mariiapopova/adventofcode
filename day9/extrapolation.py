import numpy as np



def get_padded_diff_right(X:np.array,order:int )-> np.array:
    return np.pad(np.diff(lines,n=order,axis=1),((0,0),(order,0)))

def get_padded_diff_left(X:np.array,order:int )-> np.array:
    return np.pad(np.diff(lines,n=order,axis=1),((0,0),(0,order)))

def to_int(line:list[str])-> list[int]:
    return [ int(char) for char in line if char.isdigit()]


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

    lines_split = [line[0].split(' ') for line in list_of_lines]

    lines_num = list(map(lambda x:[ int(char) for char in x ] ,lines_split))#if char.isdigit()

    lines = np.array(lines_num)

    padded_difs_right = np.zeros( (lines.shape[-1],*lines.shape))
    padded_difs_left = np.zeros( (lines.shape[-1],*lines.shape))

    padded_difs_right[0,:] = lines[:]
    padded_difs_left[0,:] = lines[:]
    current_order = 1
    last_padded_right =1
    while np.sum(last_padded_right)!=0:
        last_padded_right = get_padded_diff_right(lines,current_order)
        last_padded_left = get_padded_diff_left(lines,current_order)
        padded_difs_right[current_order,:] = last_padded_right[:]
        padded_difs_left[current_order,:] = last_padded_left[:]
        current_order+=1

    print(int(padded_difs_right.sum(axis =0)[:,-1].sum()))
    mult = np.array([2*(0-i%2)+1 for i in range(padded_difs_left.shape[0])])

    

    print(int((padded_difs_left[:,:,0]*mult[:,None]).sum(axis = 0).sum()))
