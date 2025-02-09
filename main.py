import os
import sys
import subprocess
from datetime import datetime

# Function to create a backup
def backup_data(source, destination):
    # Creating a timestamp for the backup folder
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_folder = os.path.join(destination, "backup-" + timestamp)
    
    try:
        # Checking if the source directory exists
        if not os.path.exists(source):
            raise Exception("Source directory does not exist.")
        
        # Creating the backup folder
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        
        # Running the rsync command to backup data
        subprocess.run(["rsync", "-av", source, backup_folder], check=True)
        print(f"Backup successful. Data from {source} has been backed up to {backup_folder}")
    except Exception as e:
        print(f"Error: {e}")

# Function to setup automatic backups using cron jobs
def setup_cron_job(source, destination, frequency):
    cron_command = f"{frequency} /usr/bin/python3 {os.path.realpath(__file__)} {source} {destination}\n"
    try:
        # Capture the existing crontab
        existing_cron_jobs = subprocess.run(["crontab", "-l"], check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        # No crontab for user
        existing_cron_jobs = ""

    # Write the existing + new cron command to mycron
    with open("mycron", "w") as cronfile:
        cronfile.write(existing_cron_jobs)
        cronfile.write(cron_command)

    # Install the new crontab
    subprocess.run(["crontab", "mycron"], check=True)
    
    print("Cron job setup complete.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 backup.py <source_directory> <destination_directory> <cron_frequency>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    cron_frequency = sys.argv[3]

    # First, perform an immediate backup
    backup_data(source_dir, destination_dir)
    
    # Then, setup the cron job for automatic backups
    setup_cron_job(source_dir, destination_dir, cron_frequency)
