import praw
import prawcore

user_agent = "Sub-Scriber script 1.0 written by Edward Brace"
try:
    reddit = praw.Reddit(
        client_id="CLIENT-ID",
        client_secret="CLIENT-SECRET",
        password="YOUR-PASSWORD",
        user_agent=user_agent,
        username="YOUR_USERNAME"
    )
    name = reddit.user.me().name
except prawcore.exceptions.ResponseException:
    print("Log-in failed!")
    exit(1)

filename = input("Logged-in as /u/" + name + "\nEnter path of text file: ")
try:
    file = open(filename, "r")
except FileNotFoundError:
    print("File " + filename + " does not exist.")
    exit(1)
#main loop that accesses + joins each listed subreddit
while True:
    line = file.readline().strip()
    if line == "": #end condition
        break

    if line[:2] == "r/":
        line = line[2:]

    try:
        reddit.subreddit(line).subscribe()
        print(line + " joined successfully")
    except prawcore.exceptions.NotFound:
        print(line + " cannot be found.")

file.close()