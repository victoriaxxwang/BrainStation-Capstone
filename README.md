# Enhancing Customer Satisfaction with Data-Driven Product Insights
By Victoria X. Wang, December 2024, BrainStation Capstone

### Project Description
Project Overview: Leveraging Sentiment Analysis and Similarity Search to Optimize Product offerings and success

In the past decade, there is an exponential growth in online purchases and E-commerce platforms. Hence, E-commerce platforms are tasked with figuring out how customers feel about their brand, the services and product they offer. The relationship between customer sentiments and factors that influence them is valuable. Sentiment analysis allows for product-customer fit, which translates to sales and profit. According to the Statista Research Department, by 2029, the revenue in the E-commerce market in the US is estimated to reach 1.9 trillion dollars. So despite the fierce competition, there’s a lot of opportunities in the E-commerce market. We want to take advantage of these opportunities by extracting data driven insights via customer text reviews to iteratively improve product-customer fit.

According to a 2024 survey that focus on the most profit Amazon sellers worldwid by product category from December 2023 to January 2024, the beauty and personal care category topped the chart.

Hence, for this project, we will focus on the beauty and personal care category for analysis of the text reviews to predict customer sentiment and product success.

### Project Goal
Our problem statement is: How might we leverage user text reviews to identify product issues and prioritize features that customers value the most?

My solution is to use machine learning and NLP to analyze customer sentiment and extract insights. This will result in a Review Analyzer App for various stakeholders to enhance customer-product fit and satisfaction with data-driven product insights.

Of note, given the limited computational power of my personal computer, I will subset the dataset to 1% (165674, 16) and utilize Google Colab for mapping text to 384-dimension embeddings via the Sentence Transformer model ('all-MiniLM-L6-v2').

### Dataset Description
I used the Amazon Review dataset from UCSD (https://amazon-reviews-2023.github.io/index.html#). 

The Amazon review dataset is a rich, relatively clean dataset. There are many categories of products to choose from. I focused on the beauty and personal care category. Given its business value, we are looking to extract insights to better understand features of those products that makes them so profitable.

### Data Exploration, Cleaning and Wrangling
**Please see below for a basic description of each variable**
**From User Reviews: df BP : 'BP.csv'**
1. `user_id` : ID of reviewer --> 1) No demographic data to do customer segmentation. This serves as unique reviewer identifier. 
2. `rating` : Rating from of product from 1.0 to 5.0 --> 1) Convert float to integer 2) Convert rating to sentiment buckets 
3. `title_x` : Title of the user review
4. `text` : Text body of the user review --> 1) Sentiment Analysis & Review Analyzer 
5. `timestamp` : Time of review in unix time -->1) Convert to datetime (new column name `time` & set it as the index) to assess how other variables change with time. Break down the `time` into `Year`, `Month` and `Week of Year`.
6. `verified_purchase` : User purchase verification 
7. `helpful_vote` : Reviews that are voted to be helpful 

**From Item Metadata: df BP_meta : 'BP_meta.csv'**
1. `average_rating` : Rating of product shown on the product page. 
2. `price`: Price of product in US dollars (at time of crawling or scraping) 
3. `rating_number`: Number of ratings given for the product

**The variables are then categorized into text, continuous, categorical or others. `text` and `sentiment` (target variable) are the essential variables for our binary classification.**

**Text:**
1. `title_x` = title given by the reviewer for their review
2. **`text` = body of text of the review**

**Continuous variables:**
1. `rating` = 1-5 
2. `helpful_vote` = number of counts a review has received a vote stating it as helpful
3. `average_rating` = average rating per product
4. `price` = price of product 
5. `rating_number`= number of rating a product has
6. `timestamp`= datetime that was extracted to `year`, `month` and `week_of_year`
8. `year` = year the review was written
9. `month`= month the review was written
10. `week_of_year`= week of year the review was written

**Categorical variables:**
1. `verified_purchase` = true (purchase was verified) and false (purchase not verified)
2. **`sentiment` = y = target variable, positive sentiment =1 (rating=3,4,5), negative sentiment =0 (rating=1,2)**

**Others:**
1. `user_id` = unique identifier of the reviewer
2. `parent_asin` = unique identifier that allow for the merging metadata and user review data.

