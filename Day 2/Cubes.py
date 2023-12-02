
N_RED =12
N_GREEN = 13
N_BLUE  =14

def process_game_1(game_line: str):

    game_descr={}
    game_descr["id"] = int(game_line.split(':')[0].split(' ')[1])
    game_descr["rounds"] = game_line.split(':')[1].split(';')
    game_descr["round_descr"]=[]


    for round_ in game_descr["rounds"]:
        sets = round_.split(',')

        for set_ in sets:
            number =int(set_.split(" ")[1])

            color = set_.split(" ")[2][0]

            if color == 'r':
                if number > N_RED:
                    return 0
            if color == 'g':
                if number > N_GREEN:
                    return 0
            if color == 'b':
                if number> N_BLUE:
                    return 0
    
    return game_descr["id"]


def process_game_2(game_line: str):

    game_descr={}
    game_descr["id"] = int(game_line.split(':')[0].split(' ')[1])
    game_descr["rounds"] = game_line.split(':')[1].split(';')
    game_descr["round_descr"]=[]

    red_max = 0
    green_max = 0
    blue_max = 0

    for round_ in game_descr["rounds"]:
        sets = round_.split(',')


        for set_ in sets:
            number =int(set_.split(" ")[1])
            color = set_.split(" ")[2][0]

            if color == 'r':
                red_max = max((red_max,number))
    
            if color == 'g':
                green_max = max((green_max,number))

            if color == 'b':
                blue_max = max((blue_max,number))

    return red_max*green_max*blue_max







if __name__ == "__main__":
    with open("input.txt", "r",encoding="utf-8") as f_read:
        list_of_games = f_read.readlines()


        possible_ids = sum(map(process_game_2,list_of_games))

        print(possible_ids)

