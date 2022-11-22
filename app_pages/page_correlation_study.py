from feature_engine.discretisation import EqualFrequencyDiscretiser
from feature_engine.imputation import CategoricalImputer
import streamlit as st
import numpy as np
from src.data_management.data import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import ppscore as pps





def page_correlation_study():

    df = load_housing_data()

    df_corr_pearson, df_corr_spearman, pps_matrix = calculate_corr_and_pps(df)

    cols_and_conclusions = {
        '1stFlrSF': 'Houses with high Sales Prices tend to have first floors with at least 1500 square feet.',
        'GarageArea': 'Houses with low Sales Prices tend to have no garage and those with a garage of at least 600 square feet tend to have high Sales Prices.',
        'GrLivArea': 'Houses with high sales prices tend to have above grade living area of at least 1500 square feet. Those with low sales prices tend to have 1000 square feet or less.',
        'OverallQual': 'Houses with high Sales prices tend to have at least a Very Good Overall Quality Rating.',
        'TotalBsmtSF': 'Houses with high Sales Prices tend to have basements with at a square footage of at least 1200. Houses with no basements or basements with less than 1000 square feet tend to have low Sales prices.',
        'YearBuilt': 'Houses do not tend to have a high Sales Price if built before 1990.'
    }

    conclusions = print_conclusions(cols_and_conclusions)

    

    st.write("## Sale Price Correlation Study")
    st.info(
        """
        * Our client wishes to know how certain attributes correlate with the final sale price of a property.\n
        * The dataset is available to view below and we have chosen the most important features relevant to sale
         price further below.
        """
    )

    if st.checkbox("House Price Data"):
        st.write(
            "* Below is the raw uncleaned dataset for our study.\n"
            f" * This dataset has {df.shape[0]} rows representing {df.shape[0]} properties.\n"
            f" * This dataset has {df.shape[1]} columns representing {df.shape[1]} different house attributes.\n\n"
            "A sample of the first 10 rows can be seen below."
        )

        st.write(df.head(10))

    st.info(
        """
        * A correlation study was run in our SalePriceStudy notebook and it was found that 
        the variables most closely correlated with the sale price of a house were as follows:\n
        """
        f"* {', '.join(list(cols_and_conclusions.keys()))}"

    )

    st.write(
        """
        * Insight into these attributes and their values plotted against sales prices can be seen below.
            * Each conclusion below maps to its respective plot which can be chosen by selecting the feature 
            from the drop down menu.
            * All sale prices have been sorted into 6 ranges for a more general representation of the type
             of sale price one might expect for a property with a given attribute.
        """
    )

    st.success(
        "## Conclusions:\n"
        f"{print_conclusions(cols_and_conclusions)}"
    )

    load_plots_and_conclusions(df,cols_and_conclusions,plot_numerical)

    st.info( """
        During feature engineering, heatmaps were produced to study the correlation levels and PPS 
        between all variables in our dataset. These can be seen below, showing only variables whose correlation 
        and PPS are greater than 0.4 & 0.2 respectively.
        """)

    if st.checkbox("Pearson Correlation"):
        heatmap_corr(df=df_corr_pearson,threshold=0.4, figsize=(20,14), font_annot = 14)

    if st.checkbox("Spearman Correlation"):    
        heatmap_corr(df=df_corr_spearman,threshold=0.4, figsize=(20,14), font_annot = 14)

    if st.checkbox("Predictive Power Score"): 
        heatmap_pps(df=pps_matrix,threshold=0.2, figsize=(20,14), font_annot = 14)
    


def load_plots_and_conclusions(df,cols_and_conclusions,plot_numerical):
    df_disc, hue_order = sale_price_discretisation(df)
    variables = list(cols_and_conclusions.keys())

    st.write(" ## Visualisations:")
    option = st.selectbox(
        "",
        (variables))

    for variable in variables:
        if option == variable:
            plot_numerical(df_disc, variable, 'SalePrice', hue_order)

    
def print_conclusions(cols_and_conclusions):
    conclusions = ""
    for conclusion in list(cols_and_conclusions.values()):
        conclusions += f"* {conclusion}\n"

    return conclusions   
    

def plot_numerical(df, col, target_var, hue_order):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, hue_order=hue_order,kde=True,element="step") 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig)


def sale_price_discretisation(df):

    # disctretises 'SalePrice'
    discretiser= EqualFrequencyDiscretiser(q=6, variables=['SalePrice'])
    discretiser.fit(df)
    df_disc=discretiser.transform(df)
    
    # maps quantile values to 'SalePrice'
    labels=discretiser.binner_dict_['SalePrice']
    q_value= len(labels)-1
    labels_map={}

    for x in range(0,q_value):
        if x == 0:
            labels_map[x] = f"< {int(labels[1])}"
        elif x < q_value -1:
            labels_map[x] = f"{int(labels[x])} - {int(labels[x+1])}"
        else:
            labels_map[x] =f"{int(labels[x])} +"
    
    df_disc["SalePrice"] = df_disc["SalePrice"].replace(labels_map)

    # creates hue_order for histograms
    hue_order = list(labels_map.values())
  
    return df_disc, hue_order


def calculate_corr_and_pps(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')
    
    return df_corr_pearson, df_corr_spearman, pps_matrix


def heatmap_corr(df,threshold, figsize=(20,14), font_annot = 14):
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5, 
                     )
    axes.set_yticklabels(df.columns, rotation = 0, fontsize =20)
    axes.set_xticklabels(df.columns, fontsize =20)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:

        mask = np.zeros_like(df, dtype=np.bool)
        mask[abs(df) < threshold] = True

        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                        mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                        linewidth=0.05,linecolor='grey')
        ax.set_yticklabels(df.columns, rotation = 0, fontsize =20)
        ax.set_xticklabels(df.columns, fontsize =20)

        plt.ylim(len(df.columns),0)
        st.pyplot(fig)









