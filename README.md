# Optical-Character-Recognition

Optical Character Recognition (OCR) is a technology used to convert images of text into machine-readable text, which can then be edited, searched, and analyzed digitally. In this report, we present a genetic algorithm for solving an OCR problem involving alphabet characters represented as 16x16 grayscale images. The goal of the problem is to find the position of a few pixels that distinguish the characters of the alphabet from each other. My genetic algorithm is designed to find the optimal combination of pixels that yields the highest accuracy in character recognition.

There are two test versions, one with Latin characters and another one with Japanese characters. To try any one of them just run the file testLatin.py or testJapanese.py.
In those file, the value of N can be changed, which determines the size of the set of pixels we are looking for. In the file GeneticAlgorithm.py there are some other values that can be changed to obtain different results, those are POPULATION_SIZE, MUTATION_RATE and N_ITER_MAX. Please note those values have been selected to increase optimization.

The results of the project can be found in the file report.pdf, where everything is visualized and explained properly.
