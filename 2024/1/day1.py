import numpy as np

def parsing(game_line: str):

    game_descr={}
    game_descr["first_num"] = int(game_line.split(' ')[0])
    game_descr["sec_num"] = int(game_line.split(' ')[3][:-1])
    
    return game_descr["first_num"], game_descr["sec_num"]

if __name__ == "__main__":
    with open("day1_input.txt", "r",encoding="utf-8") as f_read:
        list_of_games = f_read.readlines()

        rel_fn = np.zeros(len(list_of_games))
        rel_sn = np.zeros(len(list_of_games))
        for i in range(len(list_of_games)):
            fn = parsing(list_of_games[i])[0]
            sn = parsing(list_of_games[i])[1]
            rel_fn[i] = fn
            rel_sn[i] = sn
        
        sort_fn = np.sort(rel_fn)
        sort_sn = np.sort(rel_sn)

        diff_sum = np.sum(abs(sort_fn-sort_sn))

        print(diff_sum)

        print("Task 2: Similarity Score")

        k = 0
        for j in range(len(list_of_games)):
            finds = np.where(np.array(sort_sn)==sort_fn[j])[0]
            k += sort_fn[j]*len(finds)

        print(k)