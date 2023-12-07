import numpy as np

def get_num_comb(time:int,distance_to_beat:int,acceleration: float = 1.0 ) -> int:
    t_hold = np.arange(time+1)

    v_after = t_hold*acceleration
    dist = v_after*(time - t_hold)
    return(np.sum(dist>distance_to_beat))


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

    times = [int(time) for time in list_of_lines[0][0].split(":")[1].split(" ") if time.isdigit()]
    dists = [int(time) for time in list_of_lines[1][0].split(":")[1].split(" ") if time.isdigit()]
    
    print (np.prod(list(map(get_num_comb, times,dists))))
    
    


