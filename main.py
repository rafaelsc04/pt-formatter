#!/home/rafael/.asdf/shims/python

# Author: Rafael Camargo
# Date: 03/03/2022
# E-mail: rafasc0404@gmail.com

import sys

lines = open(sys.argv[1], 'r').readlines()

limit = 80

for i in lines:
    line = i[0:-1].split(" ")
    chars = 0
    charscount = (len(line) + sum([(chars + len(j)) for j in line])) - 1
   
    if len(line) == 1 and line[0] == '': continue # means it is an empty line
		
    if charscount > limit: # if it exceeded
        tmp_charscount = 0
        fitted_words = []
        for word in line:
            if (tmp_charscount + len(word)) > limit: break
            tmp_charscount += (1 + len(word))
            fitted_words.append(word)

        exceed = [x for x in line if not x in fitted_words or fitted_words.remove(x)]

        exceed_charcount = 0
        for word in exceed:
            exceed_charcount += (1 + len(word))

        # throw exceeds them in the next line
        #   .how to get the next iteration?
        #   .pass the anterior line to the next?
    elif charscount < limit: # if fits more words
        continue
        # get the first word from the next line
        # throw it at the and of this
    print()
