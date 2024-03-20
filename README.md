# Most-Starred Python Projects on GitHub

## Overview

This program is designed to fetch and visualize the most-starred Python projects on GitHub. It uses the GitHub API to retrieve data about repositories that are highly rated by the community, focusing on Python projects. The program then visualizes this data using the plotly library, creating an interactive bar chart that highlights each project's popularity based on the number of stars it has received. Users can hover over each bar to see more details about the project, including the owner's name and the project's description.

## Inspiration

This project is based on the contents and exercises found in "Python Crash Course" by Eric Matthes. It is intended to demonstrate practical applications of Python in accessing web APIs and data visualization techniques. The book serves as an excellent resource for beginners looking to dive into Python programming, covering fundamentals, projects, and various Python libraries.

## Features

- Fetches data on the most-starred Python projects from GitHub's API.
- Visualizes the data using an interactive bar chart with hoverable links and descriptions.
- Displays the repository name, owner, and the number of stars in a clear, engaging format.

## Installation

To run this program, you need to have Python installed on your system along with the following libraries:

- `requests`
- `plotly`
- `pandas` (included for potential future data manipulation features)

To install these dependencies, run the following command in your terminal: `pip install -r requirements.txt`

## Usage

To execute the program, simply run the Python script from your terminal: `python most_starred_projects.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
