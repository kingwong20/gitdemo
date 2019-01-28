
#prints hello

import utils

@utils.benchmark
def say_hi():
    print("hello dior!")

if __name__== "__main__":
    say_hi()


