from github import Github
import os
import subprocess

# Authenticate with GitHub
token = os.getenv('GH_TOKEN')  # Store your token in an environment variable
g = Github(token)

# Get the repository
repo_name = "marcelstancu/test"  # Replace with your repository name
repo = g.get_repo(repo_name)

# Get pull requests
pulls = repo.get_pulls(state='open', sort='created', base='main')

for pr in pulls:
    print(f"Checking PR #{pr.number}: {pr.title}")

    # Check if the pull request contains Python files
    files = pr.get_files()
    contains_python_code = any(file.filename.endswith('.py') for file in files)

    if not contains_python_code:
        print(f"PR #{pr.number} does not contain Python code. Skipping...")
        continue

    # Clone the pull request locally
    pr_branch = pr.head.ref
    repo_url = pr.head.repo.clone_url
    subprocess.run(["git", "clone", repo_url])
    subprocess.run(["git", "checkout", pr_branch], cwd=repo_name)

    # Run pylint or flake8 to check for errors
    result = subprocess.run(["pylint", repo_name], capture_output=True, text=True)
    errors = result.stdout

    if errors:
        print(f"Errors found in PR #{pr.number}:")
        print(errors)

        # Create a new branch for fixes
        fix_branch = f"fixes/{pr_branch}"
        subprocess.run(["git", "checkout", "-b", fix_branch], cwd=repo_name)

        # Apply fixes (this part is manual or requires additional logic to automate)
        # For demonstration, let's assume fixes are applied

        # Commit and push changes
        subprocess.run(["git", "add", "."], cwd=repo_name)
        subprocess.run(["git", "commit", "-m", "Fix Python errors"], cwd=repo_name)
        subprocess.run(["git", "push", "origin", fix_branch], cwd=repo_name)

        # Create a new pull request with the fixes
        repo.create_pull(
            title=f"Fixes for PR #{pr.number}",
            body="Automated fixes for Python errors",
            head=fix_branch,
            base=pr_branch
        )

    # Clean up cloned repo
    subprocess.run(["rm", "-rf", repo_name])

print("Completed checking pull requests.")
