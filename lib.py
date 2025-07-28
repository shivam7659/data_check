import os

# Silent git command execution for GitHub Actions (Linux)
def silent_git(cmd):
    return os.system(f"git -c advice.detachedHead=false {cmd} > /dev/null 2>&1")

# Get PR branch content
with open('usecase.conf', 'r') as file:
    pr_content = file.read()

# Switch to main branch silently
silent_git("fetch origin main")
silent_git("checkout origin/main -b temp_main")

# Get main branch content
with open('usecase.conf', 'r') as file:
    main_content = file.read()

# Clean up (switch back to PR branch)
silent_git("checkout -")

# Print results cleanly
print("PR Branch Config:")
print(pr_content)
print("\nMain Branch Config:")
print(main_content)
