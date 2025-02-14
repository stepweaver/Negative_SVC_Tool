import pandas as pd
import os

# Define input and output paths
input_path = r"G:\My Drive\Card Office Stuff\Negative Flex Script\Negative SVC_Full Data_data.csv"
output_dir = r"G:\My Drive\Card Office Stuff\Negative Flex Script"

# Read the CSV file
df = pd.read_csv(input_path)

# Create a CSV for PLANNUM = 2
df_plan2 = df[df['PLANNUM'] == 2]
if not df_plan2.empty:
    output_file_plan2 = os.path.join(output_dir, 'plannum_2.csv')
    
    with open(output_file_plan2, 'w', encoding='utf-8') as f:
        f.write('/DELIMITER=","\n')
        f.write('/FIELDS=UPDATE_MODE,PRIMARYKEYVALUE,SVC1PLANNUM\n')
        for _, row in df_plan2.iterrows():
            f.write(f'D,{row["PRIMARYKEY"]},2\n')

# Create a CSV for PLANNUM = 200
df_plan200 = df[df['PLANNUM'] == 200]
if not df_plan200.empty:
    output_file_plan200 = os.path.join(output_dir, 'plannum_200.csv')
    
    with open(output_file_plan200, 'w', encoding='utf-8') as f:
        f.write('/DELIMITER=","\n')
        f.write('/FIELDS=UPDATE_MODE,PRIMARYKEYVALUE,SVC1PLANNUM\n')
        for _, row in df_plan200.iterrows():
            f.write(f'D,{row["PRIMARYKEY"]},200\n')

# Create special CSV for PLANNUM = 2 with SVC1PLANNUM = 4
if not df_plan2.empty:
    output_file_plan2_special = os.path.join(output_dir, 'plannum_2_special.csv')
    
    with open(output_file_plan2_special, 'w', encoding='utf-8') as f:
        f.write('/DELIMITER=","\n')
        f.write('/FIELDS=UPDATE_MODE,PRIMARYKEYVALUE,SVC1PLANNUM,SVC1AMOUNT\n')
        for _, row in df_plan2.iterrows():
            # Convert the negative decimal to the required format
            amount_str = str(row['P.AVAILBALANCE*0.01'])  # e.g. "-66.03"
            formatted_amount = '--' + amount_str.replace('-', '').replace('.', '')  # Remove minus and decimal
            f.write(f'C,{row["PRIMARYKEY"]},4,{formatted_amount}\n')

print("CSV files have been created successfully!") 