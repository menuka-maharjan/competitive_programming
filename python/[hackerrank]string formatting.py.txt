def print_formatted(number):
    x = len(bin(number)[2:])
    for i in range(1,number+1):
        o = oct(i)[2:]
        h = hex(i)[2:]
        h = h.upper()
        b = bin(i)[2:]
        d = str(i)
        print(d.rjust(x),o.rjust(x),h.rjust(x),b.rjust(x))



