from multiprocessing import Pool
import time

def square(x):
    print(f"Starte: {x}")
    time.sleep(1)
    return x * x

def main():
    numbers = [1, 2, 3, 4, 5]

    # Starte einen Pool mit 3 Prozessen
    with Pool(processes=3) as pool:
        result = pool.map(square, numbers)

    print("Squared numbers: ", result)

if __name__ == "__main__":
    main()