RULES = ['.','1','0','2','3','4','5','6','7','8','9']
DIGITS = ['1','0','2','3','4','5','6','7','8','9']

def symbols(game_line: str):
    symb_ind = []
    for indchar_, char_ in enumerate(game_line):
        if char_ not in RULES:
            symb_ind.append(indchar_)
    if len(symb_ind)==0:
        return None
    return symb_ind

def symbol_star(game_line: str):
    symb_ind = []
    for indchar_, char_ in enumerate(game_line):
        if char_ == '*':
            symb_ind.append(indchar_)
    if len(symb_ind)==0:
        return None
    return symb_ind

def numbers(game_line: str):
    symb_ind = []
    for indchar_, char_ in enumerate(game_line):
        if char_ in DIGITS:
            symb_ind.append(indchar_)   
    if len(symb_ind)==0:
        return None    
    return symb_ind

def numbers_comp(symb_ind,line):
    masha_numbers = []
    if symb_ind is None:
        return (None, None)
    stfin = []
    st = symb_ind[0]
    for i in range(1,len(symb_ind)):
        if symb_ind[i]-1 != symb_ind[i-1]:
            fin = symb_ind[i-1]
            stfin.append((st,fin))
            # print(symb_str[st:fin+1])
            # print(st)
            # print(fin+1)
            # masha_numbers.append((int(symb_str[st:fin+1])))
            st = symb_ind[i]
        else:
            fin =symb_ind[i]
    stfin.append((st,symb_ind[-1]))
    # masha_numbers.append((int(symb_str[st:fin+1])))
    return (stfin,[int(line[slice[0]:slice[1]+1]) for slice in stfin])


if __name__ == "__main__":
    with open("input.txt", "r",encoding="utf-8") as f_read:
        list_of_lines = f_read.readlines()

        symb_inds = [symbols(line[:-2]) for line in list_of_lines]
        num_inds = [numbers_comp(numbers(line),line)[0] for line in list_of_lines]
        masha_num = [numbers_comp(numbers(line),line)[1] for line in list_of_lines]
        symb_stars = [symbol_star(line[:-2]) for line in list_of_lines]



        product_counts = []
        stars_products=[]
        for i in range(len(num_inds)):
            if symb_stars[i] is not None:
                for star_id in symb_stars[i]:
                    star_product = 1
                    product_count =0

                    if i==0:
                        if num_inds[i] is not None:
                            for ind,value in zip(num_inds[i],masha_num[i]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value
                        if num_inds[i+1] is not None:
                            for ind,value in zip(num_inds[i+1],masha_num[i+1]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value

                    elif i==len(num_inds)-1:
                        if num_inds[i] is not None:
                            for ind,value in zip(num_inds[i],masha_num[i]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value
                        if num_inds[i-1] is not None:
                            for ind,value in zip(num_inds[i-1],masha_num[i-1]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value

                    else:
                        if num_inds[i] is not None:
                            for ind,value in zip(num_inds[i],masha_num[i]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value
                        if num_inds[i-1] is not None:
                            for ind,value in zip(num_inds[i-1],masha_num[i-1]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value
                        if num_inds[i+1] is not None:
                            for ind,value in zip(num_inds[i+1],masha_num[i+1]):
                                if ((star_id >= ind[0]-1) and (star_id <= ind[1]+1)):
                                    product_count+=1
                                    star_product*=value

                    product_counts.append(product_count)
                    stars_products.append(star_product)
        

        print(f'Gear ratio: {sum([product  for product, product_count in zip(stars_products,product_counts) if product_count==2])}')

        adj_list = []

        for i in range(len(num_inds)):
            inner_adj_list = []
            if num_inds[i] is not None:
                for num in num_inds[i]:
                    isadjacent = False
                    if i==0:
                        if symb_inds[i] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i]])
                        if symb_inds[i+1] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i+1]])      

                    elif i==len(num_inds)-1:
                        if symb_inds[i] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i]])
                        if symb_inds[i-1] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i-1]])   

                    else:
                        if symb_inds[i] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i]])
                        if symb_inds[i-1] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i-1]])   
                        if symb_inds[i+1] is not None:
                            isadjacent = isadjacent or any([((symb>=(num[0]-1)) and (symb<=(num[1]+1))) for symb in symb_inds[i+1]])   

        
                    inner_adj_list.append(isadjacent)
            else:
                inner_adj_list.append(None)
            
            adj_list.append(inner_adj_list)

        total = 0
        for num,adj in zip(masha_num,adj_list):
            if num is not None:
                for i in range(len(adj)):
                    if adj[i]:
                        total += num[i]
        print(f'Total: {total}')


