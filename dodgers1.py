import pandas as pd
import matplotlib.pyplot as plt
import sys

"""
Los Angeles Dodgers Senior Applied Research Scientist Technical Assessment
Code created and submitted by Roy Krishnan (August 2023) 
"""
# Create a visuals framework using python tools for mocap by isolating key points in the kinetic chain. 
def plot_line_graph(data, column_name, frame, data_frame):
    plt.plot(frame, data)
    plt.xlabel('Frame')
    plt.ylabel(column_name)
    plt.title(column_name + ' Over Frames')
    plt.grid(True)

    # Parsing ball release in our file format. Assuming output file is a static mocap export. 
    ball_release = data_frame.iloc[:, -2][1:].astype(float) 
    if (ball_release == 0).any():
        zero_frame_index = ball_release[ball_release == 0].index[0]
        plt.axvline(x=zero_frame_index, color='red', linestyle='--', label='Ball Release')

    # Creating front soot strike variables and visuals. 
    front_foot_strike = data_frame.iloc[:, -4][1:].astype(float)  
    if (front_foot_strike == 0).any():
        zero_frame_index = front_foot_strike[front_foot_strike == 0].index[0] + 1
        plt.axvline(x=zero_frame_index, color='blue', linestyle='--', label='Front Foot Strike')
    
    # Creating Throwing SHoulder Max External Rotation variable and visuals 
    peak_index = data_frame['right_shoulder_external_rotation'][1:].astype(float).idxmax()
    plt.axvline(x=peak_index, color='black', linestyle='--', label='Throwing Shoulder MER')
    
    # Showing Legend
    plt.legend()  
    plt.show()

""" 
Visuals are now created for use. Mainframe needs to created. Envisioning use for Coaches that have rudimentary biomechanics training
(eg. Driveline Certification, Biomechanics 101), therefore creating the basics of an application that can be utilized in order to 
quickly sift through csv data with user prompting and render an actionable graph. 
 """

def main():
    #Loading Data
    file_path = '/Users/rohitkrishnan/Desktop/TechnicalAssessmentData/Pitching/PitcherY_Pitch1.csv'
    data_frame = pd.read_csv(file_path)

    while True:
        #User
        show_all_graphs = input("Do you want to see all graphs relating to the pitch? (yes/no): ").lower().strip()

        if show_all_graphs == "yes":
            # Go through quant. data we actually want to analyze. 
            # Starting from frames only to check if data is parsing correctly. If it is, should be 1:1 correlation. 
            columns_to_analyze = data_frame.columns[4:]
            for column in columns_to_analyze:
                column_name = column
                time_series_data = pd.to_numeric(data_frame[column][1:], errors='coerce')
                frame_data = pd.to_numeric(data_frame['frame'][1:], errors='coerce')
                plot_line_graph(time_series_data, column_name, frame_data, data_frame)
            break
        elif show_all_graphs == "no":
            # Search by column name (yes or no)
            search_specific_column = input("Search by specific column name? (yes/no): ").lower().strip()
            if search_specific_column == "yes":
                #Search by column name (which column)
                column_name = input("Enter a column name: ").strip()
                if column_name in data_frame.columns:
                    time_series_data = pd.to_numeric(data_frame[column_name][1:], errors='coerce')
                    frame_data = pd.to_numeric(data_frame['frame'][1:], errors='coerce')
                    plot_line_graph(time_series_data, column_name, frame_data, data_frame)
                    break
                else:
                    print("Invalid column name.")
            elif search_specific_column == "no":
                print("No graphs will be displayed.")
                while True:
                    restart_option = input("Do you want to restart the program, go back to the last step, or end the program? (restart/last/end): ").lower().strip()
                    #Edge case if user screws up (restart program)
                    if restart_option == "restart":
                        break  
                    elif restart_option == "last":
                        # Loop back to ask for column name
                        search_specific_column = "yes"
                        break
                    elif restart_option == "end":
                        print('Program ended')
                        sys.exit(0)
                    else:
                        print("Invalid choice. Please select either 'restart' or 'last'.")
            else:
                print("Invalid choice. Please select either 'yes' or 'no'.")

if __name__ == "__main__":
    main()
