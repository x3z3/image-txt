import os
import numpy as np
from PIL import Image

SAMPLE_IMAGE_PATH = "sample.jpg"
ENCODED_IMAGE_PATH = "sample_encoded.jpg"

STRING_MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
INT_MAP = {STRING_MAP[i]: i for i in range(len(STRING_MAP))}

def convertToChar(value):
    value = value//4
    return STRING_MAP[value]

def convertToValue(char):
    return INT_MAP[char]

def writeToFile(string):
    with open("encoded.txt", "a") as f:
        f.write(string)

def main():
    if os.path.exists("encoded.txt"):
        os.remove("encoded.txt")

    p = Image.open(SAMPLE_IMAGE_PATH)
    p = p.convert(mode="RGB")
    p.thumbnail(size=(480, 270))
    image = np.array(p).astype(int)

    string = ""
    string += str(image.shape[0]) + '*' + str(image.shape[1]) + '~'
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            for channel in range(image.shape[2]):
                char = str(convertToChar(image[row, col, channel]))
                string += char
                if len(string) >= 10:
                    writeToFile(string)
                    string = ""
    writeToFile(string)
    
    p = Image.fromarray(image.astype(np.uint8))
    p.save(ENCODED_IMAGE_PATH)



if __name__ == "__main__":
    main()

