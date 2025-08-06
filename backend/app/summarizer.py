from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # Latent Semantic Analysis summarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT_QUICK = 3
SENTENCES_COUNT_INDEPTH = 7

def summarize_text(text: str, summary_type: str = "quick") -> str:
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    if summary_type == "in-depth":
        sentences_count = SENTENCES_COUNT_INDEPTH
        summarizer = TextRankSummarizer(stemmer)
    else:
        # Default to quick summary
        sentences_count = SENTENCES_COUNT_QUICK
        summarizer = LuhnSummarizer(stemmer)

    summarizer.stop_words = get_stop_words(LANGUAGE)
    summary = summarizer(parser.document, sentences_count)

    # Return bullet points
    bullet_points = "\n".join([f"• {str(sentence)}" for sentence in summary])
    return bullet_points or "Summary could not be generated."
