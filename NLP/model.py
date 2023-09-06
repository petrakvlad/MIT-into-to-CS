import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import os

# Specify the folder path
folder = '/home/hell/Documents/GitHub/MIT-into-to-CS/NLP'

# Load the data
reviews_df = pd.read_csv(os.path.join(folder, 'reviews.csv'))
labels_df = pd.read_csv(os.path.join(folder, 'labels.csv'))

# Merge dataframes on the common ID column
merged_df = pd.merge(reviews_df, labels_df, on='id')

# Tokenize and pad the text
max_sequence_length = 100  # Adjust as needed
tokenizer = Tokenizer()
tokenizer.fit_on_texts(merged_df['text'])
X = tokenizer.texts_to_sequences(merged_df['text'])
X = pad_sequences(X, maxlen=max_sequence_length)

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(merged_df['sentiment'])

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


# Build the model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100, input_length=100))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
epochs = 10  # Adjust as needed
batch_size = 32  # Adjust as needed
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)

