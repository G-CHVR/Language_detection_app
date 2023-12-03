import re
from datetime import datetime
from pathlib import Path 

html_file_path = Path(__file__).parent / "static/index.html"
deployment_info_placeholder = '<div id="deployment-info"></div>'
deployment_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
UserName = 'GCH'  # You can obtain this dynamically during deployment

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Inject deployment information
html_content = re.sub(re.escape(deployment_info_placeholder), f'''
    <div id="deployment-info">
        <p>Deployment Date: {deployment_date}</p>
        <p>Deployed By: {UserName}</p>
    </div>
''', html_content)

# Write the updated content back to the HTML file
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)
