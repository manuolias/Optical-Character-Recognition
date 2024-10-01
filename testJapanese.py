from PIL import Image
import numpy as np

from GeneticAlgorithm import *


def processImage(letter):
    file = "japanesealphabet/_kana" + letter + "19.jpg"
    img = Image.open(file)
    res = np.array(img).reshape(16,16)/255
    for i in range(len(res)):
        for j in range(len(res[i])):
            number = res[i][j]
            res[i][j] = round(number)
    return res

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
    
    N = 6


    letters = {}
    listLetters = ["A", "BA", "CHI", "DA", "E", "FU", "HA", "HE", "HI", "HO", "I", "JI", "KA", "KE", "KI", "KO", "KU", "MA", "ME",
                   "MI", "MO", "MU", "N", "NA", "NE", "NI", "NO", "NU", "O", "PI", "RA", "RE", "RI", "RO", "RU", "SA", "SE", "SHI",
                   "SO", "SU", "TA", "TE", "TO", "TSU", "U", "WA", "WO", "YA", "YO", "YU"]
    
    for l in listLetters:
        letters[l] = processImage(l)

    weightMap = getWeightMap(list(letters.values()))
    pixels, fit = geneticAlgorithm(letters, N, weightMap)
    
    print(f"THE BEST ITERATION FOUND IS {pixels} -> Nº ERRORS: {abs(math.floor(fit))}")


    for letter in listLetters:
         print(f"LETTER {letter}, VALUES FOUND: {findLetter(pixels, letters, letters[letter])}")

    



if __name__ == "__main__":
    main()