try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)
    _analyzer = SentimentIntensityAnalyzer()
    def analyze(text):
        scores = _analyzer.polarity_scores(text)
        comp = scores['compound']
        if comp >= 0.05:
            label = 'positive'
        elif comp <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        return {'label': label, 'scores': scores}
except Exception:
    # Simple fallback if NLTK or downloads fail
    def analyze(text):
        t = text.lower()
        pos_words = ['good','great','excellent','love','best','nice','amazing','perfect']
        neg_words = ['bad','worst','terrible','disappointed','poor','awful','hate','problem']
        p = sum(t.count(w) for w in pos_words)
        n = sum(t.count(w) for w in neg_words)
        if p > n:
            label = 'positive'
        elif n > p:
            label = 'negative'
        else:
            label = 'neutral'
        return {'label': label, 'scores': {'pos':p,'neg':n}}
