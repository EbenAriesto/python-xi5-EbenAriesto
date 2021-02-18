my_str = "Kasur ini rusak"

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("Kalimat ini adalah palindrome")
else:
    print("Kalimat ini bukan palindrome")