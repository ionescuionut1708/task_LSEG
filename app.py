from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import random
import os
from io import StringIO

app = Flask(__name__)

def read_csv_data(file_path):
    return pd.read_csv(file_path, header=None, names=['Stock', 'Date', 'Price'])

@app.route('/get_random_data', methods=['POST'])
def get_random_data(file_path=None):
    try:
        if file_path is None:
            file_path = request.json['file_path']
        df = read_csv_data(file_path)
        
        if len(df) < 30:
            return jsonify({"error": "Insufficient data points"}), 400
        
        start_index = random.randint(0, len(df) - 30)
        selected_data = df.iloc[start_index:start_index+30]
        
        return jsonify(selected_data.to_dict(orient='records'))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/identify_outliers', methods=['POST'])
def identify_outliers(data=None):
    try:
        if data is None:
            data = request.json['data']
        df = pd.DataFrame(data)
        
        mean = df['Price'].mean()
        std = df['Price'].std()
        threshold = 2 * std
        
        outliers = df[abs(df['Price'] - mean) > threshold]
        
        result = []
        for _, row in outliers.iterrows():
            deviation = (row['Price'] - mean) / mean * 100
            result.append({
                'Stock': row['Stock'],
                'Timestamp': row['Date'],
                'Actual Price': row['Price'],
                'Mean of 30 data points': mean,
                'Deviation (%)': deviation
            })
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_all_files(input_dir, output_dir, num_files=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    if num_files:
        csv_files = csv_files[:num_files]
    
    for file_name in csv_files:
        file_path = os.path.join(input_dir, file_name)
        
        # fac rost de 30 de puncte de date
        with app.test_request_context():
            response = get_random_data(file_path)
            data = response.json if response.status_code == 200 else []
        
        if not data:
            print(f"Error processing file {file_name}: {response.json['error'] if 'error' in response.json else 'Unknown error'}")
            continue
        
        # identific outliers
        with app.test_request_context():
            response = identify_outliers(data)
            outliers = response.json if response.status_code == 200 else []
        
        if not outliers:
            print(f"No outliers found in file {file_name}")
            continue
        
        # salvez rezultatele intr-un CSV
        outliers_df = pd.DataFrame(outliers)
        outliers_df.to_csv(os.path.join(output_dir, f"outliers_{file_name}"), index=False)
        print(f"Processed {file_name} and saved outliers")

if __name__ == '__main__':
    input_directory = '/mnt/data/'
    output_directory = './output/'
    num_files_to_process = 2  # setez la none pentru ca vreau sa procesez toate fisierele
    
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist.")
    else:
        # procesarea fisierelor CSV
        process_all_files(input_directory, output_directory, num_files_to_process)
    

    app.run(debug=True)