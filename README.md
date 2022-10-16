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
12. Create a github repository to push all the code to the online repository. 'Since REAME.md' file has been created, ignore while creating the repo.
13. Paste the git remote link and press enter. This will create a master branch instead of main branch. Change it by :
```
git branch -M main
```
14. Add and push all the changes to github.
```
git add . && git commit -m "initial commit"
```
```
git push origin main
```
15. <p>In 'params.yaml' file, a base will be initiated where it will include the project name, random_state of the model, and the target column of the dataset/model. Also, the data source for which the data will be retrieved from will also initiated as a step. WHare to store the raw data retrived will also be initiated. From there, how the data will be splited, path of the training dataset, testing dataset, and the test size will be intiated and the paths where where these information will be initiated. The estimator which contains the algorithm used, and the parameters of the algorithm will be initiated. A model directory will be created to store the trained model. After that, push the codes to github.</p>

16. <p>Under 'src' folder, create a python file that will get the dataset based on the parameters given in the 'params.yaml' to distribute the each dataset to it destined directory as stated in 'params.yaml'. The name of this python file is 'get_data.py'. Inside 'get_data.py' file, import 'os', 'yaml' and 'pandas' to read the data. Make sure these packages/libraries are included and run in 'requirements.txt' file. An argument will be intitated as 'config' which will automatically be the path of the 'params.yaml'. Once 'config' is called, it automatically refelcts all the paths in 'params.yaml'. After this arguments has been created, it needs to be parsed.</p>
```
Run: 

python src/get_data.py
````