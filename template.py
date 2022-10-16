import os

#creating directories/folders for the project
directories = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
    "data_given"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, ".gitkeep"), "w") as f:
        pass

#creating files needed to start the project

files = [
    "dvc.yaml",  # records stages of the projects that needs to be tracked
    "params.yaml", #records all the steps of the process
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file in files:
    with open(file, "w") as f:
        pass
