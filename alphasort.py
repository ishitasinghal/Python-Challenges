#Problem statement

# sort the string in the following manner:
#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.

n = ''.join(sorted(input()))
print(n)

