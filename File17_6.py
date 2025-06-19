import schedule, time

def lunch_reminder():
    print("Lunch Time!")

def wrap_up_reminder():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch_reminder)
    schedule.every().day.at("18:00").do(wrap_up_reminder)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()