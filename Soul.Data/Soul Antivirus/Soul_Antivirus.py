import os
import hashlib
import shutil

class SoulAntivirus:
    def __init__(self):
        # Known malware signature hashes and test string
        self.virus_signatures = {
            "e99a18c428cb38d5f260853678922e03": "TestVirus1",
            "098f6bcd4621d373cade4e832627b4f6": "TestVirus2",
        }
        self.eicar_string = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
        self.quarantine_folder = "quarantine"
        os.makedirs(self.quarantine_folder, exist_ok=True)

    def scan_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                file_hash = hashlib.md5(content).hexdigest()
                
                # Check for virus signatures based on file hash
                if file_hash in self.virus_signatures:
                    virus_name = self.virus_signatures[file_hash]
                    print(f"\nInfected file detected: {file_path} (Virus: {virus_name})")
                    self.handle_infection(file_path)
                    return True
                
                # Check for EICAR test string in file contents
                if self.eicar_string.encode() in content:
                    print(f"\nEICAR test file detected in {file_path}")
                    self.handle_infection(file_path)
                    return True
                
                print(f"No infection found in file: {file_path}")
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")

        return False

    def scan_directory(self, directory):
        print(f"Starting scan in directory: {directory}")
        infected_files = []
        
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if self.scan_file(file_path):
                    infected_files.append(file_path)
        
        if infected_files:
            print(f"\nScan complete. Found {len(infected_files)} infected file(s).")
        else:
            print("Scan complete. No infections found.")
        
        return infected_files

    def scan_drive(self, drive):
        print(f"Starting scan on drive: {drive}")
        return self.scan_directory(drive)

    def handle_infection(self, file_path):
        while True:
            action = input(f"Options for {file_path}:\n"
                           "1. Delete\n"
                           "2. Quarantine\n"
                           "3. Allow\n"
                           "Choose an action (1, 2, or 3): ")
            
            if action == "1":
                self.delete_file(file_path)
                break
            elif action == "2":
                self.quarantine_file(file_path)
                break
            elif action == "3":
                print(f"File allowed: {file_path}")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print(f"File deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting file: {e}")

    def quarantine_file(self, file_path):
        try:
            quarantine_path = os.path.join(self.quarantine_folder, os.path.basename(file_path))
            shutil.move(file_path, quarantine_path)
            print(f"File quarantined: {quarantine_path}")
        except Exception as e:
            print(f"Error quarantining file: {e}")

if __name__ == "__main__":
    antivirus = SoulAntivirus()
    print("Soul Antivirus - Scan Options:")
    print("1. Scan a specific file")
    print("2. Scan a directory")
    print("3. Scan an entire drive")

    choice = input("Choose a scan option (1, 2, or 3): ")

    if choice == "1":
        file_path = input("Enter the file path to scan: ")
        antivirus.scan_file(file_path)

    elif choice == "2":
        directory = input("Enter the directory to scan: ")
        antivirus.scan_directory(directory)

    elif choice == "3":
        drive = input("Enter the drive to scan (e.g., C:\\): ")
        antivirus.scan_drive(drive)

    else:
        print("Invalid choice. Exiting.")
