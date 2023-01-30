import os
import hashlib
import sys


def fill_string(string, length):
    return string.ljust(length)


def get_hash(file_path):
    """Get the hash of a file"""
    try:
        with open(file_path, 'rb') as file:
            return hashlib.sha256(file.read()).hexdigest()
    except FileNotFoundError:
        return None


def write_array_to_file(file_path, array):
    folder_name = os.path.dirname(file_path)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(file_path, 'w') as file:
        for item in array:
            file.write(str(item) + "\n")


if __name__ == "__main__":
    # The path of the two folders you want to compare
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]

    # Create an empty list to store the different files
    diff_files = []
    same_files = []
    try:
        print(f"Start comparison between {folder1} and {folder2}")
        # Iterate through all the files in both folders
        for root, dirs, files in os.walk(folder1):
            for file in files:
                # Get the full file path
                file_path1 = os.path.join(root, file)
                file_path2 = os.path.join(
                    folder2, os.path.relpath(file_path1, folder1))
                # Compare the hashes of the files
                if get_hash(file_path1) != get_hash(file_path2) and get_hash(file_path2) != None:
                    diff_files.append(
                        f"""{fill_string(file_path1, 200)} => hash({get_hash(file_path1)}, {get_hash(file_path2)})""")
                elif (get_hash(file_path1) == get_hash(file_path2) and get_hash(file_path2) != None):
                    same_files.append(
                        f"""{fill_string(file_path1, 200)} => hash({get_hash(file_path1)}, {get_hash(file_path2)})""")
        print("End comparison")
        # Save the list of different files to a file
        write_array_to_file("./result/notsame.txt", diff_files)

        # Save the list of different files to a file
        write_array_to_file("./result/same.txt", same_files)

        print("finished")
    except Exception as error:
        print(error)
