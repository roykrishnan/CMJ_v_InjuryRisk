"""
Player & RFI sort:
Iterate through player data & sort them by Player ID & our Return from Injury (RFI) metrics.
Specific Metrics need to be specifically individualized to the player.
"""

import os
import pandas as pd
# Load the cleaned CSV file
cleaned_file_path = 'force_plate_sample_cleaned.csv'
df_cleaned = pd.read_csv(cleaned_file_path)

# Get the unique PlayerIdentifier values
unique_players = df_cleaned['PlayerIdentifier'].unique()

# Columns to keep
desired_columns = ['PlayerTestSessionId','TestDate','TestSessionSeq',"PeakPropulsiveForceNewtons", "PeakLandingForceNewtons",
                   "TimeToStabilizationMilliseconds",  'LRPropulsiveImpulseIndexPct']

# Create a folder named "PlayerID_RFI" if it doesn't exist
if not os.path.exists("PlayerID_RFI"):
    os.makedirs("PlayerID_RFI")

for player in unique_players:
    player_data = df_cleaned[df_cleaned['PlayerIdentifier'] == player]
    # Filter based on 'TestSessionSeq'
    player_data_filtered = player_data[player_data['TestSessionSeq'] <= 4][desired_columns].copy()
    
    player_file_path = os.path.join("PlayerID_RFI", f'player_{player}.csv')
    player_data_filtered.to_csv(player_file_path, index=False)
    print(f"Data for PlayerIdentifier {player} saved to {player_file_path}")
