# Heritage Housing Issues

Link to live dashbard can be accessed [here](https://heritage-housing-issues.herokuapp.com/).

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|



## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* 2 - The client is interested to predict the house sales price from her 4 inherited houses, and any other house in Ames, Iowa.


## Hypothesis and how to validate?
* 1 - Larger houses will tend to have sell at a higher price. Therefore, houses with greater 1stFlrSF will have have a higher sales price.
  * This will be validated with a correlation study & relevant visualisations.

* 2 - The overall condition of the house will result in a higher sale price. Therefore, we believe houses with a similar 1stFlrSF, with a higher OverallCond rating, will have higher Sales Price than those with a lower rating.
   * This will be validated with a correlation study & relevant visualisations.
 
* 3 - Houses with Garages will tend to have a higher Sales Price than those without. And those with large garages will tend to sell at higher prices. Therefore, houses with a large GarageArea will have a higher SalePrice.
   * This will be validated with a correlation study & relevant visualisations.

## User Stories

* This project can be broken down into 5 epics, each composed of a number of user stories which can be mapped to each business requirement.

### 1. Data Collection
  * **As a data practitioner** I want relevant data **so that** data analysis can be conducted and an ML pipeline can be developed.
    * Bus Requirment: BR1 & BR2
    * Action Required: Fetching ata via Kaggle API
      * Satisfied: Publily available housing data sourced from Kaggle
  * **As a data practitioner** I want house attribute data for the inherited properties **so that** a prediction on their sale price can be made once ML pipeline developed.
    * Bus Requirment: BR2
    * Action Required: Fetching data via Kaggle API
      * Satisfied: Full inherited housing data received from client (via Kaggle)
  * **As a client** I want an explanation of the data **so that** I can understand what each column represents to more clearly comprehend the attributes which factor into the sale price of a property.
    * Bus Requirment: BR1
    * Action Required: Inspect data
      * Satisfied: Context for each column provided in README and dashboard (Project Summary)
  * **As a technical user** I want to know the content and source of the data **so that** I can trust the quality of the project's input.
    * Bus Requirment: BR1 & BR2
    * Action Required: Inspect dataset and ensure source is trustworthy
      * Satisfied: Dashboard (Project Summary)
### 2. Data visualization, cleaning, and preparation
  * **As a client** I want to see relevant plots showing how house attributes relate to the sale price **so that** I can gain a better understanding of what features are important when estimating what a property is worth.
    * Bus Requirment: BR1
    * Action Required: Create data plots using relevant python libraries
      * Satisfied: Dashboard (Sale Price Correlation Study) & Jupyter Notebooks (SalePriceStudy & FeatureEngineering)
  * **As a client** I want to discover how house attributes correlate with sales price **so that** I know which attributes most strongly affect the sale price of a property.
    * Bus Requirment: BR1
    * Action Required: Conduct correlation study on the data
      * Satisfied: Dashboard (Sale Price Correlation Study)
  * **As a technical user** I want to see how the data was prepared prior to modelling **so that** I can gain insight into the Data Cleaning & Feature Engineering steps used.
    * Bus Requirment: BR2
    * Action Required: Data Cleaning & Feature Engineering
      * Satisfied: Dashboard (ML Model)
  * **As a data practitoner** I want to have a means of cleaning the data **so that** there is no corrupted or incomplete data within the dataset for ML modelling.
    * Bus Requirment: BR2
    * Action Required: Data Cleaning
      * Satisfied: Jupyter Notebook (DataCleaning)
  * **As a data practitoner** I want to have a means of engineering the data **so that** the data is compatible with ml tasks and the variable distribution can lend itself to more accurate predictions.
    * Bus Requirment: BR2
    * Action Required: Feature Engineering
      * Satisfied: Jupyter Notebook (FeatureEngineering)  
### 3. Model training, optimization and validation.
  * **As a client** I want to predict the the value of the properties I have inherited **so that** I know how much they are worth and maximise their sale value.
    * Bus Requirment: BR2
    * Action Required: Build ML pipeline wiht a target of 'SalePrice'
      * Satisfied: Dashboard (House Price Prediction)
  * **As a client** I want to predict the the value of any house in Ames, Iowa **so that** I have knowledge about the hosuing market in the area if I wish to purchase there in the future.
    * Bus Requirment: BR2
    * Action Required: Build ML pipeline wiht a target of 'SalePrice'
      * Satisfied: Dashboard (House Price Prediction)
  * **As a data practitioner** I want a means of optimising the performance of the ML pipeline **so that** I can make the most accurate sale price prediction possible.
    * Bus Requirment: BR2
    * Action Required: Hyperparameter optimisation using GridSearchCV
      * Satisfied: Jupyter Notebook (SalePricePredition)
  * **As a technical user** I want to know how the model was trained **so that** I gain insight into the fine tuning of the ML task.
    * Bus Requirment: BR2
    * Action Required: Present most up to date version of pipeline in dashboard
      * Satisfied: Dashboard (ML Model), Jupyter Notebook (SalePricePredition)
  * **As a technical user** I want to know how the performance of the ML model **so that** I know how effiecient it is and how it was evaluated.
    * Bus Requirment: BR2
    * Action Required: Evaluate ML model performance and present evidence
      * Satisfied: Dashboard (ML Model), Jupyter Notebook (SalePricePredition)    
### 4.  Dashboard planning, designing, and development.
  * **As a client** I want to easily navigate through a dashboard **so that** I can easily find the information I desire. 
    * Bus Requirment: BR2
    * Action Required: Build streamlit dashboard using 'Multipage' class
      * Satisfied: Dashboard (Side Menu)
  * **As a client** I want interactive visualisations **so that** I may focus on specific elements of the data. 
    * Bus Requirment: BR1
    * Action Required: Plot data and render visualisations in dashboard
      * Satisfied: Dashboard (Sale Price Correlation Study)
  * **As a client** I want to be presented with the summed value of my inherited homes  **so that** I can have a reliable estimate of their value.
    * Bus Requirment: BR2
    * Action required: Run ML Pipeline on inherited housing data and get total sum of values.
      * Satisfied: Dashboard (House Price Prediction) 
  * **As a client** I want run sale price predictions using attributes for any Ames, Iowa property **so that** I can predict the sale price of a property I may wish to purchase in the future 
    * Bus Requirment: BR2
    * Action Required: Use streamlit widgets to create an app which uses ML pipeline to predict based on inputs
      * Satisfied: Dashboard (House Price Prediction)
  * **As a technical user** I to know the project hypotheses and how they were validated **so that** I can gain insight into how conclusions were reached during data analysis.
    * Bus Requirment: BR1
    * Action Required: Posit hypotheses and presnt findings of attempt to validate
      * Satisfied: Dashboard (Project Hypotheses)   
### 5.  Dashboard deployment and release.
  * **As a client** I want a live site **so that** I can access the dashboard and make predictions whenever I wish.
    * Bus Requirment: BR1 & BR2
    * Action Required: Deploy site on heroku
      * Satisfied: Dashboard 
  * **As a data practioner** I want a live site on which to host the project **so that** I can release new pipeline iterations when developed
    * Bus Requirment: BR2
    * Action Required: Redeploy up to date commits to Heroku
      * Satisfied: Dashboard 

## Rationale to map the business requirements to the Data Visualizations and ML tasks
* Business Requirement 1: Correlation Study and Data Visualisation
    * We will inspect the data related to the house sales within our dataset.
    * A correlation study will be conducted to understand which factors affect the sale price of a house most strongly.
      * We will study both Pearson and Spearman levels of correlation.
    * We will plot the most strongly correlated and relevant variables against Sale Price to understand our insights more clearly.
    * Our correlation study and visualisations will asist in validating our project hypotheses.

* Business Requirment 2: Building a Regression Pipeline
    * We want to predict the Sale Price of our client's inherited homes and any other houses in the area.
    * We will train a regression model on our data. This should be the most suitable option as the Sale price of a property is represented as a continuous numeric value in our dataset.
    * We will fine tune our model by fitting a number of hyperparameters and testing the performance for each combination.
    * We hope to fit a pipeline which exceeds our performance metric by this process


## ML Business Case

* We want an ML model to predict:
  1. The combined sale price of our client's 4 inherited houses in Ames, Iowa.
  2. The sale price of any house in Ames, Iowa.
  * In this case, our target variable to predict, is 'SalePrice' which represents the sale price in USD of each home in the dataset.

* Our ideal outcome is to produce a Machine Learning pipeline which will produce a Sale Price prediction to meet our business requirement. Ideally, this pipeline will be trained on only the most important features in our dataset. 
  * It would, therefore, be capable of predicting the sale price of a home with fewer house attributes than is represented in one of the rows in our dataset.

* The model success metrics are and R2 score > 0.75 on both our train and test sets.
  * We will fit a regression model to achieve this.
  * The model will be considered a failure if:
    * Our target R2 score is not reached.
    * The final sale price of the four inherited properties differs by more than 25% of our final predicted total summed sale price.

* The output is defined as a:
  * a prediction of a continuous value representing the final USD sale price of our client's inherited properties
  * a prediction of a continuous value of the final USD sale price of any house in Ames, Iowa given specific attributes for the property

* Heuristics: Currently, we have no reliable means of estimating the sale price of a house in Ames, Iowa. While our client is quite knowledgeable about house prices in her native Belgium, what makes a house attractive or valuable in Iowa is unknown.
   * Within our project hypotheses, we have made some predictions but these are to be validated.

* The training data to fit our model comes from a publily available Kaggle dataset. The dataset contains 1,460 rows of data, each representing a house sold in Ames, Iowa and containing up to 24 features, which hold data relating to a specific attribute of the house.
  * The TrainSet of the data containfs 'SalePrice' as the target variable and all other varaibles, apart from, in the current iteration of our pipeline, 'EnclosedPorch' and 'WoodDeckSF'.


## Dashboard Design
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)
1. Page 1: Project Summary
   * Background and reason for inception of our project.
   * Our business requirements are set out.
   * The source and context of our dataset is explained. A table eplaining each feature of our dataset is available to view.
 
 2. Page 2: Sale Price Correlation Study
    * This page was designed to answer our Business Requirement 1.
    * It contains the output of our correlation study which has taken place in the SalesPriceStudy notebook.
    * A portion of our dataset is displayed and its context is explained..
    * The conclusions of our correlation study are presented and a select box feature allows the user to choose a feature, from among those most strongly correlated with the sale price of a home, against Sale Price ranges.
    * Further information on correlation within our dataset is presented also:
       * Heatmaps displaying correlation levels bewteen variables can be viewed through checkboxes.
       * A heatmap displaying PPS levels can be viewed through a checkbox.
  
