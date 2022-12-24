import os
import numpy as np
from PIL import Image

SAMPLE_IMAGE_PATH = "sample.jpg"
DECODED_IMAGE_PATH = "sample_decoded.jpg"

STRING_MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
INT_MAP = {STRING_MAP[i]: i for i in range(len(STRING_MAP))}

def convertToChar(value):
    value = value//4
    return STRING_MAP[value]

def convertToValue(char):
    return INT_MAP[char]*4

def writeToFile(string):
    with open("encoded.txt", "a") as f:
        f.write(string)

def readFromFile():
    with open("encoded.txt", "r") as f:
        return f.read()

def main():
    if not os.path.exists("encoded.txt"):
        print("The encoded file does not exist")
        return

    string = readFromFile()
    image = np.zeros((270, 480, 3), dtype=np.uint8)
    ind = 0
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            for channel in range(image.shape[2]):
                image[row, col, channel] = convertToValue(string[ind])
                ind += 1
    
    p = Image.fromarray(image.astype(np.uint8))
    p.save(DECODED_IMAGE_PATH)


if __name__ == "__main__":
    main()

