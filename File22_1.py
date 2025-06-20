
import os, sys, time, hashlib, argparse, smtplib, ssl
from datetime import datetime
from email.message import EmailMessage

def calc_hash(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None

def remove_dups(dir, log):
    seen = {}
    total = 0
    removed = 0
    log.write(f"Start scan: {dir}\n")
    for root, _, files in os.walk(dir):
        for f in files:
            total += 1
            fp = os.path.join(root, f)
            h = calc_hash(fp)
            if h and h in seen:
                try:
                    os.remove(fp)
                    removed += 1
                    log.write(f"Removed duplicate: {fp}\n")
                except Exception as e:
                    log.write(f"Error removing {fp}: {e}\n")
            else:
                seen[h] = fp
    log.write(f"Finished. Scanned {total} files, removed {removed} duplicates.\n")
    return total, removed

def send_mail(to, subj, body, file_path):
    msg = EmailMessage()
    msg["Subject"] = subj
    msg["From"] = "you@example.com"
    msg["To"] = to
    msg.set_content(body)
    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(file_path))
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
        s.login("you@example.com", "app_password")
        s.send_message(msg)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("directory")
    p.add_argument("interval", type=int)
    p.add_argument("email")
    args = p.parse_args()
    if not os.path.isdir(args.directory):
        print("Invalid directory", file=sys.stderr); sys.exit(1)

    time.sleep(args.interval * 60)

    os.makedirs("Marvellous", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfn = os.path.join("Marvellous", f"log_{ts}.txt")
    with open(logfn, "w") as log:
        total, removed = remove_dups(args.directory, log)

    body = (f"Scan started: {ts}\n"
            f"Total files scanned: {total}\n"
            f"Duplicates removed: {removed}\n")
    send_mail(args.email, "Duplicate Removal Report", body, logfn)

if __name__ == "__main__":
    main()
