import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data Source
# Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental
# Protection Agency using data from CSIRO, 2015; NOAA, 2015.
# https://datahub.io/core/sea-level-rise


def draw_plot():
    ### Read data from file
    ## Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv("epa-sea-level.csv",float_precision='legacy') #fp req for error in replit
    # print(df.head())
    # print(df.describe())

    ### Create scatter plot
    ## Use matplotlib to create a scatter plot using the "Year" column as the
    ## x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y,s=5);
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    
    ### Create first line of best fit
    ## Use the linregress function from scipi.stats to get the slope and
    ## y-intercept of the line of best fit. Plot the line of best fit over
    ## the top of the scatter plot. Make the line go through the year 2050 to
    ## predict the sea level rise in 2050.
    slope, intercept, r, p, se = linregress(x, y)
    # print("Slope:",slope,"\nIntercept:",intercept,"\nRvalue:",r,"\nPvalue:",p,"\nStdErr:",se)
    
    years_extended = []
    for x in range(1880, 2050, 1):
        years_extended.append(x)
    years_extended = pd.Series(years_extended)
    plt.plot(years_extended, slope*years_extended+intercept, '-r')


    ### Create second line of best fit
    ## Plot a new line of best fit just using the data from year 2000
    ## through the most recent year in the dataset. Make the line also go
    ## through the year 2050 to predict the sea level rise in 2050 if the
    ## rate of rise continues as it has since the year 2000.
    
    df_recent = df[df['Year'] >= 2000]
    # print(df_recent.head())
    # print(df_recent.describe())
    x_rec = df_recent['Year']
    y_rec = df_recent['CSIRO Adjusted Sea Level']
    slope_rec, intercept_rec, r_rec, p_rec, se_rec = linregress(x_rec, y_rec)
    
    years_extended_rec = []
    for x in range(2000, 2050, 1):
        years_extended_rec.append(x)
    years_extended_rec = pd.Series(years_extended_rec)
    plt.plot(years_extended_rec, slope_rec*years_extended_rec+intercept_rec, '-g')

    ### Add labels and title
    ## The x label should be "Year", the y label should be
    ## "Sea Level (inches)", and the title should be "Rise in Sea Level".
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()