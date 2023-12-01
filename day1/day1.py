inp = open("day1_input.txt", "r")
inp_lines = inp.readlines()
inp.close()

fin = 0

digits = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0','1', '2',
          '3','4','5','6','7','8','9']
digits1 = ['orez','eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin', '0','1', '2',
          '3','4','5','6','7','8','9']

for line in inp_lines:
    fir = 0
    sec = 0
    fir1 = 0
    sec1 = 0

    temp = [(line.find(j), j) for j in digits if j in line]
    temp1 = min(temp)[1]

    fir = digits.index(temp1) % 10 
        
    fir1 = str(fir)

    temp_rev = [(line[::-1].find(j), j) for j in digits1 if j in line[::-1]]
    temp2 = min(temp_rev)[1]
    sec = digits1.index(temp2) % 10 

    sec1 = str(sec)

    fin+=int(fir1+sec1)

print(fin)
        