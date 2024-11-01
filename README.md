# Sentiment Analysis of Product Reviews

### Describe your project (big idea)
-Leveraging text data to predict customer sentiment and product success

### Describe your goal
-In the past decade, there is an exponential growth in online purchases and E-commerce platforms. Hence, Ecommerce platforms are tasked with figuring out how customers feel about their brand, the services and product they offer. The relationship between customer sentiments and factors that influence them is valuable. Sentiment analysis allows for product-customer fit, which translates to sales and profit. According to the Statista Research Department, by 2029, the revenue in the e-commerce market in the US is estimated to reach 1.9 trillion dollars. So despite the fierce competition, there’s a lot of opportunities in the e-commerce market. We want to take advantage of these opportunities by extracting data driven insights via customer sentiment to iteratively improve product-customer fit. 

### Describe your data
-For my capstone, I will be using an Amazon Review dataset from UCSD (https://amazon-reviews-2023.github.io/index.html#). Data dictionaries is also included in the website.
-The Amazon review dataset is a rich, relatively clean dataset. There are many categories of products to choose from. I conducted my EDA on the beauty category and intend to expand to other categories as a next step. 

### Describe your work (models, analysis, EDA, etc.)
Below are the variables assessed in the EDA: 
From User Reviews: df BeautyReview : 'AmazonBeautyReview.csv'
1. user_id : ID of reviewer --> 1) No demographic data to do customer segmentation. This serves as unique reviewer identifier.
2. rating : Rating from of product from 1.0 to 5.0 --> 1) Convert float to integer 2) Convert rating to sentiment buckets
3. title_x : Title of the user review --> 1) Assess the relationship between the title & rating? How does that compare w/ text & rating?
4. text : Text body of the user review --> 1) Assess the relationship between the title & rating? How does that compare w/ text & rating?
5. timestamp : Time of review in unix time -->1) Convert to datetime (new column name time & set it as the index) to assess how other variables change with time. Break down the time into Year, Month and Week of Year.
6. verified_purchase : User purchase verification --> 1) Assess the distribution of other variable per yes or no purchase verification.
7. helpful_vote : Reviews that are voted to be helpful --> 1) Assess the relationship between variables and if the review is helpful.

From Item Metadata: df BeautyReviewMeta : 'AmazonBeautyReview_meta.csv'
1. average_rating : Rating of product shown on the product page.
2. price: Price of product in US dollars (at time of crawling or scraping)
3. rating_number: Number of ratings given for the product

From basic EDA, the following insights were extracted: 
-The distribution of rating is a bit skewed towards higher ratings. 
-In general, customers are happy with the products, where their average rating is centered at 4. 
-When looking at total number of ratings by years from 2003 to 2023, there is a dramatic increase after 2017, which was when Amazon launched the "Early Reviewer Program" that incentivized customers with gift cards to leave product reviews. This highlights the importance E-commerce giants are placing on customer reviews and customer sentiment for business success and growth. 
-When looking at a preliminary extraction of the top 20 positive and negative sentiments from the reviews. We can potenitally gather insights on what is currently working well and what are potential areas of improvement. 

### Describe your results
-We are still in the preliminary EDA phase, but below are next steps for the projects.
1. EDA on other categories from the Amazon Customer Review dataset, with the focus on a. distribution of user ratings, b. top sentiment phrases, and c. to increase the diversity of category training set.
2. More in-depth text data analysis techniques, with the focus on a. Sentiment via counting sequence of words, n-grams, b. Word embeddings to create features that group similar words to handle synonyms c. Natural Language Processing (NLP) to extract meaning 

### Party!
