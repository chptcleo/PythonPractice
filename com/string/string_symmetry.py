if __name__ == "__main__":
    print "start"
    my_str = "abcdedcba"
    str_length = len(my_str)
    half_length = str_length / 2
    is_symmety = False
    for i in range(str_length):
        if i == half_length:
            is_symmety = True
            break
        if my_str[i] == my_str[str_length - 1 - i]:
            continue
        else:
            break
    print is_symmety
    print "end"
