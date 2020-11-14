import pandas as pd


def calculate_demographic_data(print_data=True):
    ### Read data from file
    df = pd.read_csv("adult.data.csv")
    # print(df.describe())

    ### How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    ### What is the average age of men?
    men_bool = df["sex"] == 'Male'
    average_age_men = df.loc[men_bool,'age'].mean()
    average_age_men = round(average_age_men,1)

    ### What is the percentage of people who have a Bachelor's degree?
    bach_count = df.education.value_counts().loc['Bachelors']
    total_ed_count = df.education.count()
    percentage_bachelors = bach_count / total_ed_count
    percentage_bachelors = round(percentage_bachelors*100,1)

    ### What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    ### What percentage of people without advanced education make more than 50K?

    ## with and without `Bachelors`, `Masters`, or `Doctorate`
    # total count
    total_ed_count = df.education.count()
    # df for each higher education
    bach_df = df[df.education == 'Bachelors']
    mast_df = df[df.education == 'Masters']
    doc_df = df[df.education =='Doctorate']
    # combine into one higher ed df
    higher_ed_df = pd.concat([bach_df,mast_df,doc_df])
    # higher ed count
    higher_ed_count = higher_ed_df.education.count()
    # ratio of higher ed to lower ed
    higher_education = higher_ed_count / total_ed_count # given in repl.it template but did not use
    lower_education = 1 - higher_education # given in repl.it template but did not use

    ## percentage with salary >50K
    # count higher ed over 50K
    higher_ed_rich_count = higher_ed_df.salary.value_counts().loc['>50K']    
    # calc percentage higher ed over 50k    
    higher_education_rich = higher_ed_rich_count / higher_ed_count
    higher_education_rich = round(higher_education_rich*100,1)
    # calc percentage lower ed over 50k
    lower_ed_count = total_ed_count - higher_ed_count
    lower_ed_rich_count = df.salary.value_counts().loc['>50K'] - higher_ed_rich_count
    lower_education_rich = lower_ed_rich_count / lower_ed_count
    lower_education_rich = round(lower_education_rich*100,1)

    ### What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    ### What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'] == 1).sum()    
    min_worker_bool = df["hours-per-week"] == 1
    min_worker_rich = df.loc[min_worker_bool,'salary'] == '>50K'
    rich_percentage = min_worker_rich.value_counts().loc[True]/num_min_workers
    rich_percentage = round(rich_percentage*100,1)

    ### What country has the highest percentage of people that earn >50K?
    # create dictionary of country counts
    countries_count = {}
    countries = df["native-country"].tolist()
    for i in countries:
        try:
            countries_count[i]+=1
        except:
            countries_count[i]=1
    # create dictionary of high earners country counts
    df_high_earn = df[df.salary == '>50K']
    countries_high_earn_count = {}
    countries_high_earn = df_high_earn["native-country"].tolist()
    for i in countries_high_earn:
        try:
            countries_high_earn_count[i]+=1
        except:
            countries_high_earn_count[i]=1
    # create dictionary of countries' ratio of higher earners to total
    high_earn_percentage = {}
    for k in countries_count:
        try:
            high_earn_percentage[k] = countries_high_earn_count[k] / countries_count[k]
        except:
            pass
    # Return key with highest value
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    v=list(high_earn_percentage.values())
    k=list(high_earn_percentage.keys())
    highest_earning_country = k[v.index(max(v))]
    highest_earning_country_percentage = round(max(v)*100,1)

    ### Identify the most popular occupation for those who earn >50K in India.
    india_df = df.loc[df['native-country'] == 'India']
    india_high_earn_df = india_df.loc[df['salary'] == '>50K']
    top_IN_occupation = india_high_earn_df['occupation'].value_counts().idxmax()
    
    
    
    ##### DO NOT MODIFY BELOW THIS LINE #####
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# calculate_demographic_data(print_data=True)