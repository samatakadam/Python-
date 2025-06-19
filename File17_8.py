import schedule, time

def check_mail():
    print("Checking mail...")

def main():
    schedule.every(10).seconds.do(check_mail)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()