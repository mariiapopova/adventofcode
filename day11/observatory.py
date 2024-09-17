import numpy as np


# def get_card_strength(string: str) -> int:
#     return tuple(CARDS[::-1].index(char_) for char_ in string)


# from math import lcm
# PARTS_SYMBOLS = ".S|-LJ7F"

def get_pairwise_manhattan(x:np.array)->np.array:
    xx,xy = np.meshgrid(x,x)
    dists = np.tril(np.abs(xx-xy), k=0)
    return dists


def process_line(lines:list[str])->list[list[int]]:
    result = []
    ch_to_did = lambda x: 1 if x=='#' else 0
    for line in lines:
        result.append(list(map(ch_to_did,line)))
    if  1 not in result[-1]:
        result.append(result[-1])

    return result


def process_line_2(lines:list[str])->list[list[int]]:
    result = []
    ch_to_did = lambda x: 1 if x=='#' else 0
    for line in lines:
        result.append(list(map(ch_to_did,line)))

    return result


def process_columns(matr:np.array)->np.array:
    result =[]
    for column_indx in range(matr.shape[1]):
        if matr[:,column_indx].sum()==0:
           result.append(matr[:,column_indx])
           result.append(matr[:,column_indx])
        else:
            result.append(matr[:,column_indx]) 
    return np.array(result)

def inside_vertical(column:np.array,map_:np.array)-> np.array:
    pass

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

    list_num = [ line for lines in  map(process_line,list_of_lines)  for line in lines ]
    arr_num = np.array(list_num)
    arr_num =process_columns(arr_num).T
    y,x = np.where(arr_num ==1)


    x_d = get_pairwise_manhattan(x)
    y_d = get_pairwise_manhattan(y)

    print(x_d.sum()+y_d.sum())


    list_num = [ line for lines in  map(process_line_2,list_of_lines)  for line in lines ]
    arr_num = np.array(list_num)


    sum_h,sum_v = arr_num.sum(axis=0)==0,arr_num.sum(axis=1)==0
    y,x = np.where(arr_num ==1)


    y_el = y.copy()
    x_el = x.copy()
    for ind,val in enumerate(y):
        y_el[ind] = y_el[ind]  +(1000000-1)*np.sum(sum_v[:val])
    for ind,val in enumerate(x):
        x_el[ind] =x_el[ind] + (1000000-1)*np.sum(sum_h[:val])


    x_d = get_pairwise_manhattan(x_el)
    y_d = get_pairwise_manhattan(y_el)

    print(x_d.sum()+y_d.sum())