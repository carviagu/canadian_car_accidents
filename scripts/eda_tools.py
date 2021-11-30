############################################
# Script with functions to manage dataset
############################################

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def special_values_summary(df = None, vals = []):
    '''
    Returns a dataset with a summary of the pressence of selected values
    in the different values. 
    Params:
    :df: Dataset to analyze
    :vals: List with the selected values 
    '''
    
    # Columns list in the dataset
    cols_svals_df = pd.DataFrame(data = df.columns, columns = ['column_name'])

    # Loop start
    for value in vals:
    
        # Counts the occurencies of the value in a column.
        totals = list()
        for col in cols_svals_df['column_name']:
            totals.append(df[df[col].isin(value)][col].count())
        
        # Creates a column with counts
        cols_svals_df[value[0]] = totals
    
        # Computes percentaje of the occurencies in a column within the total elements.
        percentajes = list()
        for col in cols_svals_df['column_name']:
            percentajes.append(np.round(cols_svals_df[cols_svals_df['column_name'] == col][value[0]] / 
                                        len(df.index) * 100, decimals = 3).values)
        
        # Creates a column with percentajes
        cols_svals_df[value[0] + '%'] = percentajes
    # Loop end

    # Computes total and the percentaje
    cols_svals_df['total'] = cols_svals_df['Q'] + cols_svals_df['N'] + cols_svals_df['U'] + cols_svals_df['X']
    cols_svals_df['total%'] = np.round(cols_svals_df['total'] / len(df.index) * 100, decimals = 1)

    return cols_svals_df


def get_corr_matrix(dataset = None, metodo='pearson', size_figure=[10,8]):

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
                square=True, linewidths=.5,  cmap ='viridis' ) #cbar_kws={"shrink": .5}
    plt.show()


def norm_category(df = None, obj_val = "", cat_val = ""):
    '''
    Computes the normalized of a categorical variable givin an 
    objetive variable. 
    Params:
    :df: Dataset to normalize
    :obj_val: Object variable
    :cat_val: Categorial variable
    '''
    grouped = df.groupby([obj_val, cat_val]).count().iloc[:,1]
    grouped = grouped.reset_index()
    grouped.columns = [obj_val, cat_val, 'counted']
    grouped['group%'] = np.round(grouped['counted'] / 
                                 grouped.groupby(obj_val)['counted'].transform('sum') * 100, decimals = 3)
    
    return grouped