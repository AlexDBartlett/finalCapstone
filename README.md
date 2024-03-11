Sentiment Analysis of Amazon Product Reviews

DESCRIPTION

This project performs sentiment analysis on Amazon product reviews using Python. 
Sentiment analysis is crucial for understanding the opinions, emotions, and attitudes expressed in textual data. 
By analyzing sentiment, we can gain insights into customer feedback, identify trends, and make data-driven decisions to improve products or services.

INSTALLATION

To install and run this project locally, follow these steps:

Clone this repository to your local machine:
git clone https://github.com/AlexDBartlett/finalCapstone.git

Install the required dependencies by running:

pip install pandas 
pip install spacy 
pip install spacytextblob 
pip install matplotlib

Download the English language model for spaCy by running:
python -m spacy download en_core_web_sm

USAGE 

After installing the project, you can use it as follows:

Ensure you have the necessary Python libraries/modules installed: pandas, spacy, spacytextblob, and matplotlib.
Run the script sentiment_analysis.py to analyze the sentiment of Amazon product reviews.
The script will load the dataset amazon_product_reviews.csv and perform sentiment analysis on the reviews. 
It will categorize each review as positive, negative, or neutral based on its sentiment score.
The sentiment scores and their corresponding categories will be printed to the console, along with a histogram visualizing the distribution of sentiment scores.

Credits
Author: Alex Bartlett
GitHub Repository: https://github.com/AlexDBartlett/finalCapstone
