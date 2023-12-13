from tkinter import filedialog
import tkinter as tk
from perform_sentiment_analysis import perform_sentiment_analysis
from create_sentiment_graph import create_sentiment_graph
from news_summarization import news_summarization

def close_window():
    root.destroy()

def select_file_and_create_graph():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            sentiment_scores = perform_sentiment_analysis(file_path)
            create_sentiment_graph(file_path, sentiment_scores, root)

            with open(file_path, 'r') as file:
                news_article = file.read()

            summary = news_summarization(news_article)

            # Create the summary label
            summary_label = tk.Label(root, text=summary, wraplength=400)
            # Pack the summary label (but don't show it immediately)
            summary_label.pack_forget()

            # Function to show the summary label
            def show_summary():
                summary_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            # Create a button to show the summary
            show_summary_button = tk.Button(root, text="Show Summary", command=show_summary)
            show_summary_button.pack()

            # Exit button to close the window
            exit_button = tk.Button(root, text="Exit", command=close_window)
            exit_button.pack()

    except Exception as e:
        # Handle specific exceptions or display a general error message
        error_label = tk.Label(root, text=f"Error: {str(e)}")
        error_label.pack()

root = tk.Tk()
root.title("Sentiment Analysis Visualizer")
root.attributes('-fullscreen', True)  # Open window in full screen

plot_button = tk.Button(root, text="Select File for Sentiment Analysis", command=select_file_and_create_graph)
plot_button.pack()

root.mainloop()
