# -*-coding:utf-8 -*

def binary(n):
    bin = list()
    while n > 0:
        q = n // 2
        r = n % 2
        bin.append(r)
        n = q

    return bin


if __name__ == '__main__':
    binar = binary(4)
    print(binar)
