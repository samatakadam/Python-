import schedule, time, shutil
from datetime import datetime

def backup():
    shutil.copy("file.txt", "backup_file.txt")
    with open("backup_log.txt", "a") as log:
        log.write(str(datetime.now()) + " - Backup done\n")

def main():
    schedule.every().hour.do(backup)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()