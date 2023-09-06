from model import *
import csv
import argparse



def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Perform inference on input data and save predictions to a CSV file.')
    parser.add_argument('input_file', help='Path to the input CSV file containing text data')
    parser.add_argument('output_file', help='Path to the output CSV file to save predictions')
    args = parser.parse_args()

    # Load input data from the CSV file
    input_file_path = args.input_file
    inf_data = pd.read_csv(input_file_path)

    # Tokenize and pad the text
    max_sequence_length = 100
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(inf_data['text'])
    inf_data_token = tokenizer.texts_to_sequences(inf_data['text'])
    inf_data_token = pad_sequences(X, maxlen=max_sequence_length)

    # Perform inference
    predictions = model.predict(inf_data_token)

    # Round predictions to the nearest integer
    predicted_labels = label_encoder.inverse_transform(predictions.round().astype(int))

    # Prepare the original texts
    original_texts = tokenizer.sequences_to_texts(inf_data_token)

    # Specify the path to the output CSV file
    output_file_path = args.output_file

    # Save predictions to the output CSV file
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write a header row
        writer.writerow(['Text', 'Label'])
        
        # Iterate through the data and write it to the CSV file
        for i in range(len(predicted_labels)):
            writer.writerow([original_texts[i], predicted_labels[i]])

if __name__ == "__main__":
    main()