3. Page 3: Project Hypotheses
    * Before analysis, it was known that we would want a page to describe our prject hypotheses, our conclusions and how we validated them. 
    * This page confirms hypothesess 1 & 3:
       * Larger Houses (those with greater 1stFlrSF) tend to sell at higher prices.
       * Homes with garages tend to sell at higher prices than those without, and those with large garages sell at higher prices.
    * This page shows hypothesis to be inconclusive:
       * The OverallCond rating of a home does not necessarily lend to greater Sale Price, regardless of size.
      
 4. Page 4: ML Model
    * This page displays the current iteration of the ML pipeline and will be of interest to technical users.
    * There is the option provided with a selectbox to view orevious iterations of the pipeline also.
    * The ML pipeline is displayed, including the features used to fit the model and their importance, are displayed.
    * The performance of the current iteration, and whether it meets the performace criteria, is stated.
    * The regression plots for both the Train & Test Set are presented to the user.
 
 5. Page 5: House Price prediction
    * This page is designed to answer Business Requirement 2.
    * The inherited houses data is available to view.
    * A prediction is made on the sale price of each home using the ML model presented in Dashboard: Page 4.
    * The total sum the client can expect to receive from the sale of her inherited properties is displayed.
    * There are input widgets which will take values for the house attributes on which the model was trained.
        * A user can enter attributes for a specific property into the inputs and using the 'Predict Sale Price' button, can run the values through the ML model and output a predicted sale price for a house with those features.

