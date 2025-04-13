import cv2

image = cv2.imread(r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\Sonic1_MD_Map_Ghz1.png") 
height, width, _ = image.shape

block_size = 256

for x in range(0, width, block_size):
    cv2.line(image, (x, 0), (x, height), (0, 0, 255), 2) 

for y in range(0, height, block_size):
    cv2.line(image, (0, y), (width, y), (0, 0, 255), 2)

cv2.imwrite("grid_output.png", image)

