import itertools
import time

def main():
    print("\nWARNING! If you try to generate too many words", \
             "your system will not respond until it is finished.\n" \
             "\nTo exit: CTRL + C\n")
    chrs = str(input("Enter Characters: "))
    while True:
        try:
            min_length = int(input("Enter min lenght: "))
            max_length = int(input("Enter max lenght: "))
            break
        except ValueError:
            print("Invalid input!")

    count = 0
    start_time = time.time()
    file = open("wordlist.txt", "w")
    try:
        for lenght in range(min_length, max_length+1):
            for letters in itertools.product(chrs, repeat=lenght):
                file.write((''.join(letters))+"\n")
                count += 1
        print("{} words were generated in {}s."
              .format(count, round((time.time() - start_time),4)))
    except KeyboardInterrupt:
        print("Aborted by the user! {} words were generated in {}s."
              .format(count, round((time.time() - start_time),4)))
    finally:
        file.close()

if __name__ == '__main__':
    main()
