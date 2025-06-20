
import argparse, logging, os, sys
import psutil

LOG_FILE = "procinfo.log"

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )
    return logging.getLogger()

def parse_args():
    p = argparse.ArgumentParser(description="Display running processes info")
    p.add_argument("-f", "--file", help="file with process names (one per line)")
    p.add_argument("names", nargs="*", help="process names to filter")
    return p.parse_args()

def load_names_from_file(path, logger):
    if not os.path.isfile(path):
        logger.error(f"Filter file not found: {path}")
        sys.exit(1)
    names = []
    try:
        with open(path) as f:
            names = [ln.strip() for ln in f if ln.strip()]
    except Exception as e:
        logger.error(f"Error reading file {path}: {e}")
        sys.exit(1)
    return names

def gather_processes(filter_names, logger):
    procs = []
    try:
        for p in psutil.process_iter(['pid', 'name', 'username']):
            info = p.info
            if not filter_names or info.get('name') in filter_names:
                procs.append(info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        logger.warning(f"Issue reading process info: {e}")
    return procs

def log_processes(proc_list, logger):
    if not proc_list:
        logger.info("No processes found matching criteria.")
    for info in proc_list:
        name = info.get('name', 'N/A')
        pid = info.get('pid', 'N/A')
        user = info.get('username', 'N/A')
        logger.info(f"Name={name} PID={pid} User={user}")

def main():
    logger = setup_logger()
    args = parse_args()

    filters = []
    if args.file:
        filters = load_names_from_file(args.file, logger)
    elif args.names:
        filters = args.names

    processes = gather_processes(filters, logger)
    log_processes(processes, logger)

if __name__ == "__main__":
    main()
