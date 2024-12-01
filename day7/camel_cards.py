# import numpy as np

CARDS = "AKQJT98765432"

CARDS2 = "AKQT98765432J"


def get_card_strength(string: str) -> int:
    return tuple(CARDS[::-1].index(char_) for char_ in string)


def get_card_strength_J(string: str) -> int:
    return tuple(CARDS2[::-1].index(char_) for char_ in string)


def count_hand(hand: str) -> dict[str, int]:
    return {char_: hand.count(char_) for char_ in hand}


def sort_hand(hand: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(list(hand.items()), key=lambda x: x[1], reverse=True)


def get_hand_type(hand: list[tuple[str, int]]) -> int:
    if hand[0][1] == 5:
        return 6
    elif hand[0][1] == 4:
        return 5
    elif hand[0][1] == 3:
        if hand[1][1] == 2:
            return 4
        else:
            return 3
    elif hand[0][1] == 2:
        if hand[1][1] == 2:
            return 2
        else:
            return 1
    else:
        return 0


def get_hand_type_J(hand: list[tuple[str, int]]) -> int:
    if "J" in [h[0] for h in hand]:
        if hand[0][0] != "J":
            hand.append(
                (hand[0][0], hand[0][1] + hand[[h[0] for h in hand].index("J")][1])
            )
            del hand[[h[0] for h in hand].index("J")]
            del hand[0]

        else:
            if len(hand) > 1:
                hand.append((hand[1][0], hand[0][1] + hand[1][1]))
                del hand[0]
                del hand[0]

        if hand[-1][1] == 5:
            return 6
        elif hand[-1][1] == 4:
            return 5
        elif hand[-1][1] == 3:
            if hand[0][1] == 2:
                return 4
            else:
                return 3
        elif hand[-1][1] == 2:
            if hand[0][1] == 2:
                return 2
            else:
                return 1
        else:
            return 0

    else:
        return get_hand_type(hand)


# def compare_hands(first,second):


def evaluate_hand(hand: str) -> tuple[int, int]:
    return (get_hand_type(sort_hand(count_hand(hand))), get_card_strength(hand))


def evaluate_hand_j(hand: str) -> tuple[int, int]:
    return (get_hand_type_J(sort_hand(count_hand(hand))), get_card_strength_J(hand))


# def get_num_comb(time:int,distance_to_beat:int,acceleration: float = 1.0 ) -> int:
#     t_hold = np.arange(time+1)

#     v_after = t_hold*acceleration
#     dist = v_after*(time - t_hold)
#     return(np.sum(dist>distance_to_beat))


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]

        hands = [line[0].split(" ")[0] for line in list_of_lines]
        bids = [int(line[0].split(" ")[1]) for line in list_of_lines]

        hands_evaled_o = [evaluate_hand(hand) for hand in hands]

        hands_ranking_o = [
            (hand, bid)
            for _, hand, bid in sorted(zip(hands_evaled_o, hands, bids), reverse=True)
        ]

        total = 0
        for indx, val in enumerate(hands_ranking_o[::-1]):
            # print(val[1],indx+1)
            total += val[1] * (indx + 1)
        print(total)

        # NOW WITH JOKERS
        hands_evaled = [evaluate_hand_j(hand) for hand in hands]

        hands_ranking = [
            (hand, bid)
            for _, hand, bid in sorted(zip(hands_evaled, hands, bids), reverse=True)
        ]

        total = 0
        for indx, val in enumerate(hands_ranking[::-1]):
            # print(val[1],indx+1)
            total += val[1] * (indx + 1)
        print(total)


# hands_ranking_o
