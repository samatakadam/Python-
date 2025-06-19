import schedule, time
from datetime import datetime

def main():
    schedule.every(1).minutes.do(lambda: print(datetime.now()))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()