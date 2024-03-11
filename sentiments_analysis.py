# Import libraries/modules.
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import matplotlib.pyplot as plt

# Load the model.
nlp = spacy.load('en_core_web_sm')

# Add the SpacyTextBlob extension to the pipeline.
nlp.add_pipe('spacytextblob')

def remove_stopwords(text):
    """ Removes stop words from the review data.

    Args:
        text (str): The review data text with stop words.

    Returns:
        str: The review data text with stop words removed.
    """
    if pd.isna(text):
        return ""
    try:
        doc = nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]
        return ' '.join(tokens)
    except ValueError as ve: 
        print("ValueError processing text:", text)
        print("Error message:", ve)
        return ""
    except TypeError as te:
        print("TypeError processing text:", text)
        print("Error message:", te)
        return ""
 
def categorise_sentiment(score):
    """ Categorise sentiment scores into positive, negative, or neutral.

    Args:
        score (float): The sentiment score.

    Returns:
        str: The sentiment category positive if >0, negative if <0, or neutral if 0).
    """
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

def reviews_data_analysis(text):
    """ Analyse the sentiment of the review data.

    Args:
        text (str): The review data for sentiment analysis.

    Returns:
        float: The sentiment score of the review data, categorised as positive, negative or neutral.
    """
    doc = nlp(text)
    sentiment_score = doc._.polarity
    return  categorise_sentiment(sentiment_score)

# Load the dataset, explicitly specifying data types for 'id' and 'reviews.dateSeen'.
dataframe = pd.read_csv("amazon_product_reviews.csv", dtype={1: str, 10: str})

# Select the 'review.text' column.
reviews_data = dataframe['reviews.text']

# Apply remove_stopwords function to remove stopwords from each review in the 'reviews_data' column.
clean_reviews_data = reviews_data.apply(remove_stopwords)

# Clean the data by removing missing values in the 'reviews_data' column.
clean_data = dataframe.dropna(subset=['reviews.text'])

# Apply the sentiment analysis function to each review in 'clean_reviews_data'.
sentiment_scores = clean_reviews_data.apply(reviews_data_analysis)

# Test results with 20 reviews.
test_reviews = clean_reviews_data.head(20) 

# Print the reviews and their sentiment scores.
for review, score in zip(test_reviews, sentiment_scores.head(20)):
    print("Review:", review)
    print("Sentiment Score:", score)
    
# Plot a histogram of sentiment scores.
plt.hist(sentiment_scores, bins=10)
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Distribution of Sentiment Scores')
plt.show()
