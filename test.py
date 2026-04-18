import subprocess
from collections import defaultdict, Counter

def run_git_command(command):
    result = subprocess.run(
        args=command, 
        stdout=subprocess.PIPE, 
        text=True
    )
    return result.stdout


def count_total_commits():
    output = run_git_command(["git", "log", "--oneline"])
    return len(output.strip().split("\n"))
    
def commits_per_author():
    output = run_git_command(["git", "log", "--pretty=format:%an"])
    print(output)
    return Counter(output.split("\n"))


print(commits_per_author())
