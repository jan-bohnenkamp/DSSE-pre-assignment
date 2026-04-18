# Important
# Forgetting text=True → you get bytes instead of strings
# Not stripping output → extra empty lines break logic
# Assuming every line is valid → git log --numstat includes commit metadata lines


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
    return dict(Counter(output.split("\n")))

def file_change_stats():
    output = run_git_command(["git", "log", "--numstat"]) 
    lines = output.strip().split("\n")

    file_counts = defaultdict(int)
    total_added = 0
    total_removed = 0

    for line in lines:
        parts = line.split("\t")
        if len(parts) == 3:
            added, removed, filename = parts
            
            # handle binary files marked with "-"
            if added.isdigit() and removed.isdigit():
                total_added += int(added)
                total_removed += int(removed)
            
            file_counts[filename] += 1

    return file_counts, total_added, total_removed

def most_modified_file(file_counts):
    return max(file_counts, key=file_counts.get)


if __name__ == "__main__":

    print(f"Total commits: {count_total_commits()}")

    print(f"\nCommits per author: {commits_per_author()}")

    file_counts, added, removed = file_change_stats()
    print(f"\nMost modified file: {most_modified_file(file_counts)}") 
    print(f"Total lines added: {added}")
    print(f"Total lines removed: {removed}")
