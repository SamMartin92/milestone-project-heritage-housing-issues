import streamlit as st


def page_hyp_study_body():
    """
    Function to runs all elements
    of hypothesis study page
    """
    st.info(
        """
        * Before our project began, we posited some hypothises about the Sale Price of the properties in the dataset.\n
        * Having conducted our data analysis in our SalePriceStudy notebook, we can offer the following insights:

        """
    )

    st.success(
        """
        1. Larger houses will tend to have sell at a higher price. Therefore, houses with greater 1stFlrSF will have have a higher sales price.\n
            * **Correct**. There is a strong linear correlation between '1tFlrSF' and 'SalePrice'.
            * From plotting our data , one can observe that homes with first floor square footage of at least 1500 tend to sell for within the highest price range.\n

        2. The overall condition of the house will result in a higher sale price. Therefore, we believe houses with a similar 1stFlrSF, with a
            higher OverallCond rating, will have higher Sales Price than those with a lower rating.\n
            * **Inconclusive**. There is not enough evidence to support this and the correlation between 'OverallCond' and 'SalePrice' is weak.
            * When observing the sale price of properties within similar ranges of '1stFlrSF' on a strip plot, those with higher than average ratings of 'OverallCond'
             were shown to distributed between lower, average and higher sale prices.\n

        3. Houses with Garages will tend to have a higher Sales Price than those without. And those with large garages will tend to sell at higher prices.
            Therefore, houses with a large GarageArea will have a higher SalePrice.
            * **Correct**. There is a strong linear correlation between 'GarageArea' and 'SalePrice'.
            * It is clear from our study that houses without garages sell overwhelmingly in the lowest price range.
            * It can be seen too, from our correlation study histogram, that properties sold in the lowest price range mainly have a garage area of only 200-400 square foot, whereas
                the bulk of the properties sold within the highest price range have a garage area of at least 600 square foot and fall within the 600-900 square foot range.
        """
    )
