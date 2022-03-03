#!/home/rafael/.asdf/shims/python

# Author: Rafael Camargo
# Date: 03/03/2022
# E-mail: rafasc0404@gmail.com

import sys

filename = sys.argv[1]

lines = open(filename, 'r').readlines()

limit = 80

for i in lines:
    line = i[0:-1].split(" ")
    chars = 0
    charscount = len(line) + sum([(chars + len(j)) for j in line])
    print(charscount)

    if charscount > limit: # if it exceeded
        tmp_charscount = 0
        fitted_words = []
        for k in line:
            tmp_charscount += len(k)
            fitted_words.append(k)
            if tmp_charscount >= limit: break
        print(line)
        print(fitted_words)

        # get all the exceeded words
        # throw them in the next line
        #   .how to get the next iteration?
        #   .pass the anterior line to the next?
    elif charscount < limit: # if fits more words
        print('teste')
        # get the first word from the next line
        # throw it at the and of this


