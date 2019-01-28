
#prints hello

import utils

@utils.benchmark
def say_hi():
    print("hello EXVIVO!")

if __name__== "__main__":
    say_hi()


