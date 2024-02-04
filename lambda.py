l=[3,4,5,6,7,8,9,10,11,12,14,18,17,16,15]


def list_gen(l , func):

    new_list=[]
    for i in l:
        if func(i):
            new_list.append(i)
    return new_list

even_list =list_gen(l,lambda i: i %2 == 0)
odd_list = list_gen(l,lambda i : i %2 != 0)

print (l)

print(even_list)

print(odd_list)