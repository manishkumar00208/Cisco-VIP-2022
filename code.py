import re


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check(Ip):

    if (re.search(regex, Ip)):
        return True

    else:
        print("Invalid Ip address:", Ip)



if __name__ == '__main__':

    lst = []
    print("enter 10 IPv4 addresses")

    for i in range(10):
        ip = input()

        if check(ip) == True:

            dec = ip.split(".")
            dec = list(map(int, dec))
            dec = dec[0] * (256 ** 3) + dec[1] * (256 ** 2) + dec[2] * (256 ** 1) + dec[3]

            lst.append(dec)
            lst.append(bin(dec))
            lst.append(oct(dec))
            lst.append(hex(dec))

    with open('conversion.txt', 'w+') as f:

        for items in lst:
            f.write('%s\n' % items)
    f = open('conversion.txt', 'r')

    print("The first IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The second IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The third IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The fourth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The fifth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The sixth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The seventh IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The eighth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The ninth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip())
    print("The tenth IP address in Decimal, Binary, Octal and hexadecimal format is", f.readline().strip(),  f.readline().strip(), f.readline().strip(), f.readline().strip())
    f.close()