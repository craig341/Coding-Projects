import os
import requests

# Base directory where the files will be stored
BASE_DIR = "/Users/craig/main/smart stuff/Past Papers/Physics"

# A list of years to consider (you can expand this as needed)
years = [2023, 2022, 2021, 2020, 2019, 2018]  # Add more years if required

# A list of months (full name, lowercase)
months = [
    "may", "june", "july", "october", "november"
]

# A list of possible base subject codes for Physics papers
base_codes = ["8463"]  # Update these base codes based on actual paper codes

# A list of possible paper numbers (P1, P2, etc.)
papers = ["1", "2"]

# A list of possible paper types (QP, MS, INS)
paper_types = ["QP", "MS"]

# A list of possible paper suffixes (H, F, etc.)
suffixes = ["H"]  # Add other possible suffixes here if necessary


# Function to download and save files
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ Downloaded: {save_path}")
        else:
            print(f"❌ Failed to download: {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"🚨 Error downloading {url}: {e}")


# Function to generate and download Physics papers
def brute_force_download():
    for year in years:
        for month in months:
            for base_code in base_codes:
                for paper in papers:
                    for paper_type in paper_types:
                        for suffix in suffixes:
                            # Construct the full paper code by combining base_code, suffix, and paper number
                            code = f"{base_code}{paper}{suffix}"  # For example, "84632H" or "84631H"
                            date_code = f"{month[:3].upper()}{str(year)[-2:]}"  # e.g., JUN22

                            # URL without -CR
                            url = f"https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/{year}/{month}/AQA-{code}-{paper_type}-{date_code}.PDF"

                            # URL with -CR
                            url_cr = f"https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/{year}/{month}/AQA-{code}-{paper_type}-{date_code}-CR.PDF"

                            # Create the folder path for saving the file, based on Paper number
                            paper_folder = f"Paper {paper}"
                            folder_path = os.path.join(BASE_DIR, paper_folder, date_code)
                            os.makedirs(folder_path, exist_ok=True)

                            # Construct the save path
                            new_filename = f"Phys-{paper}-{date_code}-{paper_type}.pdf"
                            save_path = os.path.join(folder_path, new_filename)

                            # Check if the file exists before downloading
                            if not os.path.exists(save_path):
                                # Try downloading the URL without the -CR suffix
                                download_file(url, save_path)
                                # If that fails, try with -CR at the end
                                if not os.path.exists(save_path):
                                    download_file(url_cr, save_path)
                            else:
                                print(f"🛑 File already exists: {save_path}")


# Function to remove empty folders
def remove_empty_folders(base_folder):
    for dirpath, dirnames, filenames in os.walk(base_folder, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            if not os.listdir(dir_to_check):  # If the directory is empty
                print(f"🗑️ Removing empty folder: {dir_to_check}")
                os.rmdir(dir_to_check)  # Remove empty directory


if __name__ == "__main__":
    brute_force_download()
    # Remove empty folders within Paper 1 and Paper 2 directories
    remove_empty_folders(os.path.join(BASE_DIR, "Paper 1"))
    remove_empty_folders(os.path.join(BASE_DIR, "Paper 2"))
    print("Download & sorting complete!")