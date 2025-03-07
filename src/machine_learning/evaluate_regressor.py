import numpy as np
import streamlit as st
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")


def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    """
    Displays results of regression_evaluation function
    """
    st.write("### *Model Evaluation* \n")
    st.write("* #### Train Set")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("* #### Test Set")
    regression_evaluation(X_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):
    """
    Returns R2 score for Test & Train Sets
    for given pipeline
    """
    prediction = pipeline.predict(X)
    st.write(f'*R2 Score:* {r2_score(y, prediction).round(3)}')
    st.write(
        f'Mean Absolute Error: {mean_absolute_error(y, prediction).round(3)}')
    st.write(
        f'Mean Squared Error: {mean_squared_error(y, prediction).round(3)}')
    st.write(
        f'Root Mean Squared Error: {np.sqrt(mean_squared_error(y, prediction)).round(3)}')
    st.write("\n")

    return r2_score(y, prediction.round(3))


def regression_evaluation_plots(
        X_train,
        y_train,
        X_test,
        y_test,
        pipeline,
        alpha_scatter=0.5):
    """
    Plots performance of regression model on
    Test & Train datasets
    """
    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 10))
    sns.scatterplot(
        x=y_train['SalePrice'],
        y=pred_train,
        alpha=alpha_scatter,
        ax=axes[0])
    sns.lineplot(
        x=y_train['SalePrice'],
        y=y_train['SalePrice'],
        color='red',
        ax=axes[0])
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predictions")
    axes[0].set_title("Train Set")

    sns.scatterplot(
        x=y_test['SalePrice'],
        y=pred_test,
        alpha=alpha_scatter,
        ax=axes[1])
    sns.lineplot(
        x=y_test['SalePrice'],
        y=y_test['SalePrice'],
        color='red',
        ax=axes[1])
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predictions")
    axes[1].set_title("Test Set")

    st.pyplot(fig)


def curr_version_r2_score(X, y, pipeline):
    """
    Returns R2 score for Train and
    Test Set of given pipeline
    """
    prediction = pipeline.predict(X)
    curr_r2_score = r2_score(y, prediction).round(3)

    return curr_r2_score
