import requests
import json
from bs4 import BeautifulSoup
from langdetect import detect

API_KEY = "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"

def scrape_website(url):
    """Extract text content from a webpage"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove scripts and styles
        for tag in soup(["script", "style"]):
            tag.decompose()
            
        # Extract text and limit to 5000 characters
        text = " ".join(soup.stripped_strings)[:5000]
        return text
    except requests.RequestException as e:
        return f"Error fetching website: {e}"

def summarize_text(text, length="medium"):
    """Generate bullet-point summary with specified length"""
    try:
        lang = detect(text)
    except Exception:
        lang = "en"
    
    # Map length to bullet point count
    length_map = {
        "short": 3,
        "medium": 5,
        "long": 7
    }
    
    # Enhanced prompt for bullet-point summaries without bold subheadings
    prompt = (
        f"Create a concise summary in {lang} using bullet points. "
        f"Provide exactly {length_map[length]} key points in simple, engaging language. "
        f"Focus on main ideas and avoid technical terms. "
        f"Text:\n{text}\n\nSummary:\n- "
    )
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": "qwen/qwen2.5-vl-72b-instruct:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"], lang
    except requests.RequestException as e:
        return f"Error summarizing text: {e}", lang 

def main():
    url = input("Enter website URL (or 'exit' to quit): ")
    if url.lower() == 'exit':
        return
    
    if not url.startswith(('http://', 'https://')):
        print("Please enter a URL starting with http:// or https://")
        return
    
    # Get summary length preference
    while True:
        length = input("Choose summary length (short/medium/long): ").lower()
        if length in ["short", "medium", "long"]:
            break
        print("Invalid choice. Please choose from short, medium, or long.")
    
    print("\nFetching and summarizing content... Please wait...")
    text = scrape_website(url)
    
    if "Error fetching" in text:
        print(f"\nError: {text}")
        return
    
    summary, lang = summarize_text(text, length)
    print(f"\n{'='*50}")
    print(f"Summary ({lang.upper()} - {length.capitalize()}):")
    print(f"{'-'*50}")
    print(summary)
    print(f"{'='*50}")

if __name__ == "__main__":
    main()