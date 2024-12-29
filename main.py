# main.py
import json
import random

# Simulating scraping X data
def scrape_tweets(usernames):
    data = []
    for user in usernames:
        user_data = {
            "username": user,
            "followers": random.randint(100, 10000),
            "avg_tweets_per_day": random.randint(1, 20),
            "tweets": [
                {
                    "tweet_id": f"{user}_tweet_{i}",
                    "content": f"Sample tweet content {i} from {user}",
                    "replies": random.randint(0, 50),
                }
                for i in range(5)  # Simulate 5 tweets per user
            ],
        }
        data.append(user_data)
    return data

# Save data to JSON
def save_to_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    users = ["creator1", "creator2", "creator3"]
    twitter_data = scrape_tweets(users)
    save_to_json(twitter_data)
    print("Data collection complete. Saved to data.json.")

