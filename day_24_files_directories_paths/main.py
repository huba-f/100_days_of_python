# with open("my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file:
#     file.write("new Text.")

# with open("my_file.txt", mode="a") as file:
#     file.write("new Text.")
#

# with open("new_file.txt", mode="w") as file:
#     file.write("new Text.")

with open("../day_24_files_directories_paths/mail-merge-project-end/Input/Names/invited_names.txt", mode='r') as file:
    print(file.readlines())
