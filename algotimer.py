from flask import Flask, render_template
from algorithms import *
from timeit import Timer
import random

# get flask app
app = app = Flask(__name__)

# define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sorting-algorithms")
def sorting_algorithms():

    # Creates a list of randomly generated numbers from -100 to 1000 size from 100 to 100000
    list = [random.randrange(-100, 1000) for i in range(random.randint(100, 2000))]

    # Grab benchmark of sorting algorithms
    data = {}

    data["Bubble Sort"] = Timer(lambda : bubble_sort(list)).timeit(number = 1)
    data["Selection Sort"] = Timer(lambda : selection_sort(list)).timeit(number = 1)
    data["Insertion Sort"] = Timer(lambda : insertion_sort(list)).timeit(number = 1)
    data["Radix Sort"] = Timer(lambda : radix_sort(list)).timeit(number = 1)
    data["Quick Sort"] = Timer(lambda : quick_sort(list, 0, len(list) - 1)).timeit(number = 1)
    data["Merge Sort"] = Timer(lambda : merge_sort(list)).timeit(number = 1)

    return render_template("results.html",
        table_title="Benchmark of Sorting Algorithms",
        table_subtitle="Executed on a List of " + str(len(list)) + " Randomly Generated Values",
        data=data)

@app.route("/levenshtein-distance")
def levenshtein_algorithm():

    # Get 2 random words from word list
    word_A = words[random.randint(0, len(words) - 1)]
    word_B = words[random.randint(0, len(words) - 1)]

    # Benchmark edit distance algorithm
    data = {}

    data["Levenshtein Distance"] = Timer(lambda : levenshtein_distance(word_A, word_B, len(word_A), len(word_B))).timeit(number=1)

    return render_template("results.html",
        table_title="Benchmark of Levenshtein Distance",
        table_subtitle="Executed on the words \"" + word_A + "\" and \"" + word_B + "\"",
        data=data)

# run app
if __name__ =="__main__":
    app.run(debug=True)
