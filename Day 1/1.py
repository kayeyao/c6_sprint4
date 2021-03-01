from time import sleep

import random

def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def main():
    print('a')
    delay(seconds=3)
    print('b')

if __name__ == "__main__":
    main()

def main():
    for i in range(5):
        print(i)
        delay(seconds=i)    

if __name__ == "__main__":
    main()