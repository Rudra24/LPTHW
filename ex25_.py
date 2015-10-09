__author__ = 'rudragouda'

import ex25

sentence = "All good things come to those who wait."
print sentence
print "--------------------"

words = ex25.break_words(sentence)
print words
print "--------------------"
ex25.print_first_word(words)
ex25.print_last_word(words)
print words
print "--------------------"

sorted_words = ex25.sort_sentence(sentence)
print sorted_words
print "--------------------"
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print sorted_words
print "--------------------"
