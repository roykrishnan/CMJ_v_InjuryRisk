import pandas as pd

# Load our raw data file
file_path = 'force_plate_sample_anonymized.csv'
df = pd.read_csv(file_path)

# Drop zero value columns. Zero use to us without data. Just makes the data set neater. 
columns_to_drop = ['PeakRelativeBrakingPowerWattsPerKilogram','RelativePropulsiveImpulseNewtonSecondsPerKilogram']
df_cleaned = df.drop(columns=columns_to_drop)

# Sort the rows by PlayerTestSessionId, TestDate, and TestSessionSeq. 
# Our data is focused on catching potential injuries by referencing abnormal deltas. This creates our potential time series. 
df_cleaned = df_cleaned.sort_values(by=['TestDate','PlayerIdentifier', 'TestSessionSeq'], ascending=[True, False, True])

#round to 3 sig figs to keep data values standard across columns.
df_cleaned = df_cleaned.round(3)

# Count the number of unique values in the 'PlayerIdentifier' column. Lets us know how many players we're dealing with. 
num_unique_players = df_cleaned['PlayerIdentifier'].nunique()
print("Number of unique players:", num_unique_players)

# Save the cleaned and sorted data frame back to a CSV file
cleaned_file_path = 'force_plate_sample_cleaned.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print("Clean and sort completed and saved to file: 'force_plate_sample_cleaned.csv'.")

