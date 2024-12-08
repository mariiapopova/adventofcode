# import numpy as np


# def get_card_strength(string: str) -> int:
#     return tuple(CARDS[::-1].index(char_) for char_ in string)


from math import lcm

def calculate_path_length(start_node,map_,instructions):
    step_counter = 0
    current_node = start_node
    while(current_node[-1]!='Z'):
        current_instruction= instructions[step_counter%len(instructions)]
        current_node = current_node = map_[current_node][current_instruction]
        step_counter+=1
    return step_counter




if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

        instructions = list_of_lines[0][0]
        del(list_of_lines[0])
        del(list_of_lines[0])



        map_ = {}
        for line in list_of_lines:
            map_[line[0].split(' ')[0]] = {'L':line[0].split(' ')[2][1:4],
                                        'R':line[0].split(' ')[3][0:3]}

        # current_node = 'AAA'
        # step_counter = 0
        # while current_node!='ZZZ':
        #     current_instruction = instructions[step_counter%len(instructions)]
        #     current_node = map_[current_node][current_instruction]
        #     step_counter+=1
        
        # print(step_counter)

    
    current_nodes = [ node for node in map_.keys()  if node[-1] == 'A' ]
    path_length = [ calculate_path_length(node,map_,instructions) for node in current_nodes ]
    # next_nodes = current_nodes
    # step_counter = 0
    # while any([node[-1]!="Z" for node in current_nodes ]):
    #     current_instruction = instructions[step_counter%len(instructions)]
        
        
    #     for node in current_nodes:
    #         next_nodes.add( map_[node][current_instruction])
    #     current_nodes = next_nodes
    #     next_nodes = set()

    #     step_counter+=1

    #     print(len(current_nodes))
    # print(step_counter)

    print(lcm(*path_length))




# hands_ranking_o
