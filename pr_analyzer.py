import os
import re
import requests
from typing import Dict, List, Optional, Tuple


def extract_repo_info(pr_url: str) -> Tuple[str, str, int]:
    """Extract owner, repo, and PR number from GitHub URL"""
    pattern = r"github\.com/([^/]+)/([^/]+)/pull/(\d+)"
    match = re.search(pattern, pr_url)
    if not match:
        raise ValueError("Invalid GitHub PR URL format")
    return match.group(1), match.group(2), int(match.group(3))
    
    
def get_pr_changed_files(owner: str, repo: str, pr_number: int) -> List[Dict[str, str]]:
    """Get list of files changed in the PR"""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    response = requests.get(
        url,
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"
                }
        )
    response.raise_for_status()
    return response.json()
    
pr_url = os.getenv('PR_URL')
owner, repo, pr_number = extract_repo_info(pr_url)
changed_files = get_pr_changed_files(owner, repo, pr_number)
print(changed_files)
            
            
            
            
            