import ex25_even_more_practice as ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print(f"break_words:{words}")

sorted_words = ex25.sort_words(words)
sorted_words
print(f"sorted_words:{sorted_words}")

ex25.print_first_word(words)
ex25.print_last_word(words)
words

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words

sorted_words = ex25.sort_sentence(sentence)
sorted_words
print(f"sort_sentence:{sorted_words}")

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)