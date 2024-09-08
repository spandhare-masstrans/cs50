def main():
    while True:
        try:
            percentage = convert(input())
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    a,b = fraction.split('/')
    x, y=int(a), int(b)
    if y==0:
        raise ZeroDivisionError
    elif y<x:
        raise ValueError
    return int(round((x/y)*100))

def gauge(percent):
    if percent <= 1:
        return'E'
    elif percent >= 99:
        return'F'
    else:
        return str(percent)+'%'


if __name__ == "__main__":
    main()
