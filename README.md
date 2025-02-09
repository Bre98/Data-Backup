# Automatic Data Backup System

## Overview

The Automatic Data Backup System is a Python-based tool designed to automate the process of backing up critical data on Ubuntu systems. By leveraging rsync for efficient file synchronization and cron for scheduling, this program ensures that your important files are safely backed up to a designated location at regular intervals, without the need for manual intervention.
Features

- User-defined Backup Scheduling: Allows users to specify the frequency of backups according to their needs.
- Immediate and Scheduled Backups: Supports both immediate backups and the automatic scheduling of future backups.
- Flexible Source and Destination Paths: Users can define custom paths for the source (data to be backed up) and destination (backup storage location).
- Timestamped Backup Folders: Creates uniquely timestamped folders for each backup session for easy organization and retrieval.

## Getting Started
### Prerequisites

- Ubuntu operating system (or any Unix-like system with cron and rsync).
- Python 3.x installed.

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Bre98/Data-Backup.git
   ```
2. Navigate to the project directory:

   ```
    cd Data-Backup
   ```

### Usage

To use the Automatic Data Backup System, you will need to run the backup.py script with three command-line arguments: the source directory, the destination directory, and the cron frequency for scheduled backups.

```
python3 backup.py <source_directory> <destination_directory> <cron_frequency>
```

- <source_directory>: The directory you want to back up (e.g., /home/user/documents).
- <destination_directory>: The directory where you want the backups to be stored (e.g., /mnt/backup_drive/documents_backup).
- <cron_frequency>: How often you want the backup to run. This is specified in the standard cron format (e.g., @daily, 0 * * * * for every hour).

Example:

To back up the /home/user/documents directory to /mnt/backup_drive/documents_backup every day, you would run:

```
python3 backup.py /home/user/documents /mnt/backup_drive/documents_backup @daily
```

### Setting Up Cron Jobs

The script automatically sets up a cron job based on the frequency specified. No additional steps are required for scheduling after running the script with the appropriate arguments.

## Troubleshooting

- Ensure that cron and rsync are installed on your system.
- Verify that the source and destination directories exist and that you have the necessary permissions to access them.
- If backups are not occurring as scheduled, check the cron job setup by running `crontab -l`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or have identified a bug.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
