## IMPLEMENTATION

1. Create a virtual environment
```
conda create -n winequality python = 3.7 -y
```
2. Activate the environment
```
conda activate winequality
```
3. Create requirements.txt file to keep track of the packages needed for the project:
- dvc
- dvc[gdrive]
- sklearn
4. Run requirements.txt
```
pip install -r requirements.txt
```
5. Create 'template.py' file to build the directories and files needed for the project.

6. Download the dataset : https://bit.ly/3TmpoPC
7. Initiate local repository
```
git init
```
8. Initiate dvc to start tracking your progress. This will create '.dvcignore' file
```
dvc init
```
9. Make sure the downloaded dataset is in 'data_given' directory/folder.

10. Initiate dvc to track and the dataset.
```
dvc add data_given/winequality.csv
```
11. Commit and push untracked files into our local repository.
```
git add . && git commit -m "initial commit"
```