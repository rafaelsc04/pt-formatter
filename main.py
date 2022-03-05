#!/home/rafael/.asdf/shims/python

# Author: Rafael Camargo
# Date: 03/03/2022
# E-mail: rafasc0404@gmail.com

import sys

lines = open(sys.argv[1], 'r').readlines()

limit = 80

new_file = open('file.txt', 'a')

for i in lines:
    line = i[0:-1].split(" ")

    if len(line) == 1 and line[0] == '': # means it is an empty line
        new_file.write("\n")
        continue

    chars = 0
    charscount = (len(line) + sum([(chars + len(j)) for j in line])) - 1

    if charscount > limit:
        tmp_charscount = 0
        fitted_words = [[]]
        for word in line:
            if word == '': continue
            if (tmp_charscount + len(word)) > limit: break
            tmp_charscount += (1 + len(word))
            fitted_words[0].append(word)

        excess = [x for x in line if not x in fitted_words[0]]

        excess_charcount = 0
        for word in excess: excess_charcount += (1 + len(word))

        new_lines = list()

        while excess_charcount > limit:
            tmp_charscount = 0
            new_line = list()
            for word in excess:
                if word == '': continue
                if (tmp_charscount + len(word)) > limit: break
                tmp_charscount += (1 + len(word))
                new_line.append(word)
                excess.remove(word)
            new_lines.append(new_line)
            excess_charcount = 0
            for word in excess: excess_charcount += (1 + len(word))

        new_lines.append(excess)

        fitted_words.extend(new_lines)

        for line in fitted_words:
            linestring = ''
            for word in line:
                if word == line[-1]:
                    linestring += word
                else:
                    linestring += (word + " ")
            linestring += "\n"
            new_file.write(linestring)
    elif charscount < limit: # if fits more words
        continue
        # get the first word from the next line
        # throw it at the and of this
