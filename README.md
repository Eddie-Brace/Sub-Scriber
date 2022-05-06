# Sub-Scriber
A Reddit bot that automates subscribing a user to a list of subreddits    
The newer version of [this project.](https://github.com/Eddie-Brace/SubredditSubscriber)   
The old script is much more heavyweight, but you may find it useful if you are adverse to using the Reddit API.

Create text file w/ list of subs to subscribe to:
```
r/nuclear
r/redscarepod
r/geopolitics
r/dogelore
```
Sub names should be seperated only by whitespace and "r/" as shown above. This can be done easily by copying the subreddit list (top-left of page) from your old account, chopping off the ends, and using find-all to replace "Subreddit Icon" with a blank string.   

Next, [register a Reddit app](https://www.reddit.com/prefs/apps) and paste the relevent information into the Python script.
Run as:
```bash
pip install praw
python3 Sub-Scriber.py
```
