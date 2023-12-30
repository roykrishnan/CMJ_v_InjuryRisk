import pandas as pd
import matplotlib.pyplot as plt
import os

#Prompt data retrieval. 
def get_valid_player_id_input():
    while True:
        player_input = input("Enter Player ID Number for Return from Injury tracking metrics: ")
        
        # Check if the input starts with 'Player'
        if player_input.startswith('Player'):
            player_id = player_input.replace('Player', '').strip()
        else:
            player_id = player_input
        
        # Check if the file exists
        filename = f'player_{player_id}.csv'
        if os.path.exists(filename):
            return filename
        else:
            print("File does not exist, please provide a valid input.")

#After user passes tests for them to find their Player. Load our correct CSV information.
loadfile = get_valid_player_id_input()
data = pd.read_csv(loadfile)

# Convert TestDate column to datetime
data['TestDate'] = pd.to_datetime(data['TestDate'])

# Sort data by TestDate in ascending order (oldest to newest)
data = data.sort_values(by='TestDate')

# Select columns of interest for each set of metrics
metrics_set1 = ['TestDate', 'PeakPropulsiveForceNewtons', 'PeakLandingForceNewtons']
metrics_set2 = ['TestDate', 'TimeToStabilizationMilliseconds', 'Landing Impulse']
metrics_set3 = ['TestDate',  'LRPropulsiveImpulseIndexPct']

# Plotting the first set of metrics
plt.figure(figsize=(10, 6))
plt.plot(data['TestDate'], data['PeakPropulsiveForceNewtons'], marker='o', label='Peak Propulsive Force')
plt.title('Peak Propulsion Force Over Time')
plt.xlabel('Test Date')
plt.ylabel('Newtons')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the second set of metrics - TimeToStabilizationMilliseconds
plt.figure(figsize=(10, 6))
plt.plot(data['TestDate'], data['PeakLandingForceNewtons'], marker='^', label='Peak Landing Force')
plt.plot(data['TestDate'], data['TimeToStabilizationMilliseconds'], marker='o', label='Time to Stabilization')
plt.title('Force & Stabilization Period Over Time')
plt.xlabel('Test Date')
plt.ylabel('Newtons')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting the third set of metrics
plt.figure(figsize=(10, 6))
plt.plot(data['TestDate'], data['LRPropulsiveImpulseIndexPct'], marker='o', label='Asymmetry as Percent in Take Off')
plt.title('Asymmetry in Take Off Over Time')
plt.xlabel('Test Date')
plt.ylabel('Side Favored (Zero being Neutral)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
