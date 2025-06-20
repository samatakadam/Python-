

import sys, os, psutil, logging, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def parse_args():
    if len(sys.argv) != 3 or not sys.argv[1].strip() or not sys.argv[2].strip():
        print("Usage: ProcInfoLog.py <DirectoryName> <EmailAddress>")
        sys.exit(1)
    return sys.argv[1].strip(), sys.argv[2].strip()

def ensure_directory(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            print(f"Error: could not create directory '{dir_name}': {e}")
            sys.exit(1)

def setup_logger(log_path):
    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format="%(asctime)s: %(message)s")
    return logging.getLogger()

def gather_processes():
    procs = []
    for p in psutil.process_iter(['name', 'pid', 'username']):
        try:
            info = p.info
            procs.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procs

def log_processes(logger, processes):
    if not processes:
        logger.info("No running processes found.")
    for p in processes:
        logger.info(f"Process - Name: {p.get('name','')}   PID: {p.get('pid','')}   User: {p.get('username','')}")

def send_email_with_attachment(sender, password, recipient, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(attachment_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)
    except Exception as e:
        print(f"Error reading attachment: {e}")
        return

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    dir_name, email_to = parse_args()
    ensure_directory(dir_name)

    log_file = os.path.join(dir_name, "procinfo.log")
    logger = setup_logger(log_file)

    procs = gather_processes()
    log_processes(logger, procs)

   
    sender_email = "youremail@gmail.com"
    sender_password = "your-app-password"

    subject = f"Process Info Log from '{dir_name}'"
    body = f"Hi,\n\nPlease find attached the process log file '{os.path.basename(log_file)}'."

    send_email_with_attachment(sender_email, sender_password, email_to, subject, body, log_file)
    print(f"Done! Log saved to '{log_file}' and emailed to '{email_to}'.")

if __name__ == "__main__":
    main()
