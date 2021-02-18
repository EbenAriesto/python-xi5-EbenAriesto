# dengan dictionary
vowels = "aeiou"

ip_str = "Halo nama saya Sopan Setiawan, saya sedang belajar python"

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)