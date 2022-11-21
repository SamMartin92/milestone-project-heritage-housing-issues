import streamlit as st


def page_project_summary_body():

    st.write("# Project Summary")

    st.success(
        "## **Project Inception:**\n"
        "Our client Lydia Doe has inherited four properties in  Ames, Iowa, USA. "
        "Lydia, a resident of Belgium, has limited knowledge of house prices outside of her home country and wishes to gain more insight into the Iowan property market so she may more accurately judge the value of her inheritance.\n"
        "\n Lydia wishes to maximise the sales price of her inherited properties, but also predict the sale price of any property in Ames, Iwoa, should she wish to purchase their in the future. For this reason, she also wishes to know what features contribute most closely with a properties sale price. She has requested graphical representations to better understand.\n"
        "\n Therefore, this project has 2 business requirements:\n"
        "\n 1. The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.\n"
        "\n 2. The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/SamMartin92/milestone-project-heritage-housing-issues).")

    st.info(
        "## **Project Dataset:**\n"
        "* We have located and chosen a publicly available dataset of properties sold in Ames, Iowa. It has information on 24 seperate features per property and we use it to fit our ML model to predict sale prices and to study which features correlate to the sale price most closley."
        "\n* 'SalePrice' will be our focus in this project and represents the price the property was sold for in USD in our dataset."
        "\n* It is our **target** variable, that is, it will be the value we wish to predict using the features provided to us from Lydia's inherited properties."
        "\n* Our dataset has been retrieved from the following [location](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). Information on each feature can be seen below:"
    )


    st.markdown(html_string, unsafe_allow_html=True)


html_string = """<details>
                <summary>Housing price Data</summary>
                <br>
                <table>
                <thead>
                <tr>
                <th style="text-align:left">Variable</th>
                <th style="text-align:left">Meaning</th>
                <th style="text-align:left">Units</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                <td style="text-align:left">1stFlrSF</td>
                <td style="text-align:left">First Floor square feet</td>
                <td style="text-align:left">334 - 4692</td>
                </tr>
                <tr>
                <td style="text-align:left">2ndFlrSF</td>
                <td style="text-align:left">Second floor square feet</td>
                <td style="text-align:left">0 - 2065</td>
                </tr>
                <tr>
                <td style="text-align:left">BedroomAbvGr</td>
                <td style="text-align:left">Bedrooms above grade (does NOT include basement bedrooms)</td>
                <td style="text-align:left">0 - 8</td>
                </tr>
                <tr>
                <td style="text-align:left">BsmtExposure</td>
                <td style="text-align:left">Refers to walkout or garden level walls</td>
                <td style="text-align:left">Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement</td>
                </tr>
                <tr>
                <td style="text-align:left">BsmtFinType1</td>
                <td style="text-align:left">Rating of basement finished area</td>
                <td style="text-align:left">GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement</td>
                </tr>
                <tr>
                <td style="text-align:left">BsmtFinSF1</td>
                <td style="text-align:left">Type 1 finished square feet</td>
                <td style="text-align:left">0 - 5644</td>
                </tr>
                <tr>
                <td style="text-align:left">BsmtUnfSF</td>
                <td style="text-align:left">Unfinished square feet of basement area</td>
                <td style="text-align:left">0 - 2336</td>
                </tr>
                <tr>
                <td style="text-align:left">TotalBsmtSF</td>
                <td style="text-align:left">Total square feet of basement area</td>
                <td style="text-align:left">0 - 6110</td>
                </tr>
                <tr>
                <td style="text-align:left">GarageArea</td>
                <td style="text-align:left">Size of garage in square feet</td>
                <td style="text-align:left">0 - 1418</td>
                </tr>
                <tr>
                <td style="text-align:left">GarageFinish</td>
                <td style="text-align:left">Interior finish of the garage</td>
                <td style="text-align:left">Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage</td>
                </tr>
                <tr>
                <td style="text-align:left">GarageYrBlt</td>
                <td style="text-align:left">Year garage was built</td>
                <td style="text-align:left">1900 - 2010</td>
                </tr>
                <tr>
                <td style="text-align:left">GrLivArea</td>
                <td style="text-align:left">Above grade (ground) living area square feet</td>
                <td style="text-align:left">334 - 5642</td>
                </tr>
                <tr>
                <td style="text-align:left">KitchenQual</td>
                <td style="text-align:left">Kitchen quality</td>
                <td style="text-align:left">Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor</td>
                </tr>
                <tr>
                <td style="text-align:left">LotArea</td>
                <td style="text-align:left">Lot size in square feet</td>
                <td style="text-align:left">1300 - 215245</td>
                </tr>
                <tr>
                <td style="text-align:left">LotFrontage</td>
                <td style="text-align:left">Linear feet of street connected to property</td>
                <td style="text-align:left">21 - 313</td>
                </tr>
                <tr>
                <td style="text-align:left">MasVnrArea</td>
                <td style="text-align:left">Masonry veneer area in square feet</td>
                <td style="text-align:left">0 - 1600</td>
                </tr>
                <tr>
                <td style="text-align:left">EnclosedPorch</td>
                <td style="text-align:left">Enclosed porch area in square feet</td>
                <td style="text-align:left">0 - 286</td>
                </tr>
                <tr>
                <td style="text-align:left">OpenPorchSF</td>
                <td style="text-align:left">Open porch area in square feet</td>
                <td style="text-align:left">0 - 547</td>
                </tr>
                <tr>
                <td style="text-align:left">OverallCond</td>
                <td style="text-align:left">Rates the overall condition of the house</td>
                <td style="text-align:left">10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor</td>
                </tr>
                <tr>
                <td style="text-align:left">OverallQual</td>
                <td style="text-align:left">Rates the overall material and finish of the house</td>
                <td style="text-align:left">10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor</td>
                </tr>
                <tr>
                <td style="text-align:left">WoodDeckSF</td>
                <td style="text-align:left">Wood deck area in square feet</td>
                <td style="text-align:left">0 - 736</td>
                </tr>
                <tr>
                <td style="text-align:left">YearBuilt</td>
                <td style="text-align:left">Original construction date</td>
                <td style="text-align:left">1872 - 2010</td>
                </tr>
                <tr>
                <td style="text-align:left">YearRemodAdd</td>
                <td style="text-align:left">Remodel date (same as construction date if no remodeling or additions)</td>
                <td style="text-align:left">1950 - 2010</td>
                </tr>
                <tr>
                <td style="text-align:left">SalePrice</td>
                <td style="text-align:left">Sale Price</td>
                <td style="text-align:left">34900 - 755000</td>
                </tr>
                </tbody>
                </table>
                """
