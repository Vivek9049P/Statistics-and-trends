"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
#from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

def plot_relational_plot(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Size (max cm)'], y=df['Weight (max kg)'], hue=df['Name'])
    plt.xlabel("Max Size (cm)")
    plt.ylabel("Max Weight (kg)")
    plt.title("Size vs. Weight of Irish Animals")
    plt.legend(loc='best', bbox_to_anchor=(1,1))
    plt.savefig('relational_plot.png')
    plt.show()
    

def plot_categorical_plot(df):
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values(by='Population', ascending=False)
    plt.barh(df_sorted['Name'], df_sorted['Population'], color='skyblue')
    plt.xlabel("Population")
    plt.ylabel("Animal Species")
    plt.title("Population of Irish Animals")
    plt.gca().invert_yaxis()
    plt.savefig('categorical_plot.png')
    plt.show()
    

def plot_statistical_plot(df):
    plt.figure(figsize=(8, 6))
    numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap of Animal Traits")
    plt.savefig('statistical_plot.png')
    plt.show()
    

def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col].dropna())
    excess_kurtosis = ss.kurtosis(df[col].dropna())
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    print(df.describe())
    print(df.head())
    numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
    print(numeric_df.corr())
    return df

def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    if abs(moments[2]) < 0.5:
        skew_text = "not skewed"
    elif moments[2] > 0:
        skew_text = "right skewed"
    else:
        skew_text = "left skewed"
    
    if moments[3] < -1:
        kurtosis_text = "platykurtic"
    elif moments[3] > 1:
        kurtosis_text = "leptokurtic"
    else:
        kurtosis_text = "mesokurtic"
    
    print(f'The data was {skew_text} and {kurtosis_text}.')
    return

def main():
    df = pd.read_csv('irish_animals.csv')
    df = preprocessing(df)
    col = 'Size (max cm)'  # You can change this to another numerical column
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return

if __name__ == '__main__':
    main()