**The following insights were extracted from EDA:**
1. The mean of `rating` is 4.13, which means reviewers tend to lend towards favorite ratings in the Beauty and Personal Care category.
2. The mean of `average_rating`, which is the rating of product shown on the product page, is 4.38. This is slightly higher than the actual mean of `rating`, which is 4.13.
3. The average `price` of the products are $24.66.
4. The mean of the `rating_number` shows that on average there's 10524 reviews per product, which gives us confidence that insights extracted from the review would be helpful and provide a solid representation on how the customers feel about the products.
5. The timestamps for the review range from 4/1/2000 to 9/13/2023.
6. Most (50% of the distribution) of the reviews are written in 2020, across the month of June or the 25th week of the year.

The X variable is text reviews and y, our target variable, is customer sentiment. A rating of 1-2 was bucked as negative (0) and 3-5 as positive (1). 

The text data were preprocessed using 1) Count Vectorizer, 2) TFIDF with SVD for dimensionality reduction and 3) a pretained Sentence Transformer model with 384 dimensions (‘all-MiniLM-L6-v2’).

<img width="538" alt="Class_Imbalance" src="https://github.com/user-attachments/assets/c50d4576-45f6-4aa6-8af3-19d9e0c4f2fc">

Of note, the dataset is imbalanced, with 80% positive reviews. To address this, I used AUC as the model performance metric and in addition to logistic regression, I used ensemble methods like XGBoost and Random Forest.

### Results and Model Evaluation
<img width="1145" alt="Screenshot 2024-12-08 at 6 10 53 PM" src="https://github.com/user-attachments/assets/2bb2f594-b15f-4b4f-90c8-8a53c4f4b119">

### Reviewer Analyzer Demo-Positive Review Example 
<img width="1150" alt="Positive_Sentiment_Screenshot" src="https://github.com/user-attachments/assets/3e6410f1-aad0-4a6a-976f-805cc08778de">

### Reviewer Analyzer Demo-Negative Review Example
<img width="1150" alt="Negative_Sentiment_Screenshot" src="https://github.com/user-attachments/assets/53bcde3f-0719-4aa4-8af3-7a21f34f5d78">

### Conclusion 
The Reviewer Analyzer app will empower stakeholders to gain actionable insights that can be used to improve product-market fit, outperform competitors, and drive revenue growth.

### Future Direction 
1. We can improve the reviewer simiarity research by resolving the edge cases and optimizing embedding transformation and similarity calculations.
2. We can extract additional insights via other modeling techniques such as cluster analysis, Sequential Neural Network via Keras and Topic Modeling.

### Citations 
Data Set Citation: McAuley Lab Amazon Reviews'23
@article{hou2024bridging, title={Bridging Language and Items for Retrieval and Recommendation}, author={Hou, Yupeng and Li, Jiacheng and He, Zhankui and Yan, An and Chen, Xiusi and McAuley, Julian}, journal={arXiv preprint arXiv:2403.03952}, year={2024} }
https://amazon-reviews-2023.github.io/index.html#

SentenceTransformer Library Citation: "Sentence-BERT (all-MiniLM-L6-v2 model)”:
Reimert, N., & Kiela, P. (2019). Sentence-BERT: Sentence Embeddings using Siamese Networks and Triplet Loss. In Proceedings of the 57th Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 4500–4510). Association for Computational Linguistics. (https://aclanthology.org/D19-1410/)

Citation for Statistia E-commerce Market Insights: https://www.statista.com/statistics/272391/us-retail-e-commerce-sales-forecast/

Citation for beauty and personal care category as the most profitable category:
https://www.statista.com/statistics/1400287/amazon-most-profitable-sellers-category/#:~:text=A%202024%20survey%20found%20that,with%2027%20percent%20of%20sellers.)

### Notebooks
1. Part1. Victoria_Wang_Capstone_FullDataSet_EDA
2. Part2. Victoria_Wang_Capstone_01Ssubset_Embeddings
3. Part3. Victoria_Wang_Capstone_01Ssubset_CV_TFIDF
4. Part4. Victoria_Wang_Capstone_NewReviewSentimentPredictor
5. Streamlit App Demo Review Analyzer: Enhancing Customer Satisfaction with Data-Driven Product Insights. (Please refer to the streamlit_app.py file for the demo. The codes from Part4. Victoria_Wang_Capstone_NewReviewSentimentPredictor was transformed into the streamlit_app.py file in order to run the demo.) 




