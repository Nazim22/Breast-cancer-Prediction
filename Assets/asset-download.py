import urllib.request

# URL of the CSS file on GitHub
css_url = 'https://raw.githubusercontent.com/alejandro-ao/streamlit-cancer-predict/6438cbee63241483b6a43dc1b9abad8390820b80/assets/style.css'

# Local path to save the downloaded CSS file
local_path = r'C:\Users\techn\.spyder-py3\Project-1\Assets\style.css'

# Download the CSS file and save it to the local path
urllib.request.urlretrieve(css_url, local_path)

print(f"CSS file downloaded and saved to: {local_path}")
