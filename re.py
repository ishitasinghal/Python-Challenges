#A list is to be printed containing only valid email addresses in lexicographical order.

#Code
#Just a one liner using regular expressions.

def fun(s):
    return(bool(re.findall(r'^[\w_-]+@[a-zA-Z0-9]+\.[\w]{0,3}$', s)))
  
