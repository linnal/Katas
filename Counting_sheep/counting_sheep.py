def main():
    f_out = open("output_large.txt", "w")
    with open("input_large.txt") as f:
        for i,line in enumerate(f):
            if i>0:
                f_out.write("Case #{}: {}\n".format(i, last_nr_seen(int(line))))

    f_out.close()
    return


def insomnia(n):
    return n == 0

def get_number(nr):
    seen_nr = [False] * 10
    index = 1
    while True:
        mult = index * nr
        res =  map(int, list(str(mult)))
        for elem in res:
            if not seen_nr[elem]:
                seen_nr[elem] = True
        if False not in seen_nr: 
            break
        index+=1
    return mult


def last_nr_seen(nr):
    if insomnia(nr):
        return "INSOMNIA"
    return get_number(nr)





if __name__ == '__main__':
    main()
