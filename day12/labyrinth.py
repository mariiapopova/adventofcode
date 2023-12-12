import numpy as np


# def get_card_strength(string: str) -> int:
#     return tuple(CARDS[::-1].index(char_) for char_ in string)


# from math import lcm
PARTS_SYMBOLS = ".S|-LJ7F"



def inside_vertical(column:np.array,map_:np.array)-> np.array:
    if_outside =1
    outside_map = np.ones_like(column)

    hirality ='n'

    for if_border,border_type,idx in zip(column,map_,range(column.shape[0]-1)):
        if if_border ==1 and border_type == 3:
            if_outside = (if_outside+1)%2

            outside_map[idx] =1
        elif if_border ==1 and border_type in [4,7]:
            outside_map[idx] =1
            if hirality=='n':
                hirality='l'
            elif hirality =='l':
                hirality='n'
            else:
                hirality = 'n'
                if_outside = (if_outside+1)%2

        elif if_border ==1 and border_type in [5,6]:
            outside_map[idx] =1
            if hirality=='n':
                hirality='r'
            elif hirality =='r':
                hirality='n'
            else:
                hirality = 'n'
                if_outside = (if_outside+1)%2



        elif if_border ==1:
            outside_map[idx] =1

        else:
            outside_map[idx] = if_outside
    
    return outside_map


    


# | is a vertical pipe connecting north and south.    2
# - is a horizontal pipe connecting east and west.    3
# L is a 90-degree bend connecting north and east.    4
# J is a 90-degree bend connecting north and west.    5
# 7 is a 90-degree bend connecting south and west.    6
# F is a 90-degree bend connecting south and east.    7
# . is ground; there is no pipe in this tile.         0
# S is the starting position of the animal            1


def fill_start(location_map:np.array)->np.array:
    y,x = np.where(location_map==1)

    return_map = location_map.copy()
    symbol_code=[]

    for y_off in range(-1, 2):
        for x_off in range(-1, 2):
            y_c, x_c = y_off + y, x_off + x

            if (
                (0 <= y_c <= location_map.shape[0]-1)
                and (0 <= x_c <= location_map.shape[1]-1)
                and ((y_off != 0) or (x_off!= 0))
            ):
                if ( y_off ==-1 and x_off ==0) and (location_map[y_c,x_c] in [2,6,7]):
                    symbol_code.append('u')
                elif ( y_off ==1 and x_off ==0) and (location_map[y_c,x_c] in [2,4,5]):
                    symbol_code.append('d')
                elif ( y_off ==0 and x_off ==-1) and (location_map[y_c,x_c] in [3,4,7]):
                    symbol_code.append('l')
                elif ( y_off ==0 and x_off ==1) and (location_map[y_c,x_c] in [3,5,6]):
                    symbol_code.append('r')

    symbol_code = ''.join(symbol_code)
    if symbol_code in ("ud",'du'):
        return_map[y,x]=2
    elif symbol_code in ("lr","rl"):
        return_map[y,x]=3
    elif symbol_code in ("ur","ru"):
        return_map[y,x]=4
    elif symbol_code in ("ul","lu"):
        return_map[y,x]=5
    elif symbol_code in ("dr","rd"):
        return_map[y,x]=7
    elif symbol_code in ("dl","ld"):
        return_map[y,x]=6
    
    print(return_map[y,x],symbol_code)
    
    return return_map
        







def line_to_list(line: list[str]) -> list[str]:
    return list(line[0])


def sym_to_did(line: list[str]) -> list[int]:
    return [PARTS_SYMBOLS.index(char) for char in line]


def return_adjacent(
    current_coords: tuple[int, int], location_map: np.array
) -> list[tuple[int, int]]:
    connected_tiles = []
    y, x = current_coords
    for y_off in range(-1, 2):
        for x_off in range(-1, 2):
            y_c, x_c = y_off + y, x_off + x

            if (
                (0 <= y_c <= location_map.shape[0]-1)
                and (0 <= x_c <= location_map.shape[1]-1)
                and ((y_off == 0) or (x_off == 0))
                and ((x_off != 0) or (y_off != 0))
            ):
                if (
                    y_off == -1
                    and location_map[y, x] in (2, 4, 5, 1)
                    and (
                        (location_map[y_c, x_c] == 2)
                        or (location_map[y_c, x_c] == 6)
                        or (location_map[y_c, x_c] == 7)
                    )
                ):
                    connected_tiles.append((y_c, x_c))
                if (
                    y_off == 1
                    and location_map[y, x] in (2, 6, 7, 1)
                    and (
                        (location_map[y_c, x_c] == 2)
                        or (location_map[y_c, x_c] == 4)
                        or (location_map[y_c, x_c] == 5)
                    )
                ):
                    connected_tiles.append((y_c, x_c))
                if (
                    x_off == -1
                    and location_map[y, x] in (3, 5, 6, 1)
                    and (
                        (location_map[y_c, x_c] == 3)
                        or (location_map[y_c, x_c] == 4)
                        or (location_map[y_c, x_c] == 7)
                    )
                ):
                    connected_tiles.append((y_c, x_c))
                if (
                    x_off == 1
                    and location_map[y, x] in (3, 4, 7, 1)
                    and (
                        (location_map[y_c, x_c] == 3)
                        or (location_map[y_c, x_c] == 5)
                        or (location_map[y_c, x_c] == 6)
                    )
                ):
                    connected_tiles.append((y_c, x_c))
    return connected_tiles


