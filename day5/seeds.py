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
            ll.append(range(range_list[indx],range_list[indx]+range_list[indx+1]))
    return ll


def process_range(range_:range, map_: dict[range, int] )->list[range]:
    
    ranges_to_process = range_
    resulting_ranges=[]

    while len(ranges_to_process)>0:
        current_range =ranges_to_process.pop()
        range_is_found =False

        for  shift_range, offset in map_.items():

            if (current_range.start in shift_range and current_range.stop-1 in shift_range):
                resulting_ranges.append(range(current_range.start+offset,current_range.stop+offset))
                range_is_found = True
            elif (current_range.start in shift_range):
                resulting_ranges.append(range(current_range.start+offset,shift_range.stop+offset))
                ranges_to_process.append(range(shift_range.stop,current_range.stop))
                range_is_found = True
            elif (current_range.stop-1 in shift_range) :
                resulting_ranges.append(range(shift_range.start+offset,current_range.stop+offset))
                ranges_to_process.append(range(current_range.start,shift_range.start))
                range_is_found = True
            elif (shift_range.start in current_range and shift_range.stop-1 in current_range):
                resulting_ranges.append(range(shift_range.start+offset,shift_range.stop+offset))
                ranges_to_process.append(range(current_range.start,shift_range.start))
                ranges_to_process.append(range(shift_range.stop,current_range.stop))
                range_is_found = True
        if not range_is_found:
            resulting_ranges.append(current_range)
    
    return resulting_ranges



    # for  shift_range, offset in map_.items():
    #     range_is_found =False
    #     for indx,range_ in enumerate(ranges_to_process):
    #         if (range_.start in shift_range and range_.stop-1 in shift_range):
    #             resulting_ranges.append(range(range_.start+offset,range_.stop+offset))
    #             range_is_found = True
    #         #     # del ranges_to_process[indx]
    #         # elif (range_.start in shift_range):
    #         #     resulting_ranges.append(range(range_.start+offset,shift_range.stop+offset))
    #         #     ranges_to_process.append(range(shift_range.stop,range_.stop))
    #         #     range_is_found = True
    #         # elif (range_.stop in shift_range) :
    #         #     resulting_ranges.append(range(shift_range.start+offset,range_.stop+offset))
    #         #     ranges_to_process.append(range(range_.start,shift_range.start))
    #         #     range_is_found = True
    #     if not  range_is_found :
    #         resulting_ranges.append(range_)
    # return resulting_ranges#sorted(resulting_ranges,key = lambda x: x.start)

        
        



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



    CONVERSION = False
    conversion_map = {}
    for line_ in list_of_lines:
        current_line = line_[0]
        if len(current_line) > 0:
            if ":" in current_line:
                line_type = current_line.split(":")[0]

                if line_type == "seeds":
                    # print("seeds_start")
                    seed_list = create_seed_list_as_range(create_seed_list(current_line))
                    # print(sorted(seed_list,key = lambda x: x.start))
                    # print(seed_list)
                else:
                    CONVERSION = True

            else:
                add_range_to_map(*create_range_from_str(current_line), conversion_map)

        else:
            if CONVERSION:
                # print('conv start')
                # print(sorted(seed_list,key = lambda x: x.start))
                # print(conversion_map)
                

                # for idx_, value_ in enumerate(seed_list):
                #     for key, shift in conversion_map.items():
                #         if value_ in key:
                #             seed_list[idx_] += shift

                #             break
                seed_list =process_range(seed_list,conversion_map)
                # print(sorted(seed_list,key = lambda x: x.start))
                # print('conversion fin')
                # print(conversion_map)
                # print(seed_list)
                conversion_map = {}

    # print('conv start')
    # print(print(sorted(seed_list,key = lambda x: x.start)))
    # print(conversion_map)
        
    seed_list =process_range(seed_list,conversion_map)
    # print(sorted(seed_list,key = lambda x: x.start))
    # print('conversion')
    print(sorted(seed_list,key = lambda x: x.start)[0].start)
    # # print(conversion_map)
    # print(min(seed_list))