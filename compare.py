import pandas as pd
import os
from modules.sentiment import analyze

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.csv')

def compare_product(query):
    # Load data
    df = pd.read_csv(DATA_PATH)
    # basic matching (case-insensitive substring)
    df_matched = df[df['product_name'].str.lower().str.contains(query.lower(), na=False)]
    if df_matched.empty:
        return {'product': query, 'error': 'No matching products found.'}

    # price comparison
    prices = []
    for _, row in df_matched.iterrows():
        try:
            price = float(row['price'])
        except:
            price = None
        prices.append({'platform': row['platform'], 'price': price})

    # lowest price
    valid_prices = [p for p in prices if p['price'] is not None]
    lowest = min(valid_prices, key=lambda x: x['price']) if valid_prices else {'platform': None, 'price': None}

    # sentiment on reviews - aggregate by counting labels
    sentiments = {'positive':0, 'neutral':0, 'negative':0}
    reviews = []
    for _, row in df_matched.iterrows():
        review = str(row.get('review', '')).strip()
        if review:
            res = analyze(review)
            label = res.get('label', 'neutral')
            sentiments[label] = sentiments.get(label,0) + 1
            reviews.append({'platform': row['platform'], 'review': review, 'sentiment': label})

    total_reviews = sum(sentiments.values())
    overall = 'No reviews'
    if total_reviews:
        # determine majority
        overall = max(sentiments, key=sentiments.get)

    # pick top 5 reviews for display
    top_reviews = reviews[:5]

    return {
        'product': query,
        'prices': prices,
        'lowest': lowest,
        'sentiment': {'positive': sentiments['positive'], 'neutral': sentiments['neutral'], 'negative': sentiments['negative'], 'overall': overall},
        'top_reviews': top_reviews
    }
