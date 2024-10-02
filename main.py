if __name__ == '__main__':

#String slicing and indexing

    my_string = "Hello World"
    print(my_string)
    print(my_string[0])
    print(my_string[0:3])
    print(my_string[-2])

    my_string = "abcdefghijk"
    print(my_string[2:])
    print(my_string[:3])
    print(my_string[3:6])
    print(my_string[1:3])
    print(my_string[::2])
    print(my_string[::3])
    print(my_string[2:9:2])
    print(my_string[::-1])

#Immutability

    name = "Sam"
#We want to change it to "Pam"
    slice_name = name[1:]
    name_last_letters = name[0]
    name_last_letters = "P"
    print(name_last_letters + slice_name)

    x = "Hello World"
    x = x + " it's raining"
    print(x)

    x = "Hello World"
    print(x.upper())
    print(x.lower())
    print(x.split())
    print(x)