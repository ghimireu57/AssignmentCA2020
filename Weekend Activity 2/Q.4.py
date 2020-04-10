#4. Write a program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_alphabet():
    x=input('please enter a word you want to sort with hyphen')
    y=x.split('-')
    y.sort()
    print('-'.join(y))

sort_alphabet()
