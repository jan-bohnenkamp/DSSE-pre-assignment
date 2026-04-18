import subprocess
from collections import defaultdict

def run_git_command(command):
    result = subprocess.run(
        args=command, 
        stdout=subprocess.PIPE, 
        text=True
    )
    return result.stdout


def count_total_commits():
    output = run_git_command(["git", "log", "--oneline"])
    


print(run_git_command(["git", "status"]))



