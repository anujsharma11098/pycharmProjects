def magic_number(num):
    num_str=str(num)
    odd_sum=0

    for i in num_str:
        i = int(i)
        if i%2 == 1:
            odd_sum+=i

    print(odd_sum)

magic_number(785432965)