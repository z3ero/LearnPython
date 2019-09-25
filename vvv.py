nums=list(map(int,input().strip().split(' ')))
res=0
stack=[nums]
pro=[1]
while stack:
    # print(stack)
    # print(pro)
    tmp=stack.pop(0)
    if tmp[0] or tmp[1]:
        tmppro=pro.pop(0)
        res+=tmp[0]/(tmp[0]+tmp[1])*tmppro
        tmpa=tmp[1]/(tmp[0]+tmp[1])*tmppro
        if tmp[1]>0 and tmp[0]>0:
            if tmp[0]>1 and tmp[1]>=2:
                stack.append((tmp[0]-1,tmp[1]-2))
                tmpabc=tmpa*((tmp[1]-1)/(tmp[0]+tmp[1]-1))*(tmp[0]/(tmp[0]+tmp[1]-2))
                pro.append(tmpabc)
            if tmp[0]>0 and tmp[1]>=3:
                stack.append((tmp[0],tmp[1]-3))
                tmpabc=tmpa*((tmp[1]-1)/(tmp[0]+tmp[1]-1))*((tmp[1]-2)/(tmp[0]+tmp[1]-2))
                pro.append(tmpabc)

print('%.05f'%res)