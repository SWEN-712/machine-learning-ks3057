#### machine-learning-ks3057 created by GitHub Classroom

# Analyzing accessibility tweets 

## Overview

The need for this project:
1. To mine Twitter for accessibility related tweets from users involved in the field.
2. To collect data for accessibility that can be used for research.


The scripts analyses accessibility tweets from three twitter users:
1. Jenny Lay-Flurrie<br> Chief Accessibility Officer at Microsoft<br>
   @jennylayfluffy 
2. Victor Tsaran <br> Sr. Technical Program Manager, Material Design,
   accessibility at Google<br> @vick08
3. Molly Burke <br>Youtuber and Accessibility Activist
   <br>@MollyBOfficial

On running the analysis scripts, you will get:
1. Total tweets analysed
2. Top 10 tweets with negative and positive sentiment
3. Word Cloud of tweets
   
On running the hashtag script, you will get:
1. Union of all three users' hashtags
2. Intersection of all three users' hashtags

## Generation
1. Please add your Twitter and Microsoft Azure API keys, marked by XXX
   by editing the scripts.
2. When entering the azure url, please ensure that it is the endpoint
   for sentiment analysis
3. Please go over requirements.txt for all dependencies and ensure they
  are installed

###### 1.  analyse_jenny_tweets.py
    
    EXAMPLE:
    ```
    python3 analyse_jenny_tweets.py
    ```

###### 2.  analyse_victor_tweets.py
    
    EXAMPLE:
    ```
    python3 analyse_victor_tweets.py
    ```

###### 3.  analyse_molly_tweets.py
    
    EXAMPLE:
    ```
    python3 analyse_molly_tweets.py
    ```

###### 4.  common_hashtags.py
    
    EXAMPLE:
    ```
    python3 common_hashtags.py
    ```
