# Ø Introduction

- The work has been done as a data science group project by [Yashar Mansouri](https://github.com/YM88) and [Andrea Koltai](https://github.com/apy444).
- **Main objective** of the project is to analyse different available movie databases and provide an initial recommendation on the genre and the studios of those genres that are the most profitable. 
- The **key success factor** for this objective is considered not the gross revenues, but the net income values and the net income divided by the production budget. 
- Needless to say this is an inital analysis and there are so many different factors in releasing a profitable movie. However, defining the genre or the studio creating those genres can be the first key step in a movie production investment.
- Data cleaning is almost completely done through some simple python functions and pandas libraries. 
- Merging dataframes and getting descriptive datasets are done using python functions and creating subsets of the joined tables.
- Duplicate values and NaN values have been dropped through using release year as a key and additional manual input was done to make sure the output is as valid as it can be.
- The visualization and the results part provide the output and the recommendations of the analysis.
- Plots and Visualizations are done using a combination of matplotlib and seaborn libraries.
- All codes and notes are available on the ```mod1-ym-ak - final code.ipynb``` python notebook file. 
- Figures are in the jpg format and available in the root repository folder. 
- Besides the introduction, the project consists of other sections described as below:

# I. Initial Data Lookup

This section will read the different datasets and decide which ones to analyze. Further it will do data cleaning, merging and doing initial hypotheses.
## 1. [*Box Office Mojo*](https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=2010&p=.htm) Data - _**studio** values and **title** values to be used from the dataframe_

## 2. [IMDB](https://www.imdb.com/interfaces/) Data - _Used **title_basics** and **title_ratings** from this data set_

## 3. [Rotten Tomatoes](https://www.kaggle.com/rpnuser8182/rotten-tomatoes) Data - won't be used in the EDA

## 4. [The Movie DB](https://developers.themoviedb.org/3/discover/movie-discover) Data - won't be used in the EDA

## 5. [The Numbers](https://www.the-numbers.com/movie/budgets/all) Data - _**release_date**, **movie**, **production_budget**, and **worldwide_gross** values to be used in the EDA._

# II. EDA

## 1. Merging Dataframes of imdb title basics and The Numbers for financial analysis per genre

Steps include:

- Joining the dataframes and creating the `genre_financial_df`
- Filtering for 2010-2018 years
- Removing NaN in genre and worldwide values 
- Removing duplicate in movie name values
- creating new descriptive values:

`1. net income = **worldwide gross** - **production budget**`


`2. net income ratio = **net income** / **production budget**`

- creating a new dataframe for descriptive analysis on genres `describe_genres`

## 2. Using financial data from EDA.1 part and merge with**bom_movie_gross** data
Steps include: 

- Removing NaN values from Studios
- Creating a new studio_financial _df dataframe by merging bom_movie_gross_df and genre_financial_df
- Renaming the studio name values
- Creating a subset df with the top 4 genres in highest net income medians
- Creating a subset df with the 2 top performing studios in the low budget

# III. Visualizations

## 1. Comparison of Medians in Worldwide Revenues and Production Budgets

## 2. Median of Worldwide Net Income in Different Movie Genres

## 3. Comparison Between Median Net Income Ratio & Budget Values per Genres

## 4. Top Studios with Net Income Ratio Values in the Top 4 High Budget Genres

## 5. Top Studios with Net Income Ratio Values in the Top 2 Low Budget Genres


# IV. Results

The results can help a business to make better decisions in terms of choosing the right genres/actors/writers/directors for an investment in the movie industry.

1. III-1. Plot shows the median worldwide gross vs their budget median in all different genres between 2010-2018.  According to this plot, the top 4 genre categories are Animatoin, Adventure, Sci-Fi, and Action. 

2. III-2. Plot shows the net income values for all genres 2010-2018. This give a better understanding of the world gross minus the production budgets which shows although some categories might have a high gross but in reality they have a lower total profit. 

3. III-3. The figure provides the net income ratio percentage (NIR) vs the budget median for all movie genres to give a realistic knowledge of the investment per genre.

4. III-4. The NIR is used to visulaize the top performing production studios in the top 4 genres with the net income ratio in the high budget groups.

5. III-5. The figure provides the top performing production studios in the top 2 genres with the net income ratio in the low budget groups.

# V. Next Steps

- Further analysis of the writers, directors of the data through title_principals database to visualize which writers and directors perform better.
- Measuring the voting and popularity values through imdb and the movie db databases.
- Finding the best performing actors in the specific genres.
- Analyzing multiple genre movies and see which categories have generally performed better.
- Finding recent successful hits in each category to get a better idea of whether the movies were original plots or a new extension of an existing one.  















