

# 🎧 Spotify EDA Hackathon: Phase 1 - Fundamentals

Welcome to the **Spotify EDA Hackathon**! This is the first challenge in our learning series, and it's all about mastering the **fundamentals** of data exploration. Whether you're new to EDA or already a pro, I'm hoping this challenge will be engaging for you.

## Due Date:

**Monday, 25th November 2024 11:59 PM UTC**
_Using UTC time to make sure everyone is on the same page, and the weekend is finished for everyone_

## Exploratory Data Analysis (EDA)

The basic explanation of EDA is that it is the process of examining and visualizing data to understand its characteristics, it is usually quite opinionated and subjective. EDA is a crucial step in the data analysis process because it helps you to understand the data you are working with. It allows you to identify patterns, relationships, and anomalies in the data, which can help you to make informed decisions.

I encourage you to do your own research of what EDA is, and how to present it. 

A good EDA would include the following + your interpretation of what you're seeing for each:
- Summary statistics
- Data visualisations
- Correlation analysis
- Data cleaning and preprocessing
- Feature Engineering


---

## 🏁 Challenge Overview

Your mission is to dive into the **Spotify Charts Dataset** and perform an **Exploratory Data Analysis (EDA)**. The goal is to:
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
- Download the dataset from [this Kaggle link](https://www.kaggle.com/datasets/sunnykakar/spotify-charts-all-audio-data).
- Save the dataset in the `data/` folder. (This folder is excluded from Git using `.gitignore`.). I will hunt you down if you commit the data to the repository. 😈

### 3. Solve the Challenge
Answer the following questions:

**EDA Questions**
1. What is the distribution of track durations? Are most tracks short or long?
2. Which regions and artists dominate the "Top 200" charts?
3. What trends can be seen in the `streams` and `popularity` columns over time?
4. How do `danceability`, `energy`, and `valence` vary across regions?
5. Are there correlations between `streams`, `popularity`, and any `af_` features like `af_danceability` or af_energy?

**Data Cleaning**
1. Identify and handle missing values in the dataset.
2. Create at least one meaningful new feature (check discord #definitions channel for what a feature is). I.e. `streams_per_minute`

**Bonus (Optional)**
1. Can you identify seasonal trends in track popularity or streaming numbers?
2. Explore the `explicit` column: Is explicit content more popular in some regions than others?
3. Add in any more explorations you have found interesting.

## 📝 Deliverables

Deliver your deliverables by pushing your branch to the online repository (origin).

1. Code, which should be well commented and follow standard coding practices.
2. Your EDA analysis, either in a report pdf or commented in to your code, whatever is easiest.
3. A .md file with any comments or notes you want to submit, call it `NOTES.md`.

## 🔍 Evaluation Criteria

Since this is a hackathon it is still competitive and I think a ranking system to determine the system is fair. For each criteria item below your group will be assigned a rank from 1st to last.

Your criteria ranks will be added up and the group with the lowest rank (closest to 1) will be the winner. 

- Clarity of code and adherence to coding standards.

## 🏆 Prizes

The winning group will:
- Have their EDA merged in to master and featured on the repository
- Receive $10AUD per person in the group as a 'coffee prize' transferred via [Wise.com](https://wise.com/) (not applicable if two or more teams tie for first).
- Bragging rights until the next Hackathon - There is a 'champion' role on discord to mark your glory!
- A leading role in the next Hackathon, if they like.


