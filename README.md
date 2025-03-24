# Subreddits & Storytelling: Is What’s Old is New Again? 

## Background
Modern tabletop role-playing games (RPGs) trace their origins to the late 1960s, emerging from the wargaming scene with experimental titles like Braunstein, which introduced narrative-driven character roles and open-ended play. This innovation paved the way for Dungeons & Dragons (D&D), co-created by Dave Arneson and Gary Gygax in 1974. D&D formalized the blend of storytelling and strategic gameplay, launching a new genre that quickly gained traction and inspired countless derivative systems. Decades later, the early 2000s saw the rise of the Old School Renaissance (OSR)—a movement dedicated to reviving the tone and mechanics of early D&D editions. OSR design emphasizes simplicity, modularity, and a "rulings over rules" philosophy, leading to the creation of retro-clone systems like Labyrinth Lord, Swords & Wizardry, and Old School Essentials.

Parallel to these stylistic developments, the RPG industry has seen dramatic financial growth. Hasbro’s 1998 acquisition of Wizards of the Coast (the current publisher of D&D) signaled mainstream recognition of the hobby’s value. The Open Game License (OGL) launched in the 2000s spurred third-party publishing and broadened the market. Crowdfunding platforms like Kickstarter have since become key funding sources, with projects like Shadowdark raising over $1.5 million. Meanwhile, actual-play shows like Critical Role, The Adventure Zone, and Dimension 20 have expanded RPG audiences globally, helping D&D reach an estimated 85 million players by 2021. Collectively, these trends underscore both the cultural and economic momentum driving the modern RPG landscape.

## Problem Statement
This project intends to make a model that can predict, with at least 75% accuracy, the textual differences between posts scraped from the "RPG" and "OSR" subreddit communities, in order to inform table top industry professionals of factors relevant to TTRPG game development and marketing. 

## Data Dictionary


## Executive Summary

### Project Methodology

This project compares posts of textual content collected from Reddit via the PRAW API:

* Posts from the general-purpose subreddit r/rpg
* Posts from the more narrowly focused r/osr, a community centered around Old School Renaissance (OSR) style games.

The classification goal was to predict whether a given document was more likely to originate from the OSR community or the broader RPG community. Alongside classification, we used exploratory data analysis (EDA) to surface high-weight keywords and topic anchors in each community.

After basic cleaning (e.g. lowercasing, stopword removal, and punctuation stripping), we vectorized the text using TF-IDF to identify the most significant unigrams and bigrams by term frequency and inverse document frequency. We then trained two models— a Random Forest Classifier and Logistic Regression— using GridSearchCV for hyperparameter tuning.

### Findings

The final model achieved an F1 score of approximately 83%, a significant improvement over the random baseline of ~51%. This indicates a meaningful difference in language use between the two subreddits, even with some expected overlap.

Through TF-IDF analysis and EDA, we identified a set of frequently used and highly distinctive terms in the OSR corpus:

* System-relevant terms like “B/X”, “Old School Essentials”, and “Basic Fantasy”
* Mechanics-driven terms such as “rules”, “system”, “campaign”, and “random tables”
* Thematic anchors including “dungeon”, “magic items”, and “”

These findings suggest that OSR discourse is more mechanically and structurally focused, whereas general RPG discussions are more diffuse in tone and scope. The presence of crossover (e.g. shared discussions about role-playing games generally or fantasy tropes) likely accounts for the model’s 17% misclassification rate.

### Conclusion

* Our classifier demonstrates a meaningful (though not perfect) ability to distinguish between the two, highlighting the linguistic cohesion of the OSR scene while acknowledging overlap in user interests and topics.

* The OSR community exhibits a strong preference for discourse prominently featuring discussions of mechanics, traditional play formats, and particular systems such as B/X or Old School Essentials.

* The general RPG community has a larger scope of games and genres, therefore their language may not be as consolidated around specific terminoloy as the osr community.

### Recommendations

* Terms like “Old School Essentials”, “B/X”, and “Basic Fantasy” frequently surface. By explicitly connecting your game to these well-known systems—either highlighting similarities in tone/mechanics or clarifying how your game differs—you can tap into the existing conversation around popular OSR frameworks.

* Unigrams such as “rules”, “system”, and “campaign” rank highly, suggesting that players in these communities care deeply about the structure and style of gameplay. Be prepared to showcase how your rule system supports an “old school” approach—e.g., simplicity, modularity, random tables, or robust character creation.

* Terms like “osr games,” “osr style,” “dungeon,” and “magic items” show that OSR fans gravitate toward specific tropes (e.g., traditional dungeon-crawling, distinctive loot, and resource management). Position your marketing and pitch decks around these thematic anchors to signal you speak their language.

* Future research should explore sentiment analysis on these key terms to measure not only their frequency but the connotation of the document where they appear. This might offer more insight into which terms are postively vs. negatively perceived.

* Consider expanding the dataset to include other platforms like Discord servers, blogs, or forums to verify whether these trends persist beyond Reddit.



This data science project explores the linguistic and thematic differences between two major online RPG communities—r/rpg and r/osr—to provide game designers, publishers, and marketers with a clearer understanding of how Old School Renaissance (OSR) players talk about games, what they value, and how those values differ from the broader TTRPG community. Our objective was to quantify the language of OSR through natural language processing (NLP) and build a classifier capable of distinguishing between posts from the two subreddits.

Using Reddit as our primary data source, we scraped thousands of user-submitted documents via PRAW, focusing on the communities’ natural discourse. We vectorized the text using TF-IDF and tested several classification models (Random Forest, Logistic Regression), ultimately achieving an F1 score of ~83%—a strong result that significantly outperformed the baseline accuracy of ~51%. This indicates that there are indeed detectable and meaningful differences in how each community communicates.

