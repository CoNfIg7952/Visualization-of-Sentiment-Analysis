import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def create_sentiment_graph(file_path, sentiment_scores, root):
    # Extract sentiment scores
    positive = sentiment_scores['pos']
    negative = sentiment_scores['neg']
    neutral = sentiment_scores['neu']

    # Sentiment categories and corresponding scores
    sentiments = ['Positive', 'Neutral', 'Negative']
    scores = [positive, neutral, negative]

    # Assigning colors based on sentiment
    colors = {'Positive': 'g', 'Neutral': 'grey', 'Negative': 'r'}
    color_list = [colors[sent] for sent in sentiments]

    # Create a figure and axis
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')

    # Bar positions on x-axis
    x_pos = np.arange(len(sentiments))

    # Plotting 3D bars
    ax.bar3d(x_pos, [0] * len(sentiments), [0] * len(sentiments), 1, 1, np.abs(scores), color=color_list, alpha=0.8)

    # Adjusting y-axis to accommodate negative values
    ax.set_ylim(0, max(np.abs(scores)))

    # Setting labels and title
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Score')
    ax.set_zlabel('Sentiment Score')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(sentiments)
    ax.set_title('Sentiment Analysis')

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    x_pos = np.arange(len(sentiments))
    ax.bar3d(x_pos, [0] * len(sentiments), [0] * len(sentiments), 1, 1, np.abs(scores), color=color_list, alpha=0.8)
    ax.set_ylim(0, max(np.abs(scores)))
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Score')
    ax.set_zlabel('Sentiment Score')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(sentiments)
    ax.set_title('Sentiment Analysis')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Display the graph on the left side

    root.attributes('-fullscreen', True)  # Open window in full screen

    root.attributes('-fullscreen', True)  # Open window in full screen