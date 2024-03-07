import subprocess

def run_git_command(command):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Command executed successfully!")
        print("Output:")
        print(result.stdout)
    else:
        print("Error executing command!")
        print("Errors:")
        print(result.stderr)

def main():
    # Ask for commit message
    commit_message = input("Enter your commit message: ")

    # Git add command
    run_git_command("git add .")

    # Git commit command
    run_git_command(f"git commit -m \"{commit_message}\"")

    # Git push command
    run_git_command("git push")

if __name__ == "__main__":
    main()
