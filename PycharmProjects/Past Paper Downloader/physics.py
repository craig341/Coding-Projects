import os
import requests

new_years = []
new_months = []

while True:
    

BASE_DIR = "/Users/craig/main/smart stuff/Past Papers/Physics"

years = [2023, 2022, 2021, 2020, 2019, 2018]

months = ["may", "june", "july", "october", "november"]

base_codes = ["8463"]

paper_nums = ["1", "2"]

paper_types = ["QP", "MS"]

try_cr = ["", "-CR"]


# Function to download and save files
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ Downloaded: {save_path}")
            return "success"
        else:
            print(f"❌ Tis failed: {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"🚨 Error downloading {url}: {e}")


def start_download():
    for year in years:
        for month in months:
            for num in paper_nums:
                for paper_type in paper_types:
                    for cr in try_cr:
                        date_code = f"{month[:3].upper()}{str(year)[-2:]}"  # e.g., JUN22

                        url = f"https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/{year}/{month}/AQA-8463{num}H-{paper_type}-{date_code}{cr}.PDF"

                        paper_folder = f"Paper {num}"
                        folder_path = os.path.join(BASE_DIR, paper_folder, date_code)
                        os.makedirs(folder_path, exist_ok=True)

                        new_filename = f"Phys-P{num}-{date_code}-{paper_type}.pdf"
                        save_path = os.path.join(folder_path, new_filename)

                        if not os.path.exists(save_path):
                            if download_file(url, save_path) != "success":
                                try:
                                    os.rmdir(folder_path)
                                    print(f"🗑 The folder {folder_path} has been deleted.")
                                except Exception as e:
                                    print(f"Error: {e}")
                        else:
                            print(f"🛑 Tis exists: {save_path}")

if __name__ == "__main__":
    start_download()
    print("Download & sorting complete!")
