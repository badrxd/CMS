import matplotlib.pyplot as plt


def generate_and_save_pie_chart():
    # Data for the pie chart
    labels = ['', '',
              '']
    sizes = [77, 40, 11]
    colors = ["#1C4E80", "#0091D5", 'lightskyblue']
    explode = (0, 0, 0.05)  # explode the 1st slice (Category A)

    fig, ax = plt.subplots(figsize=(10, 10))
    # ax.set_aspect('equal')
    # Create a pie chart

    font_properties = {
        # Font family (e.g., 'serif', 'sans-serif', 'monospace')
        # Font weight ('normal', 'bold', 'heavy', 'light', 'ultrabold')
        'weight': 'bold',
        'style': 'italic',       # Font style ('normal', 'italic', 'oblique')
        'size': 40,           # Font size
        'color': "#ecf0f1"
    }
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', shadow=True, startangle=140, textprops=font_properties)

    # Add a title

    # Save the pie chart as a PNG file
    plt.savefig('resources/icons/income.png', transparent=True)

    # Show the pie chart (optional)
    plt.show()


# Generate and save the pie chart
# generate_and_save_pie_chart()


def generate_and_save_plot():

    font_properties = {
        # Font family (e.g., 'serif', 'sans-serif', 'monospace')
        # Font weight ('normal', 'bold', 'heavy', 'light', 'ultrabold')
        'weight': 'bold',
        'style': 'italic',       # Font style ('normal', 'italic', 'oblique')
        'size': 40,           # Font size
        'color': "#ecf0f1"
    }
    x = [1, 2, 3, 4, 5]

    y1 = [2, 4, 6, 8, 10]
    y2 = [1, 2, 1, 2, 1]

    # Create two lines with different styles and labels
    fig, ax = plt.subplots()

    ax.plot(x, y1, label='custmers', linestyle='-',
            marker='o', color="#1C4E80")
    ax.plot(x, y2, label='amonth', linestyle='--',
            marker='x', color="#0091D5")

    ax.grid(True, linestyle='--', alpha=0.7)

    border_color = "#ecf0f1"  # Set the desired color
    ax.spines['top'].set_color(border_color)
    ax.spines['bottom'].set_color(border_color)
    ax.spines['left'].set_color(border_color)
    ax.spines['right'].set_color(border_color)

    # Add a legend
    plt.legend()
    # Save the plot as a PNG file
    plt.savefig('resources/icons/cars.png', transparent=True)

    # Show the plot
    plt.show()


# Generate and save the plot
generate_and_save_plot()
