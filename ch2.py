string = "UDDDUDUU"
crt_lvl=valley=0
for i in string:
    if(i=='U'):
        crt_lvl=crt_lvl+1
    if(i=='D'):
        crt_lvl=crt_lvl-1

    if(crt_lvl==0 and i=='U'):
        valley=valley+1

print("Valleys are:", valley)
    
