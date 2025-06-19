import schedule
import time

def reminder_coding():
    print("Do Coding..!")

def main():
    schedule.every(30).minutes.do(reminder_coding)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()