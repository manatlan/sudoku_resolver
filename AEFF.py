#!/usr/bin/python3
ll=[]
for i in open("grids.txt"):
    assert len(i.strip())==81
    ll.append( i.strip() )

all=[]
with open("grids2.txt","w+") as fid:
    for i in ll:
        if i not in all:
            all.append(i)
            fid.write(i+"\n")
