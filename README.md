# 🌐 Web Summarizer with OpenRouter

A Python-based NLP project that scrapes web content and generates concise bullet-point summaries using the OpenRouter API. This tool is perfect for quickly distilling lengthy articles or web pages into digestible key points.

## 🔍 Overview
**Web Summarizer with OpenRouter** automates the process of:

- **Scraping** text content from any webpage using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
- **Cleaning** the extracted text by removing unnecessary elements.
- **Detecting** the language of the text with [langdetect](https://pypi.org/project/langdetect/).
- **Generating** a bullet-point summary using the OpenRouter API with adjustable summary lengths.

This project is ideal for gathering key insights from online content without needing to manually read and filter through large amounts of text.

---

## ✨ Features
- **🌐 Web Scraping:** Retrieves and processes webpage text while removing scripts, styles, and extraneous content.
- **🧹 Data Cleaning:** Limits text to a manageable length (up to 5000 characters) and strips unnecessary elements.
- **📝 Summarization:** Uses an NLP prompt to generate bullet-point summaries with options for short, medium, or long outputs.
- **🔍 Language Detection:** Automatically detects text language to deliver summaries in the appropriate language.
- **➡️ API Integration:** Connects with the OpenRouter API to leverage powerful language models for summarization.

---

## 🛠️ Prerequisites
- **Python 3.7+**
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `langdetect`
  - `json` (standard library)

You can install the required packages using:

pip install requests beautifulsoup4 langdetect


## 🚀 Installation
1. **Clone the Repository:**
    ```bash
    gh repo clone SriHarsha339/WebSummarizer
    cd WebSummarizer
    ```
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
   *(If you don’t have a `requirements.txt`, you can manually install the above prerequisites.)*

3. **Configure API Key:**
   - Open the Python file and replace the placeholder `API_KEY` with your actual OpenRouter API key.
   - **Note:** For security reasons, do not expose your API key in production.



## 🎬 Usage
Run the script directly:
```bash
python websum.py
```
Follow the interactive prompts:
- **Enter Website URL:** Provide a valid URL (must start with `http://` or `https://`).
- **Choose Summary Length:** Select from `short`, `medium`, or `long`.

After a brief processing period, the tool will display a neat bullet-point summary based on the input web content.

---

## 💻 Code Overview
Below is a quick summary of what the code does:

- **`scrape_website(url)`**  
  - Uses `requests` to fetch webpage content.
  - Utilizes `BeautifulSoup` to parse HTML and extract text.
  - Limits output to 5000 characters for efficiency.

- **`summarize_text(text, length)`**  
  - Detects the language of the text with `langdetect`.
  - Sets up a prompt with the desired bullet-point count for summarization.
  - Calls the OpenRouter API using `requests` to get the summary.
  
- **`main()`**  
  - Handles user input for URL and summary length.
  - Manages the flow: fetch, summarize, and display the summary.

Check out the full [code](./websum.py) in the repository for complete details!

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact
For questions or suggestions, feel free to reach out:

**Gowtham Sri Harsha**  
Email: [harshakota339@gmail.com](mailto:harshakota339@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/gowthamsriharsha)  
[GitHub](https://github.com/SriHarsha339)

---

Happy summarizing! 😄
```
