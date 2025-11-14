# Product Price & Review Comparator — College Project

## What this project includes
- A Flask web app (`app.py`) that lets users search for a product and see:
  - Price comparison across platforms (from `data/products.csv`)
  - Sentiment analysis summary of reviews
- `modules/sentiment.py` — sentiment analyzer (uses NLTK VADER if available; fallback rule-based)
- `modules/compare.py` — product matching, price comparison, and review aggregation
- Simple UI in `templates/index.html` and `static/style.css`
- Sample dataset at `data/products.csv`

---

## Setup — Step-by-step (for beginners)
1. Install Python (3.8+ recommended).
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\\Scripts\\activate    # Windows
   ```
3. Install required packages:
   ```bash
   pip install flask pandas nltk
   ```
   - If you see errors related to `nltk` VADER, run:
   ```python
   python -m nltk.downloader vader_lexicon
   ```
4. Run the app:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

---

## How it works (high-level)
1. The app loads `data/products.csv` and searches product names by substring match.
2. `compare_product()` collects prices and reviews for matched rows.
3. `modules/sentiment.analyze()` returns a label (`positive`, `neutral`, `negative`) for each review.
4. The UI displays a lowest-price recommendation, a price table, sentiment counts, and a few reviews.

---

## We Can Make improvements
- Use real-time scraping or official APIs to fetch live prices.
- Add authentication, favorites, and price-tracking alerts.
- Improve product matching (fuzzy matching, model numbers).
- Add interactive charts (Chart.js) and pagination.
