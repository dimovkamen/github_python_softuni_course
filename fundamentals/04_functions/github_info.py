import requests


def fetch_user_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        if len(repositories) > 0:
            return repositories
        else:
            return None
    else:
        print(f"ERROR URL: {response.status_code}")
        return None


def display_repo_info(repositories):
    if repositories:
        print("\nUser's Repositories:")
        print(repositories)
        for repo in repositories:
            print()
            print(f"Repo name: {repo['name']}")
            print(f"Repo owner: {repo['owner']['login']}")

def main():
    username = input("Enter username: ")
    repositories = fetch_user_repositories(username)
    if repositories:
        display_repo_info(repositories)
    else:
        print('No repos found.')

if __name__ == '__main__':
    main()
