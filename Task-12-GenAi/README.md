# ----------- Assignment 12: Seaborn (Relational, Distribution, Categorical, Multi-Plots)---------------


## Dataset
- Insurance Dataset
- Kaggle dataset link : https://www.kaggle.com/datasets/vysakhvms/dataset


## Task 1: Relational Plot
- Imports all libraries
- Read the dataset -----> pd.read_csv()
- Convert the the dataset into DataFrame ----> pd.DataFrame()
1. Create a realtional plot using sns.relplot()
- X-axis : Age
- Y-axis : Policy Term
2. Use hue with a categorical column --->  Hue : plan
3. Create the same plot using scatter plot ---> sns.relplot() ---> kind=scatter

#### Obervations
- Most customers have a policy term of 15 or 20 years
- Nonpar plan has the highest number of customers
- Health , ULIP and Par plans have fewer records
- The scatter plot clearly shows the distribution of customers by age and plan type
 
#### Conclusion
- Relational plots help compare numerical variables and identify patterns across different categories using color


## Task 2: Line Plot as Scatter & Facet
1. Create a line plot using sns.lineplot()
2. Conerting the same relationship into a scatter style line plot
3. Using faceting (col or row ) to split the plot based on a categories column

#### Obervations
- ULIP plans generally have the highest insurance amounts
- Health plans have the lowest average amount
- Nonpar contains the largest number of customer records
- Customer age ranges approximately from 21 to 60 years
- Faceting makes it easy to compare each insurance plan separately

#### Conclusion
- Line plot show trends , scatter plots display individual data points and faceting improves compression between different plan categories


## Task 3: Distribution Plots
- For a numerical column:
1. Plot a Histogram using seaborn   ----> sns.histplot()
2. Plot KDE plot  ---> sns.kdeplot()
3. Plot Rug plot  -----> sns.rugplot()
4. Combine Histogram + KDE in a single plot  ---> sns.histplot(kde=True)

#### Obervations
- Visualized the frequency distribution of the Age column
- Used the Plan column as hue to compare distribution across different insurance plans.
- Displayed the position of each observation along the x-axis
- Visualized both frequency and probability density in a single plot

#### Conclusion
- Different Seaborn distribution plots to analyses the spread , density, and pattern of numerical data.



## Task 4: Bivariate Distribution Plots
1. Create a bivariate histogram ----> sns.histplot()
- Visualized the joint distribution of two numerical variables
2. Create a bivariate KDE plot ---> sns.kdeplot()
- Displayed the density distribution of two numerical variables



## Task 5: Matrix Plots
1. Create a pair plot using sns.pairplot()
- Visualized pairwise relationships between numerical columns
2. Create a heatmap of correlation matrix
- Calculated the correlation matrix ---> corr()
- Created a heatmap using sns.heatmap() to visualize correlations between numerical features



## Task 6: Categorical Plots
- Using a categorical and numerical column
1. Bar Plot
- Created a bar plot using sns.barplot()
- Compared the average Age across different insurance plans
2. Box Plot
- Created a box plot using sns.boxplot()
- Visualized the distribution of amount and deteched outliers
3. Violin Plot
- Created a violin plot using sns.violinplot()
- Displayed both the distribution and density of Age for each plan
4. Count Plot
- Created a count plot using sns.countplot()
- Counted the number of records for each Policy Term


## Task 7: Regression Plot
1. Create a regression plot (regplot) between two numerical columns
- Created a regression plot using sns.regplot()
- Visulized the relationship between Age and Amount with a best fit regression line
2. Create a lmplot with hue using a categorical column
- Created a lmplot using sns.lmplot()
- Used the Plan column as the hue parameter to compare regression trends across different insurance plans.


## Task 8: Multi Plots & Figure Level Plots
1. Create a FacetGrid with:
- Created a relational using sns.facetGrid()
- Display a scatter plot of Age and Amount for each plan insurance plan
2. Create a multi plot dashboard using:
---> relplot
- Created a relational plot using sns.relplot()
- Compared the relationship between Age and Amount across different plans
---> catplot
- Created a categorical plot using sns.catplot()
- Visualized the distribution of Age for different insurance plans
---> displot
- Created a distribution plot using sns.displot()
- Displayed the distribution of Age with KDE for each insurance plan 



## Learning Objective
- Relational plots
- Distribution plots
- Categorical plots
- Regression plots
- Matrix plots
- Faceting & Multi plots


## How to run
- Requirements

1. Python
2. VS code or other code editor

- Steps:

1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run
  