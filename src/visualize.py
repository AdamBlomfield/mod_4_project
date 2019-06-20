def test_viz():
    print('In Visualize')
    pass

def chicago_price_over_time_with_cutoffs():
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

    # import the csv
    zillow_chicago = pd.read_csv('../data/processed/zillow_chicago_1996_to_2018')
    # Convert to datetime
    zillow_chicago['date'] = pd.to_datetime(zillow_chicago['date'], format='%Y/%m/%d')
    
    # Find the mean of all the zipcodes for each date
    zillow_chicago_mean = pd.DataFrame(zillow_chicago[1:].mean(axis=1))
    # Add the date column into the mean column to make 1 df
    date = zillow_chicago['date']
    mean = zillow_chicago_mean
    zillow_chicago_mean = pd.concat([date,mean], axis=1)
    # rename column to 'mean'
    zillow_chicago_mean.columns = ['date', 'mean']
    # drop NaN 1st row
    zillow_chicago_mean.drop(0, inplace=True)
    
    # set figuresize and style
    sns.set(rc={'figure.figsize':(12,6)},style="white", context="talk")
    # plot
    ax = sns.lineplot('date', 'mean', data=zillow_chicago_mean, color='g', lw=5);
    # Formatting
        # Title
    title = 'Median House Price for Chicago\n Between January 1996 & April 2018'
    ax.set_title(title)
        # Axis labels
    xlabel = 'Year'
    ylabel = "Median House Price (USD)"
    ax.set(xlabel=xlabel, ylabel=ylabel)
        # Take off the border
    sns.despine()
    # Vertical Lines
        # financial crisis
    ax.axvline(x='2007-06', ymin=0, ymax=0.95, ls= "--", lw=3, color='black', label='Financial Crisis')
        # Estimation period
    ax.axvline(x='2013', ymin=0, ymax=0.95, ls= "--", lw=3, color='b', label='Start of Estimation Data')
        # Validation Period
    ax.axvline(x='2017-10', ymin=0, ymax=0.95, ls= "--", lw=3, color='r', label='Start of Validation Data')
    # show legend
    plt.legend();
    

    