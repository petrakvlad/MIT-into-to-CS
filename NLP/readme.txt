
# Description

### : Training a Text Classification Model

- `model.py`: This script is responsible for training a deep learning model for text classification. It follows the following steps:
  - Load data from CSV files (e.g., `reviews.csv` and `labels.csv`) using Pandas.
  - Merge the dataframes based on a common ID column.
  - Tokenize and pad the text data using the Keras `Tokenizer` and `pad_sequences`.
  - Encode sentiment labels using `LabelEncoder` from Scikit-Learn.
  - Split the data into training and validation sets using `train_test_split` from Scikit-Learn.
  - Define a sequential neural network model with an embedding layer, LSTM layer, and dense layer.
  - Compile the model with appropriate loss and optimizer.
  - Train the model on the training data for a specified number of epochs and batch size.

### : Inference and Prediction

- `inference.py`: This script is designed for making predictions on new text data using a pre-trained text classification model. It performs the following steps:
  - Parse command-line arguments for input and output file paths.
  - Load text data from the input CSV file using Pandas.
  - Tokenize and pad the text data in the same way as the training data.
  - Use a pre-trained model for inference to generate continuous output values.
  - Round the continuous predictions to binary sentiment labels (0 or 1).
  - Save the original texts and predicted labels to an output CSV file.

## Getting Started

1. Clone this repository to your local machine and specify path to the project folder as "folder"

2. Install the required dependencies listed in `requirements.txt` using pip:

3. Prepare your data:
- Place your input CSV files with text data (`reviews.csv`) and labels (`labels.csv`) in the same directory as the code.
- Ensure that the CSV files have a common id column for merging.

4. Call: python3 inference.py test_reviews.csv test_labels_pred.csv

- where test_reviews.csv are the reviews to classify and test_labels_pred.csv is an output file.
Training and inferencing process will start and results will be placed in the test_labels_pred.csv file

