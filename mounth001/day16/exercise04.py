tuple01=(4,5,66,7,2)
iterator=tuple01.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01={'小米':101,'小明':102,'小张':103}
iterator=dict01.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item,dict01[item])
    except StopIteration:
        break