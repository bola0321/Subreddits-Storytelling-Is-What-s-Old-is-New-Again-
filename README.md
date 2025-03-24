# Subreddits & Storytelling: Is What’s Old is New Again? 

## Background
Modern tabletop role-playing games (RPGs) trace their origins to the late 1960s, emerging from the wargaming scene with experimental titles like Braunstein, which introduced narrative-driven character roles and open-ended play. This innovation paved the way for Dungeons & Dragons (D&D), co-created by Dave Arneson and Gary Gygax in 1974. D&D formalized the blend of storytelling and strategic gameplay, launching a new genre that quickly gained traction and inspired countless derivative systems. Decades later, the early 2000s saw the rise of the Old School Renaissance (OSR)—a movement dedicated to reviving the tone and mechanics of early D&D editions. OSR design emphasizes simplicity, modularity, and a "rulings over rules" philosophy, leading to the creation of retro-clone systems like Labyrinth Lord, Swords & Wizardry, and Old School Essentials.

Parallel to these stylistic developments, the RPG industry has seen dramatic financial growth. Hasbro’s 1998 acquisition of Wizards of the Coast (the current publisher of D&D) signaled mainstream recognition of the hobby’s value. The Open Game License (OGL) launched in the 2000s spurred third-party publishing and broadened the market. Crowdfunding platforms like Kickstarter have since become key funding sources, with projects like Shadowdark raising over $1.5 million. Meanwhile, actual-play shows like Critical Role, The Adventure Zone, and Dimension 20 have expanded RPG audiences globally, helping D&D reach an estimated 85 million players by 2021. Collectively, these trends underscore both the cultural and economic momentum driving the modern RPG landscape.

## Problem Statement
This project intends to make a model that can predict, with at least 75% accuracy, the textual differences between posts scraped from the "RPG" and "OSR" subreddit communities, in order to inform table top industry professionals of factors relevant to TTRPG game development and marketing. 

## Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|post_id|---|---|---|
|title|---|---|---|
|selftext|---|---|---|
|subreddit|---|---|---|
|created_utc|---|---|---|
|is_osr	|---|---|---|
|neg|---|---|---|
|neu|---|---|---|
|pos|---|---|---|
|compound|---|---|---|
|cleaned_selftext|---|---|---|
|cleaned_title|---|---|---|
|text_len|---|---|---|
|word_count|---|---|---|

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

* Future research could explore sentiment analysis on these key terms to measure not only their frequency but the connotation of the document where they appear. This might offer more insight into which terms are postively vs. negatively perceived.

* Consider expanding the dataset to include other platforms like Discord servers, blogs, or forums to verify whether these trends persist beyond Reddit.