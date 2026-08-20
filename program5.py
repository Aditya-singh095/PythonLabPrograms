import os
import sys


def show_directory(path):
    """Display files and folders in a directory."""
    try:
        items = os.listdir(path)

        print(f"\nContents of: {os.path.abspath(path)}")

        for item in items:
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                print("[DIR] ", item)
            else:
                print("[FILE]", item)

    except FileNotFoundError:
        print("Directory not found.")

    except PermissionError:
        print("Permission denied.")


def create_workspace(name):
    """Create a workspace directory."""
    try:
        os.makedirs(name, exist_ok=True)
        print(f"Workspace created: {os.path.abspath(name)}")

    except OSError as e:
        print("Could not create workspace:", e)


def list_extensions(path, extension):
    """List files having a specific extension."""
    try:
        print(f"\nFiles with extension '{extension}':")

        for item in os.listdir(path):
            if item.endswith(extension):
                print(item)

    except FileNotFoundError:
        print("Directory not found.")


def read_or_create_log(filename):
    """Safely read an existing log or create a new one."""
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print("\nLog contents:")
                print(file.read())
        else:
            with open(filename, "w") as file:
                file.write("New log file created.\n")

            print(f"Created new log: {filename}")

    except PermissionError:
        print("Permission denied while accessing the log.")

    except OSError as e:
        print("File error:", e)


def main():
    print("===== File Management Utility =====")

    # Command-line argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.getcwd()

    print("Current path:", os.path.abspath(path))

    # Show directory
    show_directory(path)

    # Create workspace
    workspace = os.path.join(path, "workspace")
    create_workspace(workspace)

    # List Python files
    list_extensions(path, ".py")

    # Create/read log
    log_file = os.path.join(workspace, "utility.log")
    read_or_create_log(log_file)


if __name__ == "__main__":
    main()
