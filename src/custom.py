# custom.py
##----------
## This is where you put your custom code that doesn't
## fit the standard categories of data cleaning, feature engineering,
## modeling, or visualization.

def test_custom():
    print('In custom module')
    return None

<<<<<<< HEAD
=======

>>>>>>> 5a372b26f6d9b10890d4f85f29d78ce1fa08d605
def detrend(TS, column):
        p_values = []
        
        decomposition=seasonal_decompose(TS[column].dropna())
        residuals = decomposition.resid
        dftest = adfuller(residuals.dropna())
        dfoutput1 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput1['Critical Values (%s)' %key] = value
        p_values.append(dfoutput1[1])
        
    
        data_diff1 = TS[column].diff(periods=1)
        dftest = adfuller(data_diff1.dropna())
        dfoutput2 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput2['Critical Values (%s)' %key] = value
        p_values.append(dfoutput2[1])
    
        data_diff2 = TS[column].apply(lambda x: np.log(x)) - TS[column].apply(lambda x: np.log(x)).shift(1)
        dftest = adfuller(data_diff2.dropna())
        dfoutput3 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput3['Critical Values (%s)' %key] = value
        p_values.append(dfoutput3[1])
        

        temp_diff = TS[column].apply(lambda x: np.log(x)) - TS[column].apply(lambda x: np.log(x)).shift(1)
        data_diff3 = temp_diff - temp_diff.shift(12)  
        dftest = adfuller(data_diff3.dropna())
        dfoutput4 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput4['Critical Values (%s)' %key] = value
        p_values.append(dfoutput4[1])
        
        if np.argmin(p_values)==0:
            residuals.plot(figsize=(20,6))
            plt.title('{} Seasonal Decomposition'.format(column))
            plt.show();
            print(dfoutput1)
        
        elif np.argmin(p_values)==1:
            data_diff1.plot(figsize=(20,6))
            plt.title('{} First Difference'.format(column))
            plt.show();
            print(dfoutput2)
            
        elif np.argmin(p_values)==2:
            data_diff1.plot(figsize=(20,6))
            plt.title('{} Log First Difference'.format(column))
            plt.show();
            print(dfoutput3)
        
        elif np.argmin(p_values)==3:
            data_diff1.plot(figsize=(20,6))
            plt.title('{} Log Seasonal First Difference'.format(column))
            plt.show();
            print(dfoutput4)