def get_winning_num_from_str(string: str) -> list[int]:
    return [
        int(dig)
        for dig in string.split("|")[0].split(":")[1].split(" ")
        if dig.isdigit()
    ]


def get_your_num_from_str(string: str) -> list[int]:
    return [int(dig) for dig in string.split("|")[1].split(" ") if dig.isdigit()]


def get_card_number(string: str) -> int:
    a = string.split(":")[0].split(" ")[-1]
    return int(a)


def get_score_count(win: list[int], your: list[int]) -> int:
    return sum([number in win for number in your])

def get_score(win: list[int], your: list[int]) -> int:
    score = get_score_count(win,your)
    if score == 0:
        return 0
    else:
        return 2 ** (score - 1)

def process_card(id_,cards):
    
    score =get_score_count(*(cards[id_]['numbers']))
    copies_num  = cards[id_]['numbers']
    if score>0:

        for id_shift in range(score):
            cards[id_+id_shift+1]["copies_num"]+=cards[id_]['copies_num']





if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = f_read.readlines()

        your_list = [get_your_num_from_str(str_[:-1]) for str_ in list_of_lines]
        win_list = [get_winning_num_from_str(str_[:-1]) for str_ in list_of_lines]
        card_ids = [get_card_number(str_) for str_ in list_of_lines]

        scores = [get_score(win, your) for win, your in zip(your_list, win_list)]

        # print(your_list)
        # print(win_list)
        print(sum(scores))

        # 2nd part

        # create initial card sequence

        cards = {id_: {"numbers":(win,your),"copies_num":1} for id_,win,your in zip(card_ids,win_list,your_list) }

        for id_ in card_ids:
            process_card(id_,cards)

        print(sum([cards[key_]['copies_num']for key_ in cards.keys()]))