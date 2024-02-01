import subprocess

# Function to run git commands
def run_git_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode('utf-8')}")
    return output.decode('utf-8')

# Main function
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
