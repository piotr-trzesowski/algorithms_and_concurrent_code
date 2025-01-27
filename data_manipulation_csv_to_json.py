import pandas as pd
import json
from pathlib import Path


def parse_csv_to_json(input_csv, output_json):
    df = pd.read_csv(input_csv)

    grouped = df.groupby(['Database', 'Table', 'Column'])

    # Aggregate subcategories as a list of dictionaries
    aggregated_data = grouped.apply(
        lambda group: [{'category': row['Category'], 'subcategory': row['Subcategory']} for _, row in group.iterrows()]
    ).reset_index(name='subcategory_aggregated')

    # Convert the DataFrame to a list of dictionaries
    json_data = aggregated_data.to_dict(orient='records')

    # Write the JSON data to a file
    with open(output_json, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"JSON file has been created: {output_json}")


# Usage
input_csv = Path(__file__).parent / 'inputs' / 'database_structure.csv'  # Input CSV file path
output_json = 'parsed_output.json'    # Output JSON file path
parse_csv_to_json(input_csv, output_json)