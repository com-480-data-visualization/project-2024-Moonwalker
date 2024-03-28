# Project of Data Visualization (COM-480)

| Student's name | SCIPER |
| -------------- | ------ |
| Haotian Wu | 351555 |
| Erchang Ni | 352440 |
| Jingbang Liu| 369414 |

[Milestone 1](#milestone-1) • [Milestone 2](#milestone-2) • [Milestone 3](#milestone-3)

## Milestone 1 (29th March, 5pm)

**10% of the final grade**

<!-- This is a preliminary milestone to let you set up goals for your final project and assess the feasibility of your ideas.
Please, fill the following sections about your project.

*(max. 2000 characters per section)* -->

### Dataset
- [Global Video Game Sales](https://www.kaggle.com/datasets/thedevastator/global-video-game-sales): A dataset contains information about the global sales of top video games across different platforms and genres. The original dataset contains a list of video games with sales greater than 100,000 copies from [vgchartz.com](https://www.vgchartz.com), which is scraped by [Gregory Smith's work](https://zenodo.org/records/5898311#.Y9Y2K9JBwUE).
- [Popular Video Games 1980 - 2023](https://www.kaggle.com/code/hossamelshabory97/popular-video-games-1980-2023-eda): This dataset contains a list of video games dating from 1980 to 2023, it also provides things such as release dates, user review rating, discribe summary and critic review rating.

#### Global Video Game Sales Dataset
> **Size**: 11 columns and 16600 rows

| Column Name   | Description                                                   |
|---------------|---------------------------------------------------------------|
| Rank          | Ranking of the game based on global sales. (Integer)          |
| Name          | Name of the game. (String)                                    |
| Platform      | Platform the game was released on. (String)                   |
| Year          | Year the game was released. (Integer)                         |
| Genre         | Genre of the game. (String)                                   |
| Publisher     | Publisher of the game. (String)                               |
| NA_Sales      | Sales of the game in North America. (Float)                   |
| EU_Sales      | Sales of the game in Europe. (Float)                          |
| JP_Sales      | Sales of the game in Japan. (Float)                           |
| Other_Sales   | Sales of the game in other regions. (Float)                   |
| Global_Sales  | Total sales of the game worldwide. (Float)                    |

#### 1980-2023 Popular Video Games Dataset
> **Size**: 14 columns and 1512 rows

| Column Name   | Description                                                   |
|---------------|---------------------------------------------------------------|
| Title         | Title of the game. (String)                                   |
| Release Date  | Date of release of the game's first version. (Object)         |
| Team          | Game developer team. (String)                                 |
| Rating        | Average rating. (Float)                                       |
| Times Listed  | Number of users who listed this game. (Object)                |
| N of Reviews  | Number of reviews received from the users. (Object)           |
| Genres        | All genres pertaining to a specified game. (List)             |
| Summary       | Summary provided by the team. (String)                        |
| Reviews       | User reviews. (String)                                        |
| Plays         | Number of users that have played the game before. (Object)    |
| Playing       | Number of current users who are playing the game. (Object)    |
| Backlogs      | Number of users who have access but haven't started. (Object) |
| Wishlist      | Number of users who wish to play the game. (Object)           |

#### Preprocess
(TBD) For the *Global Video Game Sales* dataset, we clean up entries that miss the year of release.

For the *Popular Video Games 1980 - 2023*, we first clean up the dataset by dropping the first meaningless column and some rows including **null** values. After that, we do a deeper cleaning by removing the rows where its **Release Date** is "releases on TBD", changing the columns name to lower case, replacing spaces with "_" for consistency and converting the special data type “K“ into the integer (1000) for some columns. 

For more details please check our jupyter notebook [eda.ipynb](https://github.com/com-480-data-visualization/project-2024-Moonwalker/blob/master/data/eda.ipynb).

### Problematic

<!-- 
> Frame the general topic of your visualization and the main axis that you want to develop.
> - What am I trying to show with my visualization?
> - Think of an overview for the project, your motivation, and the target audience. 
-->

- Examines changes over time in the gaming industry, tracking shifts in consumer preferences.
- Identifies the platforms that are leading in worldwide game sales and explores the success of various game genres across different regions.


### Exploratory Data Analysis

<!-- 
> Pre-processing of the data set you chose
> - Show some basic statistics and get insights about the data 
-->

Finally, we plot the **Top 10 most popular video games genres** based on the total number of games in each genres. We also explore the **trends of the average Adventure video games'rating** over the years to explore the change of Adventure video games'rating in the past 30 years.

### Related work


#### 1. What others have already done with the data?
Several analyses and visualizations have been conducted using our dataset, including:
- [Data Analysis & Visualization: Video Game Sales](https://www.kaggle.com/datasets/thedevastator/global-video-game-sales): This work analyzed the Global Video Game Sales dataset using R.
-  

#### 2. Why is your approach original?

#### 3. What source of inspiration do you take? 
Additionally, we draw inspiration from impressive visualization projects across different subjects from previous years:
- [Anime Data Visualization](https://github.com/com-480-data-visualization/com-480-project-worldwideweebz) : This project inspired us to come up with our figure 1, aiming to visualize the genre preference and popularity about the most authoritative game sales in the video game industry.

<!-- - In case you are using a dataset that you have already explored in another context (ML or ADA course, semester project...), you are required to share the report of that work to outline the differences with the submission for this class. -->

## Milestone 2 (26th April, 5pm)

**10% of the final grade**


## Milestone 3 (31st May, 5pm)

**80% of the final grade**


## Late policy

- < 24h: 80% of the grade for the milestone
- < 48h: 70% of the grade for the milestone

