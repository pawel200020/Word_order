class Data:
    words = list()
    quantity = list()


if __name__ == '__main__':
    quantity = int(input())
    data = Data
    for i in range(quantity):
        a = input()
        if a not in data.words:
            data.words.append(a)
            data.quantity.append(1)
        else:
            c = data.words.index(a)
            data.quantity[c] += 1
    print(len(data.words))
    for i in data.quantity:
        print(i, end=" ")
