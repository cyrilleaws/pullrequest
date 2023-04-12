import requests

# GitHub API endpoint for pull requests
endpoint = 'https://api.github.com/repos/{owner}/{repo}/pulls'

# Replace {owner} and {repo} with the repository details
owner = 'example_owner'
repo = 'example_repo'

# GitHub personal access token for authentication
token = 'your_personal_access_token'

# Get open pull requests
response = requests.get(endpoint.format(owner=owner, repo=repo),
                        params={'state': 'open'},
                        headers={'Authorization': f'token {token}'})

open_prs = response.json()

# Get closed pull requests
response = requests.get(endpoint.format(owner=owner, repo=repo),
                        params={'state': 'closed'},
                        headers={'Authorization': f'token {token}'})

closed_prs = response.json()

# Get draft pull requests
response = requests.get(endpoint.format(owner=owner, repo=repo),
                        params={'state': 'draft'},
                        headers={'Authorization': f'token {token}'})

draft_prs = response.json()

# Print the PRs
print(f'Open PRs: {len(open_prs)}')
print(f'Closed PRs: {len(closed_prs)}')
print(f'Draft PRs: {len(draft_prs)}')

