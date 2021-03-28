from PIL import Image


mode = "RGB"
size = (4, 8) # colunas, linha
color = (0, 0, 0)
tonsDeCinza = Image.new(mode, size, color)

matriz = tonsDeCinza.load()

matriz [1, 1] = (200, 200, 200)
matriz [1, 2] = (200, 200, 200)
matriz [1, 3] = (200, 200, 200)
matriz [1, 4] = (200, 200, 200)
matriz [1, 5] = (200, 200, 200)
matriz [1, 6] = (200, 200, 200)

matriz [2, 1] = (120, 120, 120)
matriz [2, 2] = (120, 120, 120)
matriz [2, 3] = (120, 120, 120)
matriz [2, 4] = (120, 120, 120)
matriz [2, 5] = (120, 120, 120)
matriz [2, 6] = (120, 120, 120)

matriz [3, 1] = (88, 88, 88)
matriz [3, 2] = (88, 88, 88)
matriz [3, 3] = (88, 88, 88)
matriz [3, 4] = (88, 88, 88)
matriz [3, 5] = (88, 88, 88)
matriz [3, 6] = (88, 88, 88)

tonsDeCinza.save('tonsDeCinza.png') 