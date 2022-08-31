import os
import subprocess
import sys

args = sys.argv[1].split(" | ")
only_version = args[1]

print("Configuring git ...")
subprocess.run("git", "config", "--global", "user.email", os.environ['GIT_EMAIL'], check=True)
subprocess.run("git", "config", "--global", "user.email", os.environ['GIT_USERNAME'], check=True)
subprocess.run(["git", "pull"], check=True)
subprocess.run(["git", "checkout", "main"], check=True)

print("Tagging package version ...")
output = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], capture_output=True, check=True)
tag = output.stdout.decode("utf-8")
subprocess.run(["npm", "version", tag, "-m", f'"Release version: {tag}"'], check=True)
subprocess.run(["git", "push"], check=True)
print(f'Version {tag} tagged successfully')

if not only_version:
    print("Publishing package")
    subprocess.run(["npm", "publish"], check=True)
    print("Package published successfully")