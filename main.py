import subprocess
#Creating main file to run files in order automatically to clean, sort, identify, and create visuals of all of our data.
def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    scripts_to_run = [
        "data_clean_sort.py",
        "PlayerSort.py",
        "PlayerID_RFI/RFI_check.py"
    ]

    for script in scripts_to_run:
        run_script(script)
