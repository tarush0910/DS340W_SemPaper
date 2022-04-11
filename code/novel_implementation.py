from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import pandas as pd
import numpy as np

# import data
data = pd.read_csv("../data/us_2020_election_data.csv")

# list of selected features from feature extraction
selected_features = ['N1_retweet_hastag_word_7', 'N1_retweet_hastag_word_5', 'N1_retweet_hastag_word_9',
                     'N1_retweet_hastag_word_1', 'N1_retweet_hastag_word_4', 'N1_retweet_hastag_word_8',
                     'N1_retweet_hastag_word_6', 'N1_retweet_hastag_word_0', 'N1_retweet_hastag_word_3',
                     'N1_retweet_hastag_word_2', 'N1_retweet_mentioned_word_1', 'N1_retweet_mentioned_word_5',
                     'N1_retweet_mentioned_word_7', 'N1_retweet_hastag_tfidf', 'N2_retweet_hastag_word_7',
                     'N1_retweet_mentioned_word_4', 'N1_retweet_mentioned_word_3', 'N3_retweet_hastag_word_7',
                     'N2_retweet_hastag_word_5', 'N2_retweet_mentioned_word_1', 'N2_retweet_mentioned_word_5',
                     'N2_retweet_hastag_word_4', 'N2_retweet_hastag_word_1', 'N2_retweet_mentioned_word_7',
                     'N3_retweet_hastag_word_5', 'N1_retweet_mentioned_word_6', 'N2_retweet_mentioned_word_3',
                     'daily_retweet_avg', 'N2_retweet_hastag_word_8', 'N1_retweet_mentioned_word_0',
                     'N2_retweet_mentioned_word_4', 'N2_retweet_hastag_word_6', 'N2_retweet_hastag_word_0',
                     'N2_retweet_hastag_word_3', 'N1_retweet_mentioned_word_8', 'N3_retweet_mentioned_word_5',
                     'N3_retweet_hastag_word_1', 'N3_retweet_hastag_word_4', 'N2_retweet_hastag_word_9',
                     'N2_retweet_hastag_word_2', 'N3_retweet_mentioned_word_7', 'N3_retweet_hastag_word_3',
                     'N3_retweet_hastag_word_8', 'N1_retweet_mentioned_word_2', 'N1_retweet_mentioned_word_9',
                     'N3_retweet_hastag_word_6', 'N3_retweet_mentioned_word_1', 'N3_retweet_mentioned_word_3',
                     'N3_retweet_hastag_word_0', 'N3_retweet_mentioned_word_4', 'N3_retweet_hastag_word_9',
                     'N3_retweet_hastag_word_2', 'N2_retweet_hastag_tfidf', 'daily_rt_0', 'N3_retweet_mentioned_tfidf',
                     'N2_retweet_mentioned_word_6', 'N3_retweet_mentioned_word_6', 'daily_rt_6',
                     'retweet_number_of_mentions_avg', 'N1_retweet_mentioned_tfidf', 'N2_retweet_mentioned_word_8',
                     'N3_retweet_hastag_tfidf', 'retweet_number_of_urls_std', 'retweet_number_of_urls_avg',
                     'retweet_number_of_hashtags_avg', 'N3_retweet_mentioned_word_8', 'daily_rt_2', 'daily_rt_tw_0',
                     'daily_rt_tw_6', 'N2_retweet_mentioned_word_9', 'N2_retweet_mentioned_word_2', 'entities_count',
                     'N3_retweet_mentioned_word_2', 'N3_retweet_mentioned_word_0', 'N2_retweet_mentioned_tfidf',
                     'retweet_number_of_mentions_std', 'N2_retweet_mentioned_word_0', 'daily_rt_tw_2',
                     'N3_retweet_mentioned_word_9', 'daily_rt_5', 'daily_rt_3', 'daily_rt_1', 'daily_rt_4',
                     'N1_retweet_word_0', 'daily_rt_tw_4', 'N1_retweet_word_3', 'daily_rt_tw_3', 'daily_rt_tw_1',
                     'daily_rt_tw_5', 'N1_retweet_word_5', 'N1_retweet_word_4', 'N1_retweet_word_7',
                     'N1_retweet_word_6', 'N1_retweet_word_8', 'N1_tweet_hastag_word_3', 'N1_tweet_hastag_word_8',
                     'verified', 'N1_tweet_hastag_word_9', 'N1_tweet_hastag_word_6', 'N1_tweet_hastag_word_7',
                     'geolocation', 'N1_retweet_word_9', 'N1_retweet_word_2', 'retweet_number_of_hashtags_std',
                     'N1_tweet_hastag_word_0', 'friends_by_age', 'N1_tweet_hastag_word_5', 'N1_tweet_hastag_word_1',
                     'N2_tweet_hastag_word_3', 'N1_tweet_hastag_word_2', 'N1_tweet_hastag_word_4',
                     'N2_tweet_hastag_word_7', 'tweet_number_of_urls_std', 'N2_retweet_word_3', 'default_profile',
                     'N2_tweet_hastag_word_8', 'N2_tweet_hastag_word_6', 'N2_retweet_word_4', 'N2_tweet_hastag_word_5',
                     'N3_retweet_word_0', 'N3_retweet_word_7', 'N2_retweet_word_0', 'N2_retweet_word_5',
                     'N3_tweet_hastag_word_3', 'N3_retweet_word_5', 'N3_retweet_word_2', 'N2_retweet_word_8',
                     'tweet_number_of_urls_avg', 'N3_retweet_word_1', 'N2_retweet_word_6', 'N3_retweet_word_6',
                     'N3_retweet_word_3', 'N3_retweet_word_9', 'retweet_time_avg', 'N2_retweet_word_9',
                     'N3_retweet_word_4', 'retweet_time_max', 'N2_retweet_word_2', 'N2_retweet_word_7',
                     'N3_retweet_word_8', 'rt_self', 'N2_tweet_hastag_word_1', 'N2_retweet_word_1',
                     'N2_tweet_hastag_word_0', 'retweet_time_std', 'hour_rt_tw_20', 'N3_tweet_hastag_word_7',
                     'N3_tweet_hastag_word_8', 'N2_tweet_hastag_word_4', 'hour_rt_20', 'N3_tweet_hastag_word_6',
                     'hour_rt_tw_0', 'N2_tweet_hastag_word_2', 'hour_rt_tw_1', 'hour_rt_2', 'hour_rt_tw_23',
                     'hour_rt_tw_2', 'N2_tweet_hastag_word_9', 'hour_rt_tw_22', 'N3_tweet_hastag_word_5',
                     'hour_rt_tw_21', 'hour_rt_0', 'hour_rt_1', 'hour_rt_tw_19', 'hour_rt_tw_14',
                     'N3_tweet_hastag_word_0', 'hour_rt_tw_18', 'hour_rt_22', 'hour_rt_23', 'hour_rt_15', 'hour_rt_18',
                     'hour_rt_tw_15', 'hour_rt_19', 'tweet_by_age', 'friends_count', 'hour_rt_21', 'hour_rt_14',
                     'hour_rt_tw_17', 'followers_by_age', 'N3_tweet_hastag_word_1', 'listed_count', 'hour_rt_tw_16',
                     'hour_rt_tw_13', 'hour_rt_3', 'hour_rt_13', 'hour_rt_tw_3', 'N3_tweet_hastag_word_4',
                     'N3_tweet_hastag_word_9', 'hour_rt_17', 'hour_rt_16', 'N3_tweet_hastag_word_2', 'foll_friends',
                     'N1_tweet_hastag_tfidf', 'location', 'name_and_screen_name_similarity', 'hour_rt_tw_12',
                     'w_out_degree', 'N3_tweet_hastag_tfidf', 'hour_rt_12', 'daily_tweet_avg',
                     'tweet_number_of_hashtags_avg', 'listed_by_age', 'tweet_number_of_hashtags_std', 'hour_rt_tw_4',
                     'hour_rt_4', 'followers_count', 'favourites_by_age', 'hour_rt_tw_11', 'w_degree',
                     'retweet_time_min', 'N3_tweet_word_3', 'hour_rt_11', 'N1_tweet_word_3', 'N2_tweet_word_3',
                     'out_degree', 'N1_tweet_word_5', 'description_length', 'N1_tweet_mentioned_word_5',
                     'N3_tweet_word_9', 'N1_tweet_mentioned_word_1', 'N1_tweet_word_6', 'N3_tweet_word_5',
                     'N3_tweet_word_0', 'tweet_number_of_mentions_avg', 'N1_tweet_mentioned_word_4',
                     'N1_tweet_mentioned_word_3', 'N1_tweet_mentioned_word_6', 'hour_rt_tw_5', 'N1_tweet_word_9','target']

# Extracting selected features for our new model
selected_data = data[selected_features]

X = np.array(selected_data.drop(columns= 'target'))
y = selected_data['target'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,200,200),
                    learning_rate='adaptive', max_iter=5000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
f1_accuracy = f1_score(y_true=y_test, y_pred=y_pred)
accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

print("The F1_score for a MultiLayer Perceptron is :",f1_accuracy)
print("The accuracy_score for a Multilayer Perceptron is:",accuracy)