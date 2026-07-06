import feedparser, requests, random, json, os, re
from google import genai
from google.genai import types
from dotenv import load_dotenv 


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   
load_dotenv(os.path.join(BASE_DIR, ".env"))
with open(os.path.join(BASE_DIR, "config.json"), encoding="utf-8") as f:
    config = json.load(f)


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
MODEL_NAME = config["model_name"]
BASE_PROMPT = config["base_prompt"]
TOPICS = config["topics"]


client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(timeout=60_000)  # ۶۰ ثانیه
)


def summarize(topic, news): 
    prompt = BASE_PROMPT + f" Topic: {topic}\n\n{news} "
    
    try: 
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text 
    except Exception as e: 
        print(f"Gemini Error: {e}")
        return f"Gemini Error: {e}"


def clean_html(text):
    return re.sub(r"<[^>]+>", "", text or "")[:500]


def collect_news():
    topic, feeds = random.choice(list(TOPICS.items()))
    entries = []
    for url in feeds:
        entries += feedparser.parse(url).entries[:4]
    random.shuffle(entries)
    news = "\n\n".join(
        f"title: {e.title}\n  body: {clean_html(e.get('summary', ''))}"
        for e in entries[:6]
    )
    return topic, news


def send(text):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": TARGET_CHAT_ID, "text": text},
        timeout=30
    )
    



if __name__ == "__main__":
    try:
        topic, news = collect_news()
        summary = summarize(topic, news)
        send(f"📰 {topic}\n\n{summary}")
    except Exception as e:
        print("error: ", e)



