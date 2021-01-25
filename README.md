# Marriage_Affair

Marriage-Affair Prediction deployment URL: https://marriage-affairs.herokuapp.com/

## Introduction
#### In this project we will build a classifiacation model where according to different features we can tell if a women will be having any extra marital affairs.
#### The dataset used has 9 columns that we will divide into 8 features and 1 target column
***The Columns are Given as:***

- Rate_marriage: Women’s rating for her marriage
- Age: Women's Age
- Years_Married: Number of years married
- Children: Number of Children She has
- Religious: On the scale of 1 -5 whether she believe in religion or not
- Education: Level of education of Women
- Occupation: Occupation of women
- Occupation_husb: Occupation of Husband
- Affairs: Will have extra marital affair or not(0: will have affair, 1: will not have affair)

### Instruction to run the file
***Step 1***
**Create and activate an environment**
- Using Conda <br>
conda create -n [your environment name] python=3.7 <br>
Then activate the environment by writing <br>
conda activate [your environment name] <br>

- Using default Environments <br>
python3 -m venv [your environment name] <br>
Then activate the environment by writing <br>
[your environment name]\Scripts\activate.bat [For windows users] <br>
source [your environment name]/bin/activate [For Mac/Ubuntu users] <br>

NOTE: you can give any python version and ignore brackets while giving environment name

***Step 2***
**Install Dependencies**
- For library installations  write <br>
pip install -r requirements.txt 

***Step 3***
**Run The File**
- To run the file write <br>
python app.py
