{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def detrend(TS, column):\n",
    "        p_values = []\n",
    "        \n",
    "        decomposition=seasonal_decompose(TS[column].dropna())\n",
    "        residuals = decomposition.resid\n",
    "        dftest = adfuller(residuals.dropna())\n",
    "        dfoutput1 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])\n",
    "        for key, value in dftest[4].items():\n",
    "            dfoutput1['Critical Values (%s)' %key] = value\n",
    "        p_values.append(dfoutput1[1])\n",
    "        \n",
    "    \n",
    "        data_diff1 = TS[column].diff(periods=1)\n",
    "        dftest = adfuller(data_diff1.dropna())\n",
    "        dfoutput2 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])\n",
    "        for key, value in dftest[4].items():\n",
    "            dfoutput2['Critical Values (%s)' %key] = value\n",
    "        p_values.append(dfoutput2[1])\n",
    "    \n",
    "        data_diff2 = TS[column].apply(lambda x: np.log(x)) - TS[column].apply(lambda x: np.log(x)).shift(1)\n",
    "        dftest = adfuller(data_diff2.dropna())\n",
    "        dfoutput3 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])\n",
    "        for key, value in dftest[4].items():\n",
    "            dfoutput3['Critical Values (%s)' %key] = value\n",
    "        p_values.append(dfoutput3[1])\n",
    "        \n",
    "\n",
    "        temp_diff = TS[column].apply(lambda x: np.log(x)) - TS[column].apply(lambda x: np.log(x)).shift(1)\n",
    "        data_diff3 = temp_diff - temp_diff.shift(12)  \n",
    "        dftest = adfuller(data_diff3.dropna())\n",
    "        dfoutput4 = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])\n",
    "        for key, value in dftest[4].items():\n",
    "            dfoutput4['Critical Values (%s)' %key] = value\n",
    "        p_values.append(dfoutput4[1])\n",
    "        \n",
    "        if np.argmin(p_values)==0:\n",
    "            residuals.plot(figsize=(20,6))\n",
    "            plt.title('{} Seasonal Decomposition'.format(column))\n",
    "            plt.show();\n",
    "            print(dfoutput1)\n",
    "        \n",
    "        elif np.argmin(p_values)==1:\n",
    "            data_diff1.plot(figsize=(20,6))\n",
    "            plt.title('{} First Difference'.format(column))\n",
    "            plt.show();\n",
    "            print(dfoutput2)\n",
    "            \n",
    "        elif np.argmin(p_values)==2:\n",
    "            data_diff1.plot(figsize=(20,6))\n",
    "            plt.title('{} Log First Difference'.format(column))\n",
    "            plt.show();\n",
    "            print(dfoutput3)\n",
    "        \n",
    "        elif np.argmin(p_values)==3:\n",
    "            data_diff1.plot(figsize=(20,6))\n",
    "            plt.title('{} Log Seasonal First Difference'.format(column))\n",
    "            plt.show();\n",
    "            print(dfoutput4)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
<<<<<<< HEAD
   "version": "3.6.6"
=======
   "version": "3.7.3"
>>>>>>> 621e22db200163ed0e82e9149d3ffb654f785f9d
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
