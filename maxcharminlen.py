NO_OF_CHARS = 256
def diffchars(str, n): 
	count = [0] * NO_OF_CHARS 
	for i in range(n): 
		count[ord(str[i])] += 1
	max_distinct = 0
	for i in range(NO_OF_CHARS): 
		if (count[i] != 0): 
			max_distinct += 1	
	return max_distinct 

def smallesteSubstr_maxDistictChar(str): 
	n = len(str)
	max_distinct = diffchars(str, n) 
	minl = n 
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_length = len(subs) 
			sub_distinct_char = diffchars(subs, subs_length) 
			if (subs_length < minl and max_distinct == sub_distinct_char): 
				minl = subs_length 
	return minl 
str = "abcda"

l = smallesteSubstr_maxDistictChar(str); 
print(l) 