def return_connected(current_coords: tuple[int, int], loop_map,location_map: np.array)->list[tuple[int,int]]:
    connected_tiles = []
    y, x = current_coords
    for y_off in range(-1, 2):
        for x_off in range(-1, 2):
            y_c, x_c = y_off + y, x_off + x


            if (
                (0 <= y_c <= location_map.shape[0]-1)
                and (0 <= x_c <= location_map.shape[1]-1)):

                if loop_map[y_c,x_c] == 0:
                    loop_map[y_c,x_c] = 2
                    connected_tiles.append((y_c,x_c))

                # elif y_off==-1 and x_off==-1:
                #     if location_map[y_c,x_c] != 7:#in (2,4,5):
                #         loop_map[y_c,x_c]=-2
                #         connected_tiles.append((y_c,x_c))
                elif y_off==-1 and x_off==0:
                    if location_map[y_c,x_c] != 3:#in (2,4,5):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==-1 and x_off==1:
                    if location_map[y_c,x_c] != 6:#in (2,4,5):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==0 and x_off==-1:
                    if location_map[y_c,x_c] !=2:#in (3,5,6):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==0 and x_off==1:
                    if location_map[y_c,x_c] !=2:#in (3,5,6):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==1 and x_off==-1:
                    if location_map[y_c,x_c] != 4:#in (2,4,5):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==1 and x_off==0:
                    if location_map[y_c,x_c] !=3:#in (3,5,6):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))
                elif y_off==1 and x_off==1:
                    if location_map[y_c,x_c] !=5:#in (3,5,6):
                        loop_map[y_c,x_c]=-2
                        connected_tiles.append((y_c,x_c))

    return connected_tiles


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

    symbol_list = list(map(sym_to_did, (map(line_to_list, list_of_lines))))
    location_map = np.array(symbol_list)
    distance_map = np.zeros_like(symbol_list)
    distance_map[:] = -1

    start_y, start_x = np.where(location_map == 1)

    distance_map[start_y, start_x] = 0

    left_search = []
    right_search = []

    left_search.append((start_y, start_x))
    right_search.append((start_y, start_x))

    step_count = 1
    new_found = True
    while new_found:
        left_adjacents = return_adjacent(left_search[-1], location_map)
        right_adjacents = return_adjacent(right_search[-1], location_map)

        new_found = False
        for i in left_adjacents:
            if distance_map[i] < 0:
                left_search.append(i)
                distance_map[i] = step_count
                new_found = True

                break

        for i in right_adjacents:
            if distance_map[i] < 0:
                right_search.append(i)
                distance_map[i] = step_count
                new_found = True
                break

        step_count += 1

    print(step_count)
    print(distance_map)
    print(location_map)

    print(np.max(distance_map))

    loop_map = distance_map.copy()
    loop_map[loop_map > -1] = 1
    loop_map[loop_map < 1] = 0

    edge_coords = (
        [(0, i) for i in range(loop_map.shape[1]) if loop_map[0, i] != 1]+
        [(i, 0) for i in range(loop_map.shape[0]) if loop_map[i, 0] != 1]+
        [(i, loop_map.shape[1]-1) for i in range(loop_map.shape[0]) if loop_map[i, loop_map.shape[1]-1] != 1]+
        [(loop_map.shape[0]-1,i) for i in range(loop_map.shape[1]) if loop_map[loop_map.shape[0]-1,i] != 1]
        
    )
    # print('loop map')

    # print(loop_map)

    
    vert_maps = []
    filled_loc = fill_start(location_map)
    for column_idx in range(loop_map.shape[1]):
        vert_maps.append(inside_vertical(loop_map[:,column_idx],filled_loc[:,column_idx]))

    v_in = np.stack(vert_maps,axis=1)
    v_in[v_in==0]=7
    v_in[v_in==1]=0

    print("inside")
    # print(v_in)
    print("joint")
    # print(v_in+loop_map)

    print((v_in==7).sum())
