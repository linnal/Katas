def main():
    f_out = open("output_large.txt", "w")
    with open("input_large.txt") as f:
        for i,line in enumerate(f):
            f_out.write("Case #{}: {}".format(i, extract_last_word(line)))
    f_out.close()
    return




def extract_last_word(word):
    result = ""
    for c in word:
        if len(result) == 0:
            result += c
        else:
            result = c + result if result[0] <= c \
                     else result + c
    return result




if __name__ == '__main__':
    main()
