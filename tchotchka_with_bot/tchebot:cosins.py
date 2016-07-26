import codecs
import os
import re
import pickle, json
from scipy import spatial
import random

BASE = os.path.dirname(os.path.abspath(__file__))


class dataset:
    def __init__(self, filename):
        self.file_data = 'data.dat'
        self.data = []
        self.file_in = filename
        self.matrix = []
        self.file_matrix = 'matrix.dat'
        self.dictionary = {}
        self.file_dictionary = 'dict.json'

        try:
            # load data from .dat
            self.data = pickle.load(open(os.path.join(BASE, self.file_data), 'rb'))
        except FileNotFoundError:
            # make data set and write in file
            print(">> file 'data.dat' is not found. Create new 'data.dat'")
            with codecs.open(os.path.join(BASE, self.file_in), 'r', encoding='UTF-8') as file:
                console_counter = 0
                for sentence in file.readlines():
                    sentence = re.split(r'[^a-zа-я]', sentence.lower())
                    for trash in ['', 'а', 'и', 'не', 'y', 'ты']:
                        while trash in sentence:
                            sentence.remove(trash)
                    self.data.append(sentence)
                    console_counter += 1
                    if console_counter % 500 == 0:
                        print(">>> successfully added string {0} in dataset! ".format(console_counter))

                with open(os.path.join(BASE, self.file_data), 'wb+') as file:
                    pickle.dump(self.data, file)


        try:
            # load dictionary from .json
            with open(os.path.join(BASE, self.file_dictionary), 'r') as file:
                self.dictionary = json.load(file)
        except FileNotFoundError:
            # make a dictionary and write in file
            print(">> file 'dict.json' is not found. Create new 'dict.json")
            console_counter = 0
            for word in sentence:
                self.dictionary[word] = sentence.index(word)
                console_counter += 1
                if console_counter % 500 == 0:
                    print(">>> successfully added string {0} in dictionary! ".format(console_counter))
            json.dump(self.dictionary, open(os.path.join(BASE, self.file_dictionary), 'w'))


        try:
            # load matrix from .dat
            self.matrix = pickle.load(open(os.path.join(BASE, self.file_matrix), 'rb'))
        except FileNotFoundError:
            # make matrix and write in file
            print(">> file 'matrix.dat' is not found. Create new 'matrix.dat'")
            counter = 0
            for sentence in self.data:
                vector = self.make_vector(sentence)
                self.matrix.append(vector)
                counter += 1
                if counter % 500 == 0:
                    print(">>> successfully added string {0} in matrix! ".format(counter))
            with open(os.path.join(BASE, self.file_matrix), 'wb+') as file:
                pickle.dump(self.matrix, file)


    def make_vector(self, sentence):
        return [sentence.count(word) for word in self.dictionary.keys()]

    def count_cosses(self, vector):
        return [spatial.distance.cosine(vector, iter_vector) for iter_vector in self.matrix]

    def reply(self, input_sentence):
        input_sentence = re.split(r'[^a-zа-я]', input_sentence.lower())  # tokenize
        vector = self.make_vector(input_sentence)  # makes a vector like in the matrix
        cosins = self.count_cosses(vector)  # finds a cos difference between user's sentence and every sentence in the data, http://bit.ly/2a6F31g
        print(cosins)
        similar_sentences = []
        for i in range(0, 5):
            similar_sentences.append(" ".join(self.data[cosins.index(min(cosins))]))
            cosins[cosins.index(min(cosins))] = 2
        print(similar_sentences)
        #return "\n".join(similar_sentences)
        return similar_sentences[random.randint(1,5)]


if __name__ == "__main__":
    set_of_lenka = dataset('bot_replics:small.txt')
    while (True):
        print(set_of_lenka.reply(input('>>> ')))