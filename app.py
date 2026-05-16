from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():

    user_data = None
    repos = []

    if request.method == 'POST':

        username = request.form['username']

        # GitHub User API
        user_url = f"https://api.github.com/users/{username}"

        response = requests.get(user_url)

        if response.status_code == 200:

            user_data = response.json()

            # Fetch Repositories
            repo_url =
                f"https://api.github.com/users/{username}/repos"

            repo_response = requests.get(repo_url)

            repos = repo_response.json()

    return render_template(
        'index.html',
        user=user_data,
        repos=repos
    )

if __name__ == '__main__':
    app.run(debug=True)
