from PIL import Image
import numpy as np

from GeneticAlgorithm import *


def processImage(letter):
    file = "alphabet/" + letter + ".bmp"
    img = Image.open(file)
    res = np.array(img).reshape(16,16,3)
    return res[:,:,1]/255
    

def getWeightMap(list):
    n = len(list)
    map = np.zeros_like(list[0])
    for letter in list:
        map += letter
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            number = map[i, j]
            if ((n-number) < number):
                number = n-number
                map[i, j] = number
    return 2*map/len(list)

def findLetter(pixels, letters, letterToSearch):
    listPossible = list(letters.keys())
    for letter in list(letters.keys()):
        for pixel in pixels:
            pixelCoordinates = getPixel(pixel)
            if (getPixelColor(pixelCoordinates, letters[letter]) != getPixelColor(pixelCoordinates, letterToSearch)):
                listPossible.remove(letter)
                break    
    return listPossible


def main():
    
    N = 5
    
    letters = {}
    listLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v", "w", "x", "y", "z"]
    


    for l in listLetters:
        letters[l] = processImage(l)
    weightMap = getWeightMap(list(letters.values()))

    pixels, fit = geneticAlgorithm(letters, N, weightMap)
    print(f"THE BEST ITERATION FOUND IS {pixels} -> NUMBER ERRORS: {abs(math.floor(fit))}")
        
    for letter in listLetters:
         print(f"LETTER {letter}, VALUES FOUND: {findLetter(pixels, letters, letters[letter])}")
    

    



if __name__ == "__main__":
    main()