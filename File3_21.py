

import sys
import os
import logging
import psutil

def setup_logging(directory):
    """Configure logging to a file inside the given directory."""
    log_path = os.path.join(directory, "procinfo.log")
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s: %(message)s"
    )
    return logging.getLogger()

def create_directory(dir_name):
    """Create a directory if it doesn't already exist."""
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            print(f"Error: could not create directory '{dir_name}': {e}")
            sys.exit(1)

def gather_process_info():
    """Return a list of dicts containing name, pid, and username of running processes."""
    processes = []
    for proc in psutil.process_iter(['name', 'pid', 'username']):
        try:
            info = proc.info
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def log_processes(logger, processes):
    """Write each process's name, PID, and username to the log."""
    if not processes:
        logger.info("No running processes found!")
    else:
        for p in processes:
            name = p.get('name') or "N/A"
            pid = p.get('pid') or "N/A"
            user = p.get('username') or "N/A"
            logger.info(f"Process ‑ Name: {name}, PID: {pid}, User: {user}")

def main():
   
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        print("Usage: ProcInfoLog.py <DirectoryName>")
        sys.exit(1)

    dir_name = sys.argv[1].strip()
   
    create_directory(dir_name)

   
    logger = setup_logging(dir_name)

  
    procs = gather_process_info()

   
    log_processes(logger, procs)

if __name__ == "__main__":
    main()
