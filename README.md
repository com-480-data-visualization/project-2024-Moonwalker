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
- [Popular Video Games 1980 - 2023](https://www.kaggle.com/code/hossamelshabory97/popular-video-games-1980-2023-eda): This dataset contains a list of very pupular video games released from 1980 to 2023, it also provides other things such as release dates, user review rating, discribe summary and critic review rating, which are super useful for us to find out some interesting insights about the popularity of video games recently. 
- [Videogame-company-regions](https://www.kaggle.com/datasets/andreshg/videogamescompaniesregions): **TODO**

#### Ⅰ. Global Video Game Sales Dataset
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

#### Ⅱ. 1980-2023 Popular Video Games Dataset
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

#### Ⅲ. Videogame-company-regions Dataset
> **Size**: 7 columns and 686 rows

**TODO**

#### Ⅳ. Preprocess
For the *Global Video Game Sales* and *Videogame-company-regions* dataset, we merged the two dataset by the column **Publisher** and **Developer**, for the convenience of futher analysis. 

For the *Popular Video Games 1980 - 2023*, we first clean up the dataset by dropping the first meaningless column and some rows including **null** values. After that, we do a deeper cleaning by removing the rows where its **Release Date** is "releases on TBD", changing the columns name to lower case, replacing spaces with "_" for consistency and converting the special data type “K“ into the integer (1000) for some columns. 

For more details please check our jupyter notebook [eda.ipynb](https://github.com/com-480-data-visualization/project-2024-Moonwalker/blob/master/data/eda.ipynb).

### Problematic

<!-- 
> Frame the general topic of your visualization and the main axis that you want to develop.
> - What am I trying to show with my visualization?
> - Think of an overview for the project, your motivation, and the target audience. 
-->
**TODO**
- Examines changes over time in the gaming industry, tracking shifts in consumer preferences.
- Identifies the platforms that are leading in worldwide game sales and explores the success of various game genres across different regions.


### Exploratory Data Analysis

<!-- 
> Pre-processing of the data set you chose
> - Show some basic statistics and get insights about the data 
-->

**Top 10 Most Popular Video Games Genres.** 
This figure deisplays the top 10 popular video game genres, with 'Adventure' games leading the pack at 1005 games. Following are 'RPG' games with a significant count of 422 games. The genres 'Platform' and 'Shooter' are fairly close in popularity, with 282 and 270 games respectively. 'Brawler', 'Simulator', and 'Turn Based Strategy' genres have the fewest games among the top 10, with counts of 119, 109, and 99 games accordingly. The chart provides a clear visual representation of the disparity in popularity among different video game genres.
![Global production](images/Top10Popular.png "Top 10 Most Popular Video Games Genres")

**Trends of the Average Adventure Video Games'Rating.**
This figure shows the average ratings for adventure games from 1985 to around 2020. There’s a notable peak in the early '90s, followed by a sharp decline. Ratings fluctuate afterwards but stay mostly above 3.5. The trend from 2010 onwards is slightly downward, suggesting a recent dip in ratings for the genre. Overall, the genre’s ratings have varied but stayed within a defined range over the years.
![Global production](images/AdventureRating.png "Trends of the Average Adventure Video Games'Rating")

### Related work


#### 1. What others have already done with the data?
Several analyses and visualizations have been conducted using our dataset, including:
- [Data Analysis & Visualization: Video Game Sales](https://www.kaggle.com/datasets/thedevastator/global-video-game-sales): This work analyzed the Global Video Game Sales dataset using R.
- [Popular Video Games 1980 - 2023](https://www.kaggle.com/code/hossamelshabory97/popular-video-games-1980-2023-eda): This work analyzed the Popular Video Games 1980 - 2023 dataset using python.

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

