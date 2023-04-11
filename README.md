# Machine learning in Banking dataset
In this project, we will try to give answers to a set of questions that may be relevant when analyzing banking data:

1.  What is the share of clients attracted in our source data?
2.  What are the mean values ​​of numerical features among the attracted clients?
3.  What is the average call duration for the attracted clients?
4.  What is the average age among the attracted and unmarried clients?
5.  What is the average age and call duration for different types of client employment?

In addition, we will make a visual analysis in order to plan marketing banking campaigns more effectively,and build machine learning model that will predict the share in given features.
## How to use the Project
To use this repo first, you need to clone it with this cammand below:
```
git clone https://github.com/otman-ai/Gender-Classification.git
```
After that you have to create install all the requirements:
```
pip3 install requirements.txt
```
To run the web application for prediction,go to the local directory ,runthe following command:

```
streamlit run app.py
```
in the repo you will find :
* `makeUniqueValues.py`:pyhton script that make the unique values of the object columns of the data,we use those values in the web application .
* `app.py`:the web application that implement the model
* `tabelMdBuilder.py`:python scrpit that build Markdown table,I use it to build the READM.md tables

* `Data Understanding.ipynb` witch is notebook I used to undersind the data  .
* `EDA.ipynb` python notebook for Exploratry data analysis ,I used this notebook to get the insight.
* `Model Building.ipynb` python notebook for model building prototype
* `tabelMDBuilding.py` python script to create markdown table 
* inside *matrix* folder there is :
* * `matrix.csv`:data in csv format for the matrix of the evaluation of the model
* inside *Report* folder there is :
* * `Report.pdf`:pdf report for all the useful insigh I extract from the data ,I create it using Power BI
* * `Report.pbitsv`:Power BI dashboard
* inside *model* folder there is :
* * `model_file.p`:the algorithm in pickle format that predict the label of a given features 
* inside *Dataset* folder there is :
* * `bank-additional-full.csv` with all examples, ordered by date (from May 2008 to November 2010).
* * `bank-additional.csv` with 10% of the examples (4119), randomly selected from bank-additional-full.csv.
* * `bank-additional-names.txt`:Txt file explains the columns of the dataset
* * `Report.pbit`:Power BI dashboard
* * `data.csv`:the cleaned data I used in model building

* inside *tables* folder there is :
* * `age_duration_by_job.csv`:table I exported to use in the report ,the table is pivot table of age and duration by job
* * `mean_features`:table I exported to use it in the report,the table is the mean values ​​of numerical features among the attracted client.

Project Lifecycle:
* [Business understanding Done](#business-understanding)
* [Data understanding Done](#data-understanding)
* [EDA Done](#eda)
* [Data Modeling Pipeline](#data-modeling-pipeline)
* [Model Evaluation](#model-evaluation)
* [Model Deployment](#model-deployment)
## Business understanding:
The binary classification goal is to predict if the client will subscribe a bank term deposit (variable y).

## Data understanding:
The zip file includes two datasets: 
  1) bank-additional-full.csv with all examples, ordered by date (from May 2008 to November 2010).
  2) bank-additional.csv with 10% of the examples (4119), randomly selected from bank-additional-full.csv.

Input variables:

* **bank client data:**
   
   `age` (numeric).

   `job` : type of job (categorical: "admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown").

  `marital`: marital status (categorical: "divorced","married","single","unknown"; note: "divorced" means divorced or widowed).

   `education` (categorical: "basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown").

    `default`: has credit in default? (categorical: "no","yes","unknown").

   `housing`: has housing loan? (categorical: "no","yes","unknown").

  `loan`: has personal loan? (categorical: "no","yes","unknown")
   
* **related with the last contact of the current campaign:**
   `contact`: contact communication type (categorical: "cellular","telephone") 

   `month`: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")

   `day_of_week`: last contact day of the week (categorical: "mon","tue","wed","thu","fri")

   `duration`: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
  
* **other attributes:**
   `campaign`: number of contacts performed during this campaign and for this client (numeric, includes last contact)

   `pdays`: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)

   `previous`: number of contacts performed before this campaign and for this client (numeric)

  `poutcome`: outcome of the previous marketing campaign (categorical: "failure","nonexistent","success")
  
* **social and economic context attributes**
  `emp.var.rate`: employment variation rate - quarterly indicator (numeric)

  `cons.price.idx`: consumer price index - monthly indicator (numeric)    

  `cons.conf.idx`: consumer confidence index - monthly indicator (numeric)  

  `euribor3m`: euribor 3 month rate - daily indicator (numeric)

  `nr.employed`: number of employees - quarterly indicator (numeric)

Output variable (desired target):

  * **`y`** has the client subscribed a term deposit? (binary: "yes","no")
  
## EDA
 Exploratry data analysis :in this section we try to get some useful insigh from our data by asking questions and get the answer :
``` 
What are the mean values ​​of numerical features among the attracted clients?

```
| |age|duration|campaign|pdays|previous|emp.var.rate|cons.price.idx|cons.conf.idx|euribor3m|nr.employed|y_class|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|mean|40.91314655172414|553.1911637931034|2.0517241379310347|6.014521452145215(was 729 when we include 999)|0.4926724137931034|-1.2334482758620686|93.35438599137932|-39.78978448275862|2.123135129310344|5095.115991379309|1.0|

```
What is the share of clients attracted in our source data?¶
```
> 11%
```
 What is the average call duration for the attracted clients?
 ```
> 553 second
```
What is the average age among the attracted and unmarried clients?
```
> 31
```
What is the average age and call duration for different types of client employment?
 ```

|job|age|duration|
| ----- | ----- | ----- |
|admin.|38.2401185770751|261.8715415019763|
|blue-collar|39.2658371040724|261.8529411764706|
|entrepreneur|42.2027027027027|249.2027027027027|
|housemaid|45.67272727272727|229.6636363636364|
|management|42.42901234567901|246.7993827160494|
|retired|60.873493975903614|311.78915662650604|
|self-employed|40.67924528301887|254.9245283018868|
|services|38.51399491094148|232.529262086514|
|student|26.695121951219512|287.1341463414634|
|technician|38.62228654124457|253.28654124457307|
|unemployed|39.531531531531535|249.80180180180184|
|unknown|46.84615384615385|234.4102564102564|

For More useful insigh check the report [her](Report.pdf)
## Data Modeling Pipeline
First, I transformed the categorical variables into  LabelEncoder variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error and Accuracy. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**SVM** – #TODO:Add why I chose SVM 
*	**DecisionTreeClassifier** – #TODO:Add why I chose SVM 
*	**GaussianNBt** – #TODO:Add why I chose SVM 

## Model Evaluation
The  DecisionTreeClassifier model far outperformed the other approaches on the test and validation sets. 
||Mean absolute error|Accuracy|Algo|
| ----- | ----- | ----- | ----- |
|0|0.1029376062151007|0.8970623937848993|SVM|
|1|0.086185967467832|0.913814032532168|DecistionTree|
|2|0.151735858218014|0.848264141781986|Naive bayes|
## Model Deployment
In this step, I built a Streamlit web application using python.The web application contains interactive user interface .The page is for model Predict based on the features and return the predict label.