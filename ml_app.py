import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from deep_translator import GoogleTranslator

sia = SentimentIntensityAnalyzer()

def sentiment_vader(text):
    compound_polarity = sia.polarity_scores(text)
    
    if compound_polarity['compound'] >= 0.05:
        return 'Positive'
    elif compound_polarity['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'>Input the Review</h2>", unsafe_allow_html=True)
    review = st.text_area('Enter the Traveloka Review:', 'Traveloka')

    with st.expander("Your Input"):
        result = {
            'Review': review,
        }

    # dataframe
    df = pd.DataFrame({'Review': [review]})

    # translate text
    df["english_text"] = df["Review"].apply(lambda x: GoogleTranslator(source='id', target='en').translate(x))

    st.markdown("<h2 style = 'text-align: center;'> The Review </h2>", unsafe_allow_html=True)

    st.write(review)

    # prediction section
    st.markdown("<h2 style = 'text-align: center;'> Analysis Result </h2>", unsafe_allow_html=True)

    df['Label'] = df['english_text'].apply(lambda text: sentiment_vader(text))

    if df.iloc[0,2] == 'Positive':
        st.success("Positive Review")
        st.write('Halo! Terima kasih banyak atas review positifnya. Jika Anda memiliki masukan tambahan, jangan ragu untuk menghubungi kami melalui layanan Pusat Pesan yang dapat diakses melalui beranda Traveloka App. Kami akan dengan senang hati membantu Anda. Nantikan update dan penawaran menarik lainnya di Traveloka!')
    elif df.iloc[0,2] == 'Negative':
        st.error("Negative Review")
        st.write('Hai, kami mohon maaf terkait ketidaknyamanan atas pengalaman Anda. Jangan khawatir, saat ini tim kami sedang berupaya mengatasinya. Kami akan menyelesaikannya dan mengabari Anda melalui pesan pada Traveloka App hingga masalah tersebut terselesaikan. Terima kasih atas kesabaran Anda.')
    else:
        st.warning('Neutral Review')
        st.write('Halo Kak, terima kasih banyak atas reviewnya, semoga tetap nyaman dan selalu setia menjadi pelanggan Traveloka. Ayo pantau terus Traveloka Lifestyle Super App karena kami selalu memberikan promo-promo menarik, jangan sampai ketinggalan.')

    st.markdown('''<p style='text-align: justify;'> <br> <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors.</p>''', unsafe_allow_html=True)
