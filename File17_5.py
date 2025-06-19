import schedule, time
from datetime import datetime

def write_time():
    with open("Marvellous.txt", "a") as f:
        f.write(str(datetime.now()) + "\n")

def main():
    schedule.every(5).minutes.do(write_time)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
