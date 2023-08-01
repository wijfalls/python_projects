
import os

def get_unique_filename(filename):
    """
    Function to generate a unique filename based on the input filename. 

    :param filename: The original filename.
    :return: A unique filename. If the original filename doesn't exist, it's returned as is.
    """

    if not os.path.exists(filename):
        return filename

    base, extension = os.path.splitext(filename)
    counter = 1

    while os.path.exists(filename):
        filename = f"{base}_{counter}{extension}"
        counter += 1

    return filename


def choose_file():
     # Get the current working directory
    working_directory = os.getcwd()
    # Get a list of all files in the working directory
    files = [f for f in os.listdir(working_directory) if os.path.isfile(os.path.join(working_directory, f))]

    # Print the files with their associated numbers
    print("What file would you like to summarize? (input the number to the right of your choice)")
    for i, file in enumerate(files, 1):
        print(f"{i} | {file}")

    # Get the user's choice
    choice = int(input("Enter your choice: ")) - 1  # subtract 1 because list indices start at 0

    # Check if the user's choice is valid
    if 0 <= choice < len(files):
        return files[choice]
    else:
        print("Invalid choice")
        return None

def ensure_directory_exists(directory_path):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            # If it doesn't exist, create it
            os.makedirs(directory_path)
            print(f"Directory {directory_path} created.")
        else:
            print(f"Directory {directory_path} already exists.")
    except OSError as e:
        # If an OSError occurred (e.g., due to incorrect permissions), print a helpful error message
        print(f"Error: Failed to create directory {directory_path} due to an operating system error.")
        print(f"Details: {e}")
