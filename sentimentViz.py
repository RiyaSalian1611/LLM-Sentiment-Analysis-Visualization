import numpy as np
import matplotlib.pyplot as plt

# Function for visualizing sentiment scores
def visualize_sentiment_scores(text, sentiment):
    # Extracting sentiment scores
    negative_score = sentiment['negative']
    neutral_score = sentiment['neutral']
    positive_score = sentiment['positive']

    # Creating labels and scores
    labels = ['Negative', 'Neutral', 'Positive']
    scores = [negative_score, neutral_score, positive_score]
    colors = ['red', 'gray', 'green']

    # Creating a horizontal bar chart
    plt.barh(labels, scores, color=colors)
    plt.xlabel('Sentiment Score')
    plt.title('Sentiment Analysis for: ' + text)

    # Adding sentiment scores as text on bars
    for i, score in enumerate(scores):
        plt.text(score, i, f'{score:.2f}', ha='left', va='center')

    plt.show()

# Example usage
text = "I love spending time with my friends."
sentiment = {
    'negative': 0.1,
    'neutral': 0.2,
    'positive': 0.7
}
visualize_sentiment_scores(text, sentiment)
