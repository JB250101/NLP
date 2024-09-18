import pandas as pd
import re

# Function to clean and normalize text
def clean_text(text):
    # Remove unwanted characters (punctuation, extra spaces, etc.)
    text = re.sub(r'[^\w\s,。]', '', text)  # Remove extra punctuation
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    return text

# Function to process the dataset
def preprocess_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)
  
    # Display the first few rows of the original dataset
    print("Original Data:")
    print(df.head())

    # Keep only necessary columns (assuming columns are ['English', 'Mandarin'])
    if 'English' not in df or 'Mandarin' not in df:
        raise ValueError("Input CSV must contain 'English' and 'Mandarin' columns.")
    
    # Clean the 'English' and 'Mandarin' columns
    df['English'] = df['English'].apply(clean_text)
    df['Mandarin'] = df['Mandarin'].apply(clean_text)

    # Remove duplicates
    df.drop_duplicates(subset=['English', 'Mandarin'], inplace=True)

    # Optional: Add an annotation column (customize as needed)
    df['Annotation'] = df.apply(lambda row: annotate(row['English'], row['Mandarin']), axis=1)

    # Save the cleaned dataset to a new CSV file
    df.to_csv(output_file, index=False)
    
    # Display the final cleaned dataset
    print(f"Cleaned Data Saved to {output_file}")
    print(df.head())

# Annotation function example
def annotate(english_sentence, mandarin_sentence):
    # Custom annotation logic can be added here
    # For demonstration, we annotate all by default; modify as needed
    return "General"

# Main function
if __name__ == "__main__":
    INPUT_FILE = 'input_data.csv'  # Replace with your input file path
    OUTPUT_FILE = 'cleaned_data.csv'  # Replace with your desired output file path

    preprocess_data(INPUT_FILE, OUTPUT_FILE)
