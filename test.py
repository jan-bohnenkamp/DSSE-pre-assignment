
from pydriller import Repository

repo_path  = "jclouds"
repo = Repository(repo_path)
issues = ["JCLOUDS-27", "JCLOUDS-43", "JCLOUDS-276", "JCLOUDS-435", "JCLOUDS-1548"]


### Matching commits to the issues

matching_commits = set()

for commit in repo.traverse_commits():
    msg = commit.msg.upper()

    for issue in issues:
        if issue in msg:
            matching_commits.add(commit.hash)
            break

print(f"Total issue-related commits: {len(matching_commits)}")


### Average Unique Files changed

total_files_changed = 0
total_commits = 0

for commit in repo.traverse_commits():

    msg = commit.msg.upper()

    if any(issue in msg for issue in issues):
        total_files_changed += commit.files
        total_commits += 1

average = total_files_changed / total_commits if total_commits > 0 else 0

print(f"Average number of files changed: {average}")


### Average DMM Metrics

total_dmm = 0
count = 0

for commit in repo.traverse_commits():

    msg = commit.msg

    if any(issue in msg for issue in issues):

        files_changed = commit.files
        churn = commit.insertions + commit.deletions

        dmm = churn + files_changed

        total_dmm += dmm
        count += 1

average_dmm = total_dmm / count if count > 0 else 0

print(f"Average DMM metrics: {average_dmm}")


