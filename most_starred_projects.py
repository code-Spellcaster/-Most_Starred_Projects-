import requests
import plotly.express as px

# Perform an API request to GitHub to retrieve information about repositories.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Ensure the API response does not contain incomplete results.
response_dict = response.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Extract and process information from each repository.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Convert repository names into clickable links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    # Store the number of stars each repository has received.
    stars.append(repo_dict['stargazers_count'])

    # Prepare hover text with owner login and description for visualization.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Create a bar chart visualization of the most-starred Python projects on GitHub.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

# Customize the layout and appearance of the chart.
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Display the visualization.
fig.show()