Key findings revealed that terms like “Old School Essentials,” “B/X,” “Basic Fantasy,” “system,” “rules,” and “campaign” are strong signals of OSR-related content. These terms not only helped power our classifier but also offer a valuable lens into what OSR fans prioritize: mechanics, clarity in rules, modularity, and traditional play structures such as dungeon-crawling and resource management. Developers aiming to reach this audience would benefit from aligning their product language, design documentation, and marketing materials with these concepts.

To deepen these insights, we propose a follow-up sentiment analysis: by targeting documents containing key phrases like “OSR games,” “magic items,” or “5e,” we can assess the tone (positive, neutral, negative) surrounding these terms. This would allow creators to understand not just what OSR users talk about, but how they feel about those topics—an invaluable edge when refining mechanics, aesthetics, or outreach.

In conclusion, this project provides both a robust classifier and a qualitative map of OSR community values. These tools can guide publishers in writing Kickstarter copy, shaping rulebooks, or deciding how best to frame comparisons to other systems. While no model can fully disentangle the shared heritage of RPG communities, this approach brings us closer to speaking the OSR community’s language—both literally and figuratively.

Next Steps:

Run sentiment analysis on high-weight keywords to assess community attitudes

Expand data collection to include additional forums (e.g., Discord, blogs, YouTube transcripts)

Apply topic modeling to cluster OSR sub-genres (e.g., sword & sorcery, grimdark, high fantasy)

Share classifier tool as a lightweight, web-based demo for marketing and editorial use





# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

### Description

In week four we learned about a few different classifiers. In week five we're learning about webscraping, APIs, and Natural Language Processing (NLP). This project will put those skills to the test.

For project 3, your goal is two-fold:
1. Using [PRAW](https://praw.readthedocs.io/en/stable/index.html), you'll collect posts from two subreddits of your choosing.
2. You'll then use NLP to train a classifier on which subreddit a given post came from. This is a binary classification problem.


#### About the API

For this project, you will be using [PRAW](https://praw.readthedocs.io/en/stable/index.html) to collect posts from two different subreddits. 

To help you get started, we have a [notebook](./Reddit-PRAW-tutorial.ipynb) detailing the process of creating an app and obtaining your API credentials.

Note: Rather than working in this template notebook, make a brand new "scraping" notebook (or script), with your own unique work and comments, so you can use this project in a portfolio!

---

### Requirements

- Gather and prepare your data using PRAW.
- **Create and compare two models**. Any two classifiers at least of your choosing: random forest, logistic regression, KNN, SVM, etc.
- A Jupyter Notebook with your analysis for a peer audience of data scientists.
- An executive summary of your results.
- A short presentation (5-8 minutes) outlining your process and findings for a semi-technical audience.

**Pro Tip:** You can find a good example executive summary [here](https://www.proposify.biz/blog/executive-summary).

---

### Necessary Deliverables / Submission

- Code must be in at least one clearly commented Jupyter Notebook.
- A readme/executive summary in markdown.
- You must submit your slide deck as a PDF.
- Materials must be submitted by **9:00 AM (PDT) on Friday, 3/21**.

---

## Rubric
Your instructors will evaluate your project (for the most part) using the following criteria.  You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

For Project 3 the evaluation categories are as follows:<br>
**The Data Science Process**
- Problem Statement
- Data Collection
- Data Cleaning & EDA
- Preprocessing & Modeling
- Evaluation and Conceptual Understanding
- Conclusion and Recommendations

**Organization and Professionalism**
- Organization
- Visualizations
- Python Syntax and Control Flow
- Presentation

**Scores will be out of 30 points based on the 10 categories in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?
- Does the student consider the audience and the primary and secondary stakeholders?

**Data Collection**
- Was enough data gathered to generate a significant result? (At least 1000 posts per subreddit)
- Was data collected that was useful and relevant to the project?
- Was data collection and storage optimized through custom functions, pipelines, and/or automation?
- Was thought given to the server receiving the requests such as considering number of requests per second?

**Data Cleaning and EDA**
- Are missing values imputed/handled appropriately?
- Are distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?
- Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?

**Preprocessing and Modeling**
- Is text data successfully converted to a matrix representation?
- Are methods such as stop words, stemming, and lemmatization explored?
- Does the student properly split and/or sample the data for validation/training purposes?
- Does the student test and evaluate a variety of models to identify a production algorithm (**AT MINIMUM:** two models)?
- Does the student defend their choice of production model relevant to the data at hand and the problem?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem objective?
- Does the student interpret the results of their model for purposes of inference?
- Is domain knowledge demonstrated when interpreting results?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Does the student address how findings of this research can be applied for the benefit of stakeholders?
- Are future steps to move the project forward identified?


### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?

**Visualizations**
- Are sufficient visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Are `sklearn` and `NLTK` methods used appropriately?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?


---

### Why did we choose this project for you?
This project covers three of the biggest concepts we cover in the class: Classification Modeling, Natural Language Processing and Data Wrangling/Acquisition.

Part 1 of the project focuses on **Data wrangling/gathering/acquisition**. This is a very important skill as not all the data you will need will be in clean CSVs or a single table in SQL.  There is a good chance that wherever you land you will have to gather some data from some unstructured/semi-structured sources; when possible, requesting information from an API, but sometimes scraping it because they don't have an API (or it's terribly documented).

Part 2 of the project focuses on **Natural Language Processing** and converting standard text data (like Titles and Comments) into a format that allows us to analyze it and use it in modeling.

Part 3 of the project focuses on **Classification Modeling**.  Given that project 2 was a regression focused problem, we needed to give you a classification focused problem to practice the various models, means of assessment and preprocessing associated with classification.   
