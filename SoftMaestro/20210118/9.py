case = 1
while True:
    l,p,v = map(int,input().split())
    if l==0 and p ==0 and v==0:
        break
    if (v%p) < l:
        use = (v//p)*l + (v%p)
        print('Case '+str(case)+': '+str(use))
    else:
        use = (v//p)*l + l
        print('Case '+str(case)+': '+str(use))
    case += 1

