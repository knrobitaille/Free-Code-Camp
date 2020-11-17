import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

### Import data
df = pd.read_csv("medical_examination.csv")
# print(df.head())
# print(df.describe())

### Add 'overweight' column
# https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o
df['overweight'] = df.apply(lambda row: 0 if (row.weight / ((row.height/100) ** 2)) < 25 else 1, axis=1)
# print(df.head())

"""
To determine if a person is overweight, first calculate their BMI by dividing
their weight in kilograms by the square of their height in meters. If that
value is > 25 then the person is overweight. Use the value 0 for NOT overweight
and the value 1 for overweight.
"""

### Normalize data by making 0 always good and 1 always bad. If the value of
### 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df.apply(lambda row: 0 if row.cholesterol == 1 else 1, axis=1)
df['gluc'] = df.apply(lambda row: 0 if row.gluc == 1 else 1, axis=1)
# pd.set_option('display.max_columns', None)
# print(df.head(6))

### Draw Categorical Plot
def draw_cat_plot():
    ### Create DataFrame for cat plot using `pd.melt` using just the values from
    ### 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=["cardio"],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    # print(df_cat.head())
    # print()


    ### Group and reformat the data to split it by 'cardio'. Show the counts of
    ### each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = df_cat['value']
    df_cat = df_cat.groupby(['cardio','variable','value']).count()
    df_cat = df_cat.reset_index()
    # print(df_cat.head(24))



    ### Draw the catplot with 'sns.catplot()'
    # https://seaborn.pydata.org/generated/seaborn.catplot.html
    bar = sns.catplot(data=df_cat,
                kind='bar',
                x='variable',
                y= 'total',
                hue='value',
                col='cardio'
                )
    fig = bar.fig


    ##### Do not modify the next two lines #####
    fig.savefig('catplot.png')
    return fig


#### Draw Heat Map
def draw_heat_map():
    """
    Clean the data. Filter out the following patient segments that represent incorrect data:
        diastolic pressure is higher then systolic (Keep the correct data with df['ap_lo'] <= df['ap_hi']))
        height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
        height is more than the 97.5th percentile
        weight is less then the 2.5th percentile
        weight is more than the 97.5th percentile
        Create a correlation matrix using the dataset. Plot the correlation matrix using
        seaborn's heatmap(). Mask the upper triangle. The chart should look like "examples/Figure_2.png".
    """
    
    
    
    ### Clean the data
    df_heat = df
    df_heat.drop(df_heat[df_heat['ap_hi']<df_heat['ap_lo']].index, inplace= True)
    df_heat.drop(df_heat[df_heat['height']<df_heat['height'].quantile(0.025)].index, inplace= True)
    df_heat.drop(df_heat[df_heat['height']>df_heat['height'].quantile(0.975)].index, inplace= True)
    df_heat.drop(df_heat[df_heat['weight']<df_heat['weight'].quantile(0.025)].index, inplace= True)
    df_heat.drop(df_heat[df_heat['weight']>df_heat['weight'].quantile(0.975)].index, inplace= True)
    
    # print(df.head(992))

    ### Calculate the correlation matrix
    corr = df_heat.corr()


    ### Generate a mask for the upper triangle
    mask = np.zeros(corr.shape)
    mask[np.triu_indices_from(mask)] = True



    ### Set up the matplotlib figure
    SIZE = 8
    fig, ax = plt.subplots(figsize=(SIZE, SIZE))

    ### Draw the heatmap with 'sns.heatmap()'
    # https://seaborn.pydata.org/generated/seaborn.heatmap.html
    ax = sns.heatmap(corr,
                     mask = mask,
                     vmin=-.16,
                     vmax=.3,
                     square = True,
                     linecolor = 'white',
                     linewidths=.5,
                     cbar_kws={'shrink':.5, 'format':'%.2f'},
                     center=0,
                     fmt='.1f',
                     annot=True)



    ##### Do not modify the next two lines #####
    fig.savefig('heatmap.png')
    return fig

######################################################################
# draw_cat_plot()
draw_heat_map()