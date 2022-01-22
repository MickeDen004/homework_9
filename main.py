import random


def alpha(*alphabet):
    """напишите функцию,
    которая умеет принимать любое количество Имен и формировать из них очередь в алфавитном порядке -
    на входе нефиксированное количество позиционных аргументов,
    а на выходе список очереди"""
    a = alphabet
    print(sorted(a, reverse=False))


alpha("Wisconsin", "Alabama", "Utah", "West Virginia", "North Carolina", "California", "Idaho")


# черновик
def alpha1(*alphabet):
    """напишите функцию,
    которая умеет принимать любое количество Имен и формировать из них очередь в алфавитном порядке -     на входе нефиксированное количество позиционных аргументов,
     а на выходе список очереди"""
    a = alphabet
    return sorted(a)


info = alpha1("Forest", "Winter", "Snow")
for item in range(len(info)):
    print(info[item], end="\n")


def file_function(*my_list):
    lines = my_list
    with open(r"C:\Users\nikit\Desktop\Python\Lessons and HW\Lesson 9 Hw\my_list.txt", "w") as file:
        for line in lines:
            file.write((line + "\n"))


file_function("Forest", "Winter", "Snow", "Python", "Deer", "Owl")


def dict_func(**dictionary):
    print({v: k for k, v in dictionary.items()})
    return


print(dict_func
          (C0="16.35",
          D0="18.35 Hz",
          E0="20.60 Hz",
          F0="21.83 Hz",
          G0="24.50 Hz",
          A0="27.50 Hz",
          B0="30.87 Hz"
          )
      )


def deck(x: int):
    s = [*range(x)]
    random.shuffle(s)
    print(s)


deck(57)
