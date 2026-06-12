import requests
import sys

# Ensure UTF-8 output encoding for Windows terminals to print emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPOS = [
    "abhisheks008/DL-Simplified",
    "souma9830/SnapPass-AI",
    "asheesh109/KisanAI",
    "anurag3407/career-pilot",
    "Charushi06/StudyPlan",
    "prajwalsuryawanshi/AgentAPI",
    "aayushraj1010/med-genie",
    "imDarshanGK/AI-dev-assistant",
    "yellowgram1543/DoVER"
]

def assign_issues():
    print("=====================================================")
    print("🚀 GSSoC '26 Issue Assignment Automator")
    print("=====================================================")
    
    token = ""
    # Look for token in args (excluding options like -y or --yes)
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    if args:
        token = args[0].strip()
    
    if not token:
        token = input("🔑 Paste your GitHub PAT (starts with ghp_): ").strip()
    if not token:
        print("❌ Error: Token cannot be empty.")
        return

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # First, get the authenticated username
    user_url = "https://api.github.com/user"
    try:
        user_res = requests.get(user_url, headers=headers)
        if user_res.status_code != 200:
            print(f"❌ Invalid token or error fetching user: {user_res.text}")
            return
        username = user_res.json().get("login")
        print(f"👤 Authenticated as: {username}")
    except Exception as e:
        print(f"❌ Error authenticating: {e}")
        return
    
    print("\nFinding your open issues in GSSoC '26 repositories...")
    
    issues_to_comment = []
    
    # Search via GitHub search API to find all open issues created by this user in our target repos
    query = f"author:{username} is:issue is:open " + " ".join([f"repo:{r}" for r in REPOS])
    search_url = f"https://api.github.com/search/issues?q={query}"
    
    try:
        search_res = requests.get(search_url, headers=headers)
        if search_res.status_code == 200:
            items = search_res.json().get("items", [])
            for item in items:
                repo_url = item.get("repository_url")
                repo_name = repo_url.replace("https://api.github.com/repos/", "")
                issue_number = item.get("number")
                title = item.get("title")
                issues_to_comment.append({
                    "repo": repo_name,
                    "number": issue_number,
                    "title": title,
                    "html_url": item.get("html_url")
                })
        else:
            print(f"⚠️ Search API returned status code {search_res.status_code}. Falling back to manual check...")
    except Exception as e:
        print(f"❌ Error searching issues: {e}")

    # Fallback check if search API didn't find anything or failed
    if not issues_to_comment:
        print("No issues found via search. Checking known issue numbers...")
        known_issues = [
            ("aayushraj1010/med-genie", 528),
            ("imDarshanGK/AI-dev-assistant", 1038),
            ("yellowgram1543/DoVER", 77),
            ("abhisheks008/DL-Simplified", 1121),
            ("souma9830/SnapPass-AI", 804),
            ("asheesh109/KisanAI", 98),
            ("anurag3407/career-pilot", 3481),
            ("abhisheks008/DL-Simplified", 1120),
            ("souma9830/SnapPass-AI", 764),
            ("asheesh109/KisanAI", 96),
            ("anurag3407/career-pilot", 3477),
            ("abhisheks008/DL-Simplified", 1119),
            ("souma9830/SnapPass-AI", 763),
            ("asheesh109/KisanAI", 95)
        ]
        for repo, number in known_issues:
            check_url = f"https://api.github.com/repos/{repo}/issues/{number}"
            try:
                res = requests.get(check_url, headers=headers)
                if res.status_code == 200:
                    issue_data = res.json()
                    if issue_data.get("state") == "open":
                        issues_to_comment.append({
                            "repo": repo,
                            "number": number,
                            "title": issue_data.get("title"),
                            "html_url": issue_data.get("html_url")
                        })
            except Exception:
                pass
    
    if not issues_to_comment:
        print("❌ No open issues found to request assignment for.")
        return
        
    print(f"\nFound {len(issues_to_comment)} open issue(s):")
    for idx, issue in enumerate(issues_to_comment, 1):
        print(f"{idx}. [{issue['repo']}] #{issue['number']}: {issue['title']}")
        
    confirm = ""
    if "-y" in sys.argv or "--yes" in sys.argv:
        confirm = "y"
    else:
        confirm = input("\nDo you want to post '/assign gssoc' comment on these issues? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return
        
    for issue in issues_to_comment:
        repo = issue["repo"]
        number = issue["number"]
        comment_url = f"https://api.github.com/repos/{repo}/issues/{number}/comments"
        
        payload = {"body": "/assign gssoc"}
        print(f"\nPosting '/assign gssoc' comment on {repo} #{number}...")
        try:
            res = requests.post(comment_url, json=payload, headers=headers)
            if res.status_code == 201:
                print(f"🎉 Success! Comment posted.")
                print(f"🔗 View here: {issue['html_url']}")
            else:
                print(f"❌ Failed to comment. Status code: {res.status_code}")
                print(f"Response: {res.text}")
        except Exception as e:
            print(f"❌ Error communicating with GitHub API: {e}")

if __name__ == "__main__":
    assign_issues()
