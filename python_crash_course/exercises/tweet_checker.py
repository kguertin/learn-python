max_chars = 140
tweet = input("Enter your tweet: ")
if len(tweet) <= max_chars:
    print(f"That {len(tweet)} char tweet will work!")
else: 
    print(f"Your {len(tweet)} char tweet is {len(tweet) - max_chars} too long!")