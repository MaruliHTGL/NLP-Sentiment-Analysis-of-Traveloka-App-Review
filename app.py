import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Review Analysis']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>
                Unlock Customer Insights with Traveloka Sentiment Analyzer!
            </h1>
            
            <br>

            <p style='text-align: justify;'>
                Understanding customer feedback is the key to improving any product or service. With thousands of reviews left by users every day, manually analyzing them can be overwhelming. That’s where Traveloka Sentiment Analyzer comes in to extracting meaningful insights from Traveloka app reviews efficiently.
            </p>

            <br>

            <h3 style='text-align: justify;'>Why Use This Tool?</h3>
            <ul>
                <li><strong>Identify Trends and Patterns:</strong> Discover what users love about Traveloka and what areas need improvement.</li>
                <li><strong>Enhance User Experience:</strong> Use data-driven insights to optimize the app, improve services, and increase customer retention.</li>
                <li><strong>Make Informed Business Decisions:</strong> Base your strategies on actual user feedback rather than guesswork.  </li>
            </ul>

            <br>

            <p style='text-align: justify;'>
                Don’t let valuable customer feedback go unnoticed. With Traveloka Sentiment Analyzer, you can turn raw reviews into actionable insights that drive growth and innovation.
            </p>
            
            <br>

            <p style='text-align: justify;'>
                <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors
            </p>

            <br>

            <p style='text-align: center;'>
                <strong>Unlock the power of customer insights and stay ahead in the travel industry.</strong>
            </p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Review Analysis":
        run_ml_app()

if __name__ == '__main__':
    main()
