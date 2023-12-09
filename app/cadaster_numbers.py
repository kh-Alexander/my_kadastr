
def cadaster():
    # b = ObjectRequest()
    cadaster = open('cadasters').read().split()
    print(cadaster)
    cadaster_s = []
    for i in cadaster:
        x = i
        cadaster_s.append(x)
        if i == 'finish':
            break
    cadasters = cadaster_s[:-1]
    return cadasters


if __name__ == '__main__':
    cadaster()
