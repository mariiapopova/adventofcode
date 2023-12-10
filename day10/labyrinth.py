import numpy as np


# def get_card_strength(string: str) -> int:
#     return tuple(CARDS[::-1].index(char_) for char_ in string)


# from math import lcm
PARTS_SYMBOLS = ".S|-LJ7F"


# | is a vertical pipe connecting north and south.    2
# - is a horizontal pipe connecting east and west.    3
# L is a 90-degree bend connecting north and east.    4
# J is a 90-degree bend connecting north and west.    5
# 7 is a 90-degree bend connecting south and west.    6
# F is a 90-degree bend connecting south and east.    7
# . is ground; there is no pipe in this tile.         0
# S is the starting position of the animal            1


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
                (0 <= y_c <= location_map.shape[0])
                and (0 <= x_c <= location_map.shape[1])
                and ((y_off == 0) or (x_off == 0))
                and ((x_off != 0) or (y_off != 0))
            ):
                if y_off == -1 and  location_map[y, x] in (2,4,5,1) and (
                    (location_map[y_c, x_c] == 2)
                    or (location_map[y_c, x_c] == 6)
                    or (location_map[y_c, x_c] == 7)
                ):
                    connected_tiles.append((y_c, x_c))
                if y_off == 1 and location_map[y, x] in (2,6,7,1)  and (
                    (location_map[y_c, x_c] == 2)
                    or (location_map[y_c, x_c] == 4)
                    or (location_map[y_c, x_c] == 5)
                ):
                    connected_tiles.append((y_c, x_c))
                if x_off == -1 and location_map[y, x] in (3,5,6,1) and (
                    (location_map[y_c, x_c] == 3)
                    or (location_map[y_c, x_c] == 4)
                    or (location_map[y_c, x_c] == 7)
                ):
                    connected_tiles.append((y_c, x_c))
                if x_off == 1 and  location_map[y, x] in (3,4,7,1) and (
                    (location_map[y_c, x_c] == 3)
                    or (location_map[y_c, x_c] == 5)
                    or (location_map[y_c, x_c] == 6)
                ):
                    connected_tiles.append((y_c, x_c))
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

        new_found =False
        for i in left_adjacents:
            if distance_map[i] < 0:
                left_search.append(i)
                distance_map[i] = step_count
                new_found =True

                break

        for i in right_adjacents:
            if distance_map[i] < 0:
                right_search.append(i)
                distance_map[i] = step_count
                new_found =True
                break

        step_count += 1


    print(step_count)
    print(distance_map)
    print(location_map)
    
    print(np.max(distance_map))