## Hyperparameters
* The most up to date iteration of the pipeline contains ExtraTreesRegressor as the ML model.
* During modelling, hyperparameter optimisation was carried out in order to improve the model efficiency.
* The choice of which hyperparameters to use in this process was decided by studying the [ExtraTrees Regressor docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html) and choosing from the optional algorithm parameters.
* The ranges of values chosen to run through the hyperparameter optimisation process was decided upon by choosing from the ranges specified in the docs and zoning in on the most efficient parameter value ranges through multiple uses of the HyperparameterOptization() class contained in the notebook.

## Unfixed Bugs
* There are no unfixed bugs to my knowledge in this project, however, when running HyperparameterOptization() using GridSearchCv from feature engine, a future warning is thrown: `/workspace/.pip-modules/lib/python3.8/site-packages/feature_engine/selection/smart_correlation_selection.py:271: FutureWarning: Passing a set as an indexer is deprecated and will raise in a future version. Use a list instead.
  f = X[feature_group].std().sort_values(ascending=False).index[0]`
* I believe this is a pandas future warning and is caused by the Feature-engine library so have been unable to correct it. It causes no issue but prints out a warning for each fit in HyperparameterOptimization().

## Deployment
* This site was developed in [Gitpod](https://www.gitpod.io/) and deployed to [Heroku](https://www.heroku.com/).
* The site is a dashboard built with streamlit. 
* The code to run the site was contained in [app.py](app.py).
* It was developed by previewing the site in the browser by running the commadn `streamlit run app.py` in the command line and slecting the 5801 Port.
* Changes and entries to the workspace were committed and pushed to this repository.

### Setting up the project in Gitpod workspace:
* For this project, a Code Institute template was used which is available at this [repository](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues). To use this template, choose the 'Fork' option at the top right of the repository and open under your own Github profile.
* If you do not wish to fork this repository, to deploy a stream lit app to Heroku, you will need to add the following files to your root directory:
   * Create a shell file called setup.sh and add the following lines of code:
```python
mkdir -p ~/.streamlit/
echo "\
 [server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
* Create a Procfile to specify how to run the app on Heroku and add the following line of code:
```python
web: sh setup.sh && streamlit run app.py
```
 * Once you are ready to deploy, create a requirements.txt file to specify all the libraries need to run this app. This can be created in your root directory by running the command `pip freeze --local > requirement.txt`.
 * Create runtime.txt file in root directory and specify the version of pyhton you are running the app on.
 * See steps on how project was deployed to Heroku below.
### Heroku

* The App live link is: [https://heritage-housing-issues.herokuapp.com/](https://heritage-housing-issues.herokuapp.com/)
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. Ensure the version of python you are running in runtime.txt is compatible with your app's Heroku stack. If you need to set the heroku stack for your app, you can do so by running the following commands in the command line:
    * Install Heroku by running `pip install heroku'
    * Login by running `heroku login -i` and entering your login details
    * Set remote to Heroku `heroku git:remote -a <APP-NAME>`
    * Set stack `heroku stack:set <HEROKU-STACK> -a <APP-NAME>`  
7. The deployment process should happen smoothly in case all deployment files are fully functional. Click the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
Below is a list of the main libraries used in the creation of this project. An exhaustive list of all libraries used can be seen in [requirements.txt](requirements.txt)
* [Streamlit](https://streamlit.io/)- App framework on whihc the the dashboard was designed and created.
* [Numpy](https://numpy.org/)- Used for working with arrays. Used to generate boolean arrays in plotting correlation heatmaps and returning Root Mean Squared Error in Regression Evaluation function
* [Pandas](https://pandas.pydata.org/)- Data analysis tool used to convert the raw data for data frames and all methods of inspecting and manipulating the datasets
* [pandas_profiling](https://pypi.org/project/pandas-profiling/)- Used to generate profile reports from DataFrames in our Jupyter Notebooks. These reports provide deeper insight into the datasets providing information such as missing data, mean, median, distribution, data counts and much more.
* [Feature-engine](https://feature-engine.readthedocs.io/en/latest/)- A data engineering library with various transformer and feature selection methods for ML modelling. Some examples of its use in this project;  imputation of numerical and categorical data during data cleaning, categorical encoding to make data compatible for deeper data analysis, numerical transformation to normalise feature distribution during modelling, smart correlated selection step in ML pipeline creation and discretising data for the purpose of plotting data.
* [Scikit-Learn](https://scikit-learn.org/)- A library which provides tools for data analytics. Scikit-Learn was used to create the pipeline,feature selection & splitting Train and Test sets. It is essential to the modelling stage as the algorithms tested on our data were imported from the library. sklearn methods were used to evaluate the performance algorithms and gridsearchcv was used during hyperparameter optimization in which the performance of different hyperparameters on given models were scored to test their efficiency in predictions. 
* [XGBoost](https://xgboost.readthedocs.io/en/stable/)- A machine learning pipeline whih provides GradientBoosting methods. XGBRegressor was one of the algortihms tested druing pipeine optimization.
* [matplotlib] (https://matplotlib.org/)- Matplotlib is a library used for creating data visiualisations. It was used to create visual plots in this project, mainly used in conjuction with Seaborn.
* [seaborn](https://seaborn.pydata.org/index.html)- Seaborn is a library built on matplotlib. It was used in the creation of data visualisations in this project, such as correlation histograms and line plots, heatmaps and for regression performance.
* [ppscore](https://pypi.org/project/ppscore/)- A library used in predicting the predictive power scores of the varaibles in the dataset.


## Credits 

### Content 

- Any custom functions taken and/or adapted from Code Institue lessons or other sources has been noted in Markdown or comments in the code where applicable.
- The template for this repository was created by Code institue.
- The idea for this project was presented in the CI lessons.
- The dataset for this project was sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)

### Media

- The streamlit icon used for the dashboard was taken from [Twemoji](https://twemoji.maxcdn.com/v/latest/preview-svg.html).
- 
## Acknowledgements:
* Thank you to Neil McEwan and fellow students in the CI slack channel for this module for the assistance with queries throughout this project.
* Thank you to my mentor Mo Shami for his helpful advice.

