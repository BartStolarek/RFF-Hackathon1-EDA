# 🎧 Spotify EDA Hackathon: Phase 1 - Fundamentals

Welcome to the **Spotify EDA Hackathon**! This is the first challenge in our learning series, and it's all about mastering the **fundamentals** of data exploration. Whether you're new to EDA or already a pro, I'm hoping this challenge will be engaging for you.

## Due Date:

**Monday, 25th November 2024 11:59 PM UTC**  
_Using UTC time to make sure everyone is on the same page, and the due date is after the weekend for everyone_

## Exploratory Data Analysis (EDA)

The basic explanation of EDA is that it is the process of examining and visualizing data to understand its characteristics, it is usually quite opinionated and subjective. EDA is a crucial step in the data analysis process because it helps you to understand the data you are working with. It allows you to identify patterns, relationships, and anomalies in the data, which can help you to make informed decisions.

I encourage you to do your own research of what EDA is, and how to present it. 

A good EDA would include the following + your interpretation of what you're seeing for each:
- Data Exploration
    - Summary statistics
    - Data visualisations
    - Correlation analysis
- Data Engineering
    - Data cleaning and preprocessing
    - Feature Engineering

---

## 🏁 Challenge Overview

Your mission is to dive into the **Spotify and YouTube Dataset** and perform an **Exploratory Data Analysis (EDA)**. The goal is to:
1. Load the data.
2. Explore it visually and descriptively.
3. Clean and preprocess the data.
4. Perform some basic feature engineering.

---

## 🎯 **Learning Objectives**

- Load and explore datasets using **pandas**. If you don't know why use pandas, you should do a quick google to understand why.
- Visualize trends and insights using **matplotlib** and **seaborn**.
- Clean data and handle missing values.
- Engineer new features to uncover hidden insights.
- Collaborate with a team to solve a challenge.
- Create good code
- Use git and GitHub to collaborate on a project.

---

## 🕒 Duration

**2 Weeks**  
Work at your own pace, but ensure to contribute and complete the challenge within the timeframe.

---

## 👫 **Group Work**

- Groups of **2 people** (small enough to ensure active participation).  
- Each group will work on a **separate branch** in this repository.
- Collaborate using **GitHub** and **Discord**.

---

## 📚 **Resources**

If you need resources, I have a few recommendations:
- https://www.machinelearningplus.com/machine-learning/exploratory-data-analysis-eda/
- https://www.analyticsvidhya.com/blog/2022/07/step-by-step-exploratory-data-analysis-eda-using-python/
- https://www.kaggle.com/code/imoore/intro-to-exploratory-data-analysis-eda-in-python

Discord # Resources channel is also a good place for resources

Feel free to ask for help from your team members, the markers, or the wider community, but do try to solve your challenge on your own first. 

---

## **Tools**

You can use any tools you like to solve the challenge. Remember, the goal is to learn. I advise the tools and the use of them should mirror what you would use in a real-world scenario.

## 🛠️ Instructions

### 0. **Preparation**
- Plan your approach and assign parts to each group member - this is crucial in software development. Plan your work, and work your plan.
- Be clear with who will do what, and when its due, but remember this isn't a paid university course, so don't be disheartened if someone doesn't meet the deadline. Just make sure you're all on the same page.

### 1. **Set Up Your Workspace**
1. Clone the repository to your computer. Look in the discord resources channel for some guides on how to use git (thanks Marc).
2. Create a new branch for your group.
3. Make sure to use a **virtual environment** for your project. You can use `venv`, `conda` or jupyter notebooks. If you're using Jupyter Notebooks, make sure to install the required packages in the notebook itself. (Personally I use venv and docker, I think that this way sets you up to understand how to better deploy your code in an application in the future). 
4. Write your code just in the root folder of the repository.

### 2. **Get the Data**
- Download the dataset from [this Kaggle link](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube).
- Save the dataset in the `data/` folder. (This folder is excluded from Git using `.gitignore`.). I will hunt you down if you commit the data to the repository. 😈

### 3. Solve the Challenge
Answer the following questions (deliverables and evaluation criteria are in the next section):

**Essential EDA Questions** (Start with these)
1. What are the basic statistics of the dataset? (number of songs, artists, etc.)
2. Create visualizations to show the distribution of numerical features (danceability, energy, tempo, etc.)
3. What are the top 10 most streamed songs on Spotify in the dataset?
4. What are the top 10 most viewed music videos on YouTube?
5. Is there a correlation any noteable correlation between features?

**Data Cleaning**
1. How many missing values are there in each column?
2. What columns need cleaning? (e.g., formatting issues, inconsistent data)
3. Create one new feature from existing data (e.g., `views_per_like = views/likes`)

**Bonus Challenges** (For those who want to dig deeper)
1. How do musical features (danceability, energy, valence) relate to popularity?
2. Is there a difference in performance between singles and album tracks?
3. What patterns can you find in the relationship between YouTube engagement (likes, comments) and Spotify streams?
4. Do official music videos perform differently from unofficial ones?
5. Create your own research question and explore it!

## 📝 Deliverables

Deliver your deliverables by pushing your branch to the online repository (origin).

1. Code, which should be well commented and follow standard coding practices.
2. Your EDA analysis, either in a report pdf, notebook or commented in to your code, whatever is easiest.
3. A .md file with any comments, how to run your code and/or notes you want to submit, call it `NOTES.md`.

## 🔍 Evaluation Criteria

Since this is a hackathon it is still competitive and I think a ranking system to determine the system is fair. For each criteria item below your group will be assigned a rank from 1st to last, it is possible to tie on a rank.

Your criteria ranks will be added up and the group with the lowest rank (closest to 1) will be the winner. 

- Clarity of code adherence of coding standards and well thoughout structure/architecture
- Completeness of answering the above questions
- Utility in feature engineering
- Quality of visualizations
- Completeness of data cleaning

For example, your group might get rankings of:
| Criteria | Rank |
|----------|------|
| Clarity of code | 1 |
| Completeness of answering the above questions | 4 |
| Utility in feature engineering | 5 |
| Quality of visualizations | 2 |
| Completeness of data cleaning | 2 |

So your final rank/score will be = 1 + 4 + 5 + 2 + 2 = 14, if that is the best score, you group wins!.


## 🏆 Prizes

The winning group will:
- Have their EDA merged in to master and featured on the repository
- Receive $10AUD per person in the group as a 'coffee prize' transferred via [Wise.com](https://wise.com/) (not applicable if two or more teams tie for first).
- Bragging rights until the next Hackathon - There is a 'champion' role on discord to mark your glory!
- A leading role in the next Hackathon, if they like.