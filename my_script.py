# This library helps read and write the CSV files.
import csv

# This helps generate random passwords for each user account.
import secrets

# This calls the useradd command, which creates and adds each user account.
import subprocess

# This library helps to locate the data files for each user account.
from pathlib import Path # to locate the data files

cwd = Path.cwd()

with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
    reader = csv.DictReader(file_input)

writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames)
writer.writeheader()

for user in reader:
    user["password"] = secrets.token_hex(8)
    useradd_cmd = ["/sbin/useradd",
                    "-c", user["real_name"],
                    "-m",
                    "-G", "users",
                    "-p", user["password"],
                    user["username"]]
    subprocess.run(useradd_cmd, check=True)

writer.writerow(user)