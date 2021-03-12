import cv2
RGB = list()

for l in range(3):
    if l == 0:
        namefile = 'R'
    elif l == 1:
        namefile = 'G'
    elif l == 2:
        namefile = 'B'
    with open(f'{namefile}.txt', 'r') as file:
        RGB += [int(i[:-1] if i[:-1] != '' else 0) for i in file]
        for i in range(57*l, 57 + 57*l):
            for g in range(57*l, 56 + 57*l):
                #print(l[g], l[g+1])
                if RGB[g] > RGB[g+1]:
                    RGB[g], RGB[g+1] = RGB[g+1], RGB[g]
                    
print(f"R= {RGB[:57:7]}", '\n')
print(f"G= {RGB[57:114:7]}", '\n')
print(f"B= {RGB[114::7]}", '\n')