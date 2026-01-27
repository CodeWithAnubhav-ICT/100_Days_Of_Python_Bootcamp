# word_per_page = 0
# pages = int(input("Number of pages: "))               Bugged code
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

"""
print() is your friend.
It can help expose hidden values while your code is running.
you can use print to expose those intermediate values
and help you debug your code.
"""

word_per_page = 0
pages = int(input("Number of pages: "))                 # Debugged code
print(pages)
print(word_per_page)
word_per_page = int(input("Number of words per page: "))
print(pages)
print(word_per_page)
total_words = pages * word_per_page
print(total_words)
