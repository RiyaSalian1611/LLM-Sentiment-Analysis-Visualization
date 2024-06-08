# Importing the necessary modules
from langchain.llms import OpenAI
import matplotlib.pyplot as plt

# Setting up the OpenAI model
llm = OpenAI()

# Function for sentiment analysis
def analyze_sentiment(text):
    # Perform sentiment analysis using the LLM
    sentiment = llm.sentiment_analysis(text)
    return sentiment

# Function for visualizing sentiment scores
def visualize_sentiment_scores(text, sentiment):
    # Plotting sentiment scores
    labels = ['Negative', 'Neutral', 'Positive']
    sizes = [sentiment['negative'], sentiment['neutral'], sentiment['positive']]
    colors = ['red', 'gray', 'green']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiment Analysis for: ' + text)
    plt.show()

# Example usage
if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

    # Visualizing sentiment scores
    visualize_sentiment_scores(text, sentiment)
