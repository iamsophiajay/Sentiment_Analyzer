"""
This is a Flask application that performs sentiment analysis on user-provided text.
It provides a route for analyzing text sentiment and another for rendering the index page.

The application communicates with a sentiment analysis service to evaluate the sentiment
of the text, returning the sentiment label and score.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyzes the sentiment of the given text and returns the sentiment label and score.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."

    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Renders the index page of the sentiment analysis app.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
