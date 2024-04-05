from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme" 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        meme_large = data["preview"][-2]
        subreddit = data["subreddit"]
        return meme_large, subreddit
    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)
