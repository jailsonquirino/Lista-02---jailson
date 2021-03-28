from PIL import Image


mode = "RGB"
size = (11, 12) # colunas, linha
color = (255, 255, 255)
bitman = Image.new(mode, size, color)

matriz = bitman.load()

for y in range(bitman.size[0]):
    for x in range(bitman.size[1]):
        print(matriz[y, x], end = '')
   # print()

matriz [5, 0] = (0, 0, 0)
matriz [4, 1] = (0, 0, 0)
matriz [5, 1] = (0, 0, 0)
matriz [6, 1] = (0, 0, 0)
matriz [3, 2] = (0, 0, 0)
matriz [4, 2] = (0, 0, 0)
matriz [5, 2] = (0, 0, 0)
matriz [6, 2] = (0, 0, 0)
matriz [7, 2] = (0, 0, 0)
matriz [2, 3] = (0, 0, 0)
matriz [3, 3] = (0, 0, 0)
matriz [4, 3] = (0, 0, 0)
matriz [5, 3] = (0, 0, 0)
matriz [6, 3] = (0, 0, 0)
matriz [7, 3] = (0, 0, 0)
matriz [8, 3] = (0, 0, 0)
matriz [2, 4] = (0, 0, 0)
matriz [8, 4] = (0, 0, 0)
matriz [2, 5] = (0, 0, 0)
matriz [8, 5] = (0, 0, 0)
matriz [2, 6] = (0, 0, 0)
matriz [8, 6] = (0, 0, 0)
matriz [2, 7] = (0, 0, 0)
matriz [8, 7] = (0, 0, 0)
matriz [2, 8] = (0, 0, 0)
matriz [8, 8] = (0, 0, 0)
matriz [2, 9] = (0, 0, 0)
matriz [8, 9] = (0, 0, 0)
matriz [2, 10] =(0, 0, 0)
matriz [3, 10] =(0, 0, 0)
matriz [4, 10] =(0, 0, 0)
matriz [5, 10] =(0, 0, 0)
matriz [6, 10] =(0, 0, 0)
matriz [7, 10] =(0, 0, 0)
matriz [8, 10] =(0, 0, 0)

bitman.save('bitman.png') 
