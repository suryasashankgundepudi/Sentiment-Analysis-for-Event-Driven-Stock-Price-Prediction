# Sentiment Analysis for Event Driven Stock Price Prediction
## Overview
In this project, our goal was to build a language/sentiment model capable of accurately predicting the sentiment of financial news headlines and providing insights into the market's direction. We achieved impressive results with a model that attained a loss of 0.11, an accuracy of 0.96, and an F1-score of 0.94, outperforming our baseline models.

## Data Collection
The project's critical step involved obtaining relevant training and testing data. We utilized the TRCV2 and Financial Phrasebank datasets, pre-annotated and labeled by experts, to create a robust and accurate model.

## Model Development
We experimented with two baseline models, LSTM with GLoVe and LSTM with ELMo, which are recurrent neural networks using different word embeddings. Additionally, we fine-tuned the BERT model with the TRCV2 and Financial Phrasebank data, training it over six epochs with a batch size of 32 and gradual_unfreeze parameter for iterative learning.

## Real-World Backtesting
An exciting aspect of our project was conducting real-world backtesting using weekly price changes for AAPL stock, corresponding headlines, and our model's predicted sentiment. Our sentiment analysis model demonstrated a positive edge in the market, evident from the distribution of price changes across different sentiments.

## Future Expansions
Looking ahead, there is vast potential for expanding our work. Integrating ESG factors to evaluate a company's sustainability or analyzing freely available 10-k reports for long-term investment potential are some avenues for future exploration. We are proud of our achievements in this project and eagerly anticipate how our work can contribute to advancing financial analysis.

