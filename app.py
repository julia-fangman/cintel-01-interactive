import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns

# Add page options for the overall app
ui.page_opts(title="Julia's PyShiny App with Plot", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram
    # The ui.input_slider functions is called with 5 arguments: 
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input
    # 2. A string label ("Number of bins") to be displayed alongside the slider
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initial value fo the slider
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)
    

# Define a plot function for rendering a histogram
@render.plot(alt="Histogram Chart")
def draw_histogram():
    count_of_points = 224
    np.random.seed(1)
    random_data_array = 224 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="pink")
    plt.title("Random Histogram")
    plt.xlabel("Value")
    plt.ylabel("Density")

# Define a plot function for rendering a scatterplot
@render.plot(alt="Random Scatterplot Chart")
def scatterplot():
    count_of_points = 224
    np.random.seed(1)
    x = np.random.randn(count_of_points)
    y = np.random.randn(count_of_points)
    sns.scatterplot(x=x, y=y, color='yellow')
    plt.title("Random Scatterplot")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

# Define a plot function for rendering a heatmap
@render.plot(alt="Heatmap Chart")
def draw_heatmap():
    # Generate random data for the heatmap
    data = np.random.rand(10, 8)
    sns.heatmap(data, cmap="YlGnBu")
    plt.title("Random Heatmap")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
