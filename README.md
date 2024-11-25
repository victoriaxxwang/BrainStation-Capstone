# Sentiment Analysis of Product Reviews

### Describe your project (big idea)
-Leveraging text data to predict customer sentiment and product success

### Describe your goal
-In the past decade, there is an exponential growth in online purchases and E-commerce platforms. Hence, Ecommerce platforms are tasked with figuring out how customers feel about their brand, the services and product they offer. The relationship between customer sentiments and factors that influence them is valuable. Sentiment analysis allows for product-customer fit, which translates to sales and profit. According to the Statista Research Department, by 2029, the revenue in the e-commerce market in the US is estimated to reach 1.9 trillion dollars. So despite the fierce competition, there’s a lot of opportunities in the e-commerce market. We want to take advantage of these opportunities by extracting data driven insights via customer sentiment to iteratively improve product-customer fit. 

According to a 2024 survey that focus on the most profit Amazon sellers worldwid by product category from December 2023 to January 2024, the beauty and personal care category topped the chart. (https://www.statista.com/statistics/1400287/amazon-most-profitable-sellers-category/#:~:text=A%202024%20survey%20found%20that,with%2027%20percent%20of%20sellers.)

Hence, for this project, we will focus on the beauty and personal care category for this sentiment analysis of product reviews to see how we can leverage data to predict customer sentiment and product success.

### Describe your data
-For my capstone, I will be using an Amazon Review dataset from UCSD (https://amazon-reviews-2023.github.io/index.html#). Data dictionaries is also included in the website.

-The Amazon review dataset is a rich, relatively clean dataset. There are many categories of products to choose from. I conducted my EDA on the beauty category for sprint1, but decided to switch to beauty and personal care category due to its business value. We want to extract insights to better understand what about those products they are making them so profitable.

### Describe your work (models, analysis, EDA, etc.)
-Below are the variables assessed in the EDA: 
From User Reviews: df BP
1. `user_id` : ID of reviewer --> 1) No demographic data to do customer segmentation. This serves as unique reviewer identifier.
2. `rating` : Rating from of product from 1.0 to 5.0 --> 1) Convert float to integer 2) Convert rating to sentiment buckets
3. `title_x` : Title of the user review --> 1) Assess the relationship between the title & rating? How does that compare w/ text & rating?
4. `text` : Text body of the user review --> 1) Assess the relationship between the title & rating? How does that compare w/ text & rating?
5. `timestamp` : Time of review in unix time -->1) Convert to datetime (new column name time & set it as the index) to assess how other variables change with time. Break down the time into Year, Month and Week of Year.
6. `verified_purchase` : User purchase verification --> 1) Assess the distribution of other variable per yes or no purchase verification.
7. `helpful_vote` : Reviews that are voted to be helpful --> 1) Assess the relationship between variables and if the review is helpful.

From Item Metadata: df BP meta :
1. `average_rating` : Rating of product shown on the product page.
2. `price` : Price of product in US dollars (at time of crawling or scraping)
3. `rating_number` : Number of ratings given for the product

**From basic EDA, the following insights were extracted:**
1. The distribution of rating is a bit skewed towards higher ratings. 
2. In general, customers are happy with the products, where their average rating is centered around 4. 
3. When looking at total number of ratings by years from 2003 to 2023, there is a dramatic increase after 2017, which was when Amazon launched the "Early Reviewer Program" that incentivized customers with gift cards to leave product reviews. This highlights the importance E-commerce giants are placing on customer reviews and customer sentiment for business success and growth. 
4. When looking at a preliminary extraction of the top 20 positive and negative sentiments from the reviews. We can potenitally gather insights on what is currently working well and what are potential areas of improvement. 

After assessing the data via EDA, the variables are categorized into text, continuous, categorical or others. `text` and `sentiment` (target variable) are the essential variables for our binary classification. In other words, what features within the text provided by the reviewers are predictive of the customer's positive (rating or negative towards the product.

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

In terms of modeling, the data was preprocessed via using 1) TFIDF with SVD  as well as 2) CountVectorizer. Base Modeling with Logistic Regression, Random Forest and AdaBoostClassifier were performed in sprint 2. These models were compared via model accuracy score. 

### Describe your results
For sprint 2, comparing the accuracy scores of logistic regression, Adaboost classifer and Random Forest classifer across data preprocessed using TFIDF with SVD and CountVectorizer, Random Forest classifer resulted the highest score accuracy, at 87.1%, and the train model was not overfitted. 

In sprint 3, we will preprocess the text data using representation learning via sentence2vec and perform downstream baseline modelings. The models will be tuned via their respective hyperparameters using GridSearch. In additional to comparing the models via accuracy scores, we will use ROC curves to compare how well the classification models balance between the misses in precision and recall. We will prioritize recall despite the risk of increased false positives because we want to identify as many positive reviews as possible. Moreover, besides focusing on binary classifiers and evaluating them using accuracy scores, we will perform other types of models to extract additional insights and they include cluster analysis, Sequential Neural Network via Keras and topic modeling using BERT.

### Party!
