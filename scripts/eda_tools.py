############################################
# Script with functions to analyze dataset
############################################

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def special_values_summary(df=None, vals=None):
    '''
    Returns a dataset with a summary of the pressence of selected values
    in the different values. 
    :param df: Dataset to analyze
    :param vals: List with the selected values
    :return: dataframe
    '''

    if vals is None:
        vals = []

    # Columns list in the dataset
    cols_svals_df = pd.DataFrame(data=df.columns, columns=['column_name'])

    sum_column = pd.DataFrame(0, index=np.arange(len(cols_svals_df.index)), columns=['store'])

    # Loop start
    for value in vals:

        # Counts the occurencies of the value in a column.
        totals = list()
        for col in cols_svals_df['column_name']:
            totals.append(df[df[col].isin(value)][col].count())

        # Creates a column with counts
        cols_svals_df[value[0]] = totals
        sum_column['store'] = sum_column['store'] + cols_svals_df[value[0]]

        # Computes percentaje of the occurencies in a column within the total elements.
        percentajes = list()
        for col in cols_svals_df['column_name']:
            percentajes.append(np.round(cols_svals_df[cols_svals_df['column_name'] == col][value[0]] /
                                        len(df.index) * 100, decimals=3).values)

        # Creates a column with percentajes
        cols_svals_df[value[0] + '%'] = percentajes
    # Loop end

    # Computes total and the percentaje
    cols_svals_df['total'] = sum_column['store']
    cols_svals_df['total%'] = np.round(cols_svals_df['total'] / len(df.index) * 100, decimals=1)

    return cols_svals_df


def get_corr_matrix(dataset=None, metodo='pearson', size_figure=None):
    '''
    Prints a correlation matrix
    :param dataset: dataset
    :param metodo: method
    :param size_figure: size of the displayed matrix
    :return: plot
    '''
    if size_figure is None:
        size_figure = [10, 8]

    if dataset is None:
        print(u'\nHace falta pasar argumentos a la función')
        return 1
    sns.set(style="white")
    # Compute the correlation matrix
    corr = dataset.corr(method=metodo)
    # Set self-correlation to zero to avoid distraction
    for i in range(corr.shape[0]):
        corr.iloc[i, i] = 0
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=size_figure)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, center=0,
                square=True, linewidths=.5, cmap='viridis')  # cbar_kws={"shrink": .5}
    plt.show()


def norm_category(df=None, obj_val="", cat_val=""):
    '''
    Computes the normalized of a categorical variable giving an
    objetive variable.
    :param df: Dataset to normalize
    :param obj_val: Object variable
    :param cat_val: Categorial variable
    :return: Dataframe
    '''
    grouped = df.groupby([obj_val, cat_val]).count().iloc[:, 1]
    grouped = grouped.reset_index()
    grouped.columns = [obj_val, cat_val, 'counted']
    grouped['group%'] = np.round(grouped['counted'] /
                                 grouped.groupby(obj_val)['counted'].transform('sum') * 100, decimals=3)

    return grouped


def dataset_overview(data=None):
    '''
    Returns a dataframe with column type info and missing analysis.
    :param data: Dataset to analyze
    :return: Dataframe
    '''
    types_df = data.dtypes.reset_index()
    types_df.columns = ['columna', 'tipo_dato']
    types_df['nulos'] = data.isnull().sum().to_numpy()
    types_df['nulos%'] = types_df['nulos'] / data.shape[0] * 100
    return types_df


def classes_overview(df=None, obj_val=""):
    '''
    Returns a dataframe with percentage and absolute values of the variable.
    :param df: Dataset to analyze
    :param obj_val: Objective variable
    :return: Dataframe
    '''
    temp = df[obj_val].value_counts(normalize=True).mul(100).rename('percentaje').reset_index()
    temp_cont = df[obj_val].value_counts().reset_index()
    return pd.merge(temp, temp_cont, on=['index'], how='inner')


def classes_overview_target(df=None, target = "", obj_val=""):
    '''
    Returns a dataframe with percentage and absolute values of the variable, and the majority target
    variable of the section.
    :param df: Dataset to analyze
    :param obj_val: Objective variable
    :param target: Target variable
    :return: Dataframe
    '''
    if (target == ""):
        print("ERROR: Target variable is missing")
        return -1

    overview = classes_overview(df = df, obj_val = obj_val)

    grouped = norm_category(df = df, obj_val = target, cat_val = obj_val)

    values = df[target].unique()
    cats = df[obj_val].unique()

    temp = list()
    for ca in cats:
        hist = {}
        for val in values:
            hist[val] = grouped[(grouped[target] == val) &
                                (grouped[obj_val] == ca)]['group%'].iloc[0]

        maxi = hist[values[0]]
        selected = values[0]
        for val in values:
            if maxi < hist[val]:
                maxi = hist[val]
                selected = val

        temp.append(selected)

    overview[target] = temp

    return overview