def create_seed_list(str_: str) -> list[int]:
    return [int(id_) for id_ in str_.split(":")[1].split(" ") if id_.isdigit()]


def create_range_from_str(str_: str) -> tuple[range, int]:
    nums_for_ranges = [int(dig_) for dig_ in str_.split(" ") if dig_.isdigit()]

    # dest_range =range(nums_for_ranges[0],nums_for_ranges[0]+nums_for_ranges[2])
    source_range = range(nums_for_ranges[1], nums_for_ranges[1] + nums_for_ranges[2])
    range_shift = nums_for_ranges[0] - nums_for_ranges[1]
    return (source_range, range_shift)


def add_range_to_map(
    source_range: range, range_shift: int, map_: dict[range, int]
) -> None:
    map_[source_range] = range_shift
    return

def create_seed_list_as_range(range_list:list[int]) -> list[int]:
    ll = []
    for indx, _ in enumerate(range_list):
        if indx%2 == 0:
            ll+=(list(range(range_list[indx],range_list[indx]+range_list[indx+1])))
    return ll


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f_read:
        list_of_lines = [str_.splitlines() for str_ in f_read.readlines()]


    # print('first ')

    CONVERSION = False
    conversion_map = {}
    for line_ in list_of_lines:
        current_line = line_[0]
        if len(current_line) > 0:
            if ":" in current_line:
                line_type = current_line.split(":")[0]

                if line_type == "seeds":
                    seed_list = create_seed_list(current_line)
                    # print(seed_list)
                else:
                    CONVERSION = True

            else:
                add_range_to_map(*create_range_from_str(current_line), conversion_map)

        else:
            if CONVERSION:
                for idx_, value_ in enumerate(seed_list):
                    for key, shift in conversion_map.items():
                        if value_ in key:
                            seed_list[idx_] += shift

                            break
                # print(conversion_map)
                # print(seed_list)
                conversion_map = {}


    for idx_, value_ in enumerate(seed_list):
        for key, shift in conversion_map.items():
            if value_ in key:
                seed_list[idx_] += shift

    # print(conversion_map)
    print(min(seed_list))



    # CONVERSION = False
    # conversion_map = {}
    # for line_ in list_of_lines:
    #     current_line = line_[0]
    #     if len(current_line) > 0:
    #         if ":" in current_line:
    #             line_type = current_line.split(":")[0]

    #             if line_type == "seeds":
    #                 print("seeds_start")
    #                 seed_list = create_seed_list_as_range(create_seed_list(current_line))
    #                 # print(seed_list)
    #             else:
    #                 CONVERSION = True

    #         else:
    #             add_range_to_map(*create_range_from_str(current_line), conversion_map)

    #     else:
    #         if CONVERSION:
    #             print('conv start')
    #             for idx_, value_ in enumerate(seed_list):
    #                 for key, shift in conversion_map.items():
    #                     if value_ in key:
    #                         seed_list[idx_] += shift

    #                         break
    #             print('conversion')
    #             # print(conversion_map)
    #             # print(seed_list)
    #             conversion_map = {}


    # for idx_, value_ in enumerate(seed_list):
    #     for key, shift in conversion_map.items():
    #         if value_ in key:
    #             seed_list[idx_] += shift

    # # print(conversion_map)
    # print(min(seed_list))