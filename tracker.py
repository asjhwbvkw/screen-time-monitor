import time
import datetime

DATA_FILE = "data.txt"

def save_time(minutes):
    today = datetime.date.today().isoformat()
    line = f"{today}: {minutes} minutes\n"

    with open(DATA_FILE, "a") as f:
        f.write(line)

def main():
    print("Tracking started... (Press CTRL + C to stop)")
    start = time.time()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        end = time.time()
        minutes = round((end - start) / 60, 2)
        print(f"\nSession: {minutes} minutes")
        save_time(minutes)
        print("Saved to data.txt")

if __name__ == "__main__":
    main()
