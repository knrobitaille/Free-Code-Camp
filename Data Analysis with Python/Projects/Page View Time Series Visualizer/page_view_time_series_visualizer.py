import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = ["date"])
# print(df.head())
# print(df.describe())

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]
# print(df.head())
# print(df.describe())


def draw_line_plot():
    """
    Create a draw_line_plot function that uses Matplotlib to draw a line chart
    similar to "examples/Figure_1.png". The title should be "Daily freeCodeCamp
    Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date"
    and the label on the y axis should be "Page Views".
    """
    fig = plt.figure(figsize=(10, 3))

    plt.plot(df['value'],color='r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# draw_line_plot()

def draw_bar_plot():
    """
    Create a draw_bar_plot function that draws a bar chart similar to
    "examples/Figure_2.png". It should show average daily page views for each
    month grouped by year. The legend should show month labels and have a title
    of "Months". On the chart, the label on the x axis should be "Years" and
    the label on the y axis should be "Average Page Views".
    """
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year
    
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    # print(df_bar.head())
    # print(df_bar.describe())

    months=['January','February','March','April','May','June','July','August','September','October','November','December']

    # Draw bar plot
    fig = df_bar.plot(kind ='bar', figsize=(8, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(fontsize = 10, labels = months)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
# draw_bar_plot()
    
def draw_box_plot():
    """
    Create a draw_box_plot function that uses Searborn to draw two adjacent
    box plots similar to "examples/Figure_3.png". These box plots should show
    how the values are distributed within a given year or month and how it
    compares over time. The title of the first chart should be "Year-wise Box
    Plot (Trend)" and the title of the second chart should be "Month-wise Box
    Plot (Seasonality)". Make sure the month labels on bottom start at "Jan"
    and the x and x axis are labeled correctly.
    """
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    # print(df_box.head())
    # print(df_box.describe())

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(12, 5), ncols=2, sharex=False)
    sns.despine(left=True)
    
    box_plot_year = sns.boxplot(x=df_box['Year'], y=df_box.value, ax=axes[0])
    box_plot_year.set_title("Year-wise Box Plot (Trend)")
    box_plot_year.set_xlabel('Year')
    box_plot_year.set_ylabel('Page Views')

    box_plot_month = sns.boxplot(x=df_box['Month'], y=df_box.value, ax=axes[1],
                                 order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    box_plot_month.set_title("Month-wise Box Plot (Seasonality)")
    box_plot_month.set_xlabel('Month')
    box_plot_month.set_ylabel('Page Views') 

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
# draw_box_plot()


# Run all
print("\n\n\nLine Plot")
draw_line_plot()

print("\n\n\nBar Plot")
draw_bar_plot()

print("\n\n\nBox Plot")
draw_box_plot()
    
    
    