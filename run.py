import subprocess

repo_dir = r"c:\Users\PC\Desktop\ADVANCE AI\WEEK 12 AUTOMATION"

subprocess.run(
    ["git", "config", "--global", "user.name", "ADVANCE AI"],
    cwd=repo_dir,
    check=True,
)
subprocess.run(
    ["git", "config", "--global", "user.email", "eunice.akande@gmail.com"],
    cwd=repo_dir,
    check=True,
) 