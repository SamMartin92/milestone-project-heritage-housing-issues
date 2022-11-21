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



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: [(https://heritage-housing-issues.herokuapp.com/](https://heritage-housing-issues.herokuapp.com/)
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

