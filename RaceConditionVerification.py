from concurrent.futures import ThreadPoolExecutor
from Counter import Counter

def main() -> None:
    for i in range(100):
        increment_count()

def increment_count():
    counter = Counter()
    print(f"The count is {counter.count}")
    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(counter.increment)
        f2 = executor.submit(counter.increment)

        while True:  # simulate a do ... while loop in Python
            if f1.done() and f2.done():
                print(f"The resulted count is {counter.count}")
                if counter.count % 2 != 0:
                    print(f"Race condition detected!!!")
                break

if __name__ == "__main__":
    main()