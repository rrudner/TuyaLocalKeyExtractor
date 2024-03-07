import glob
import re
import html

def find_xml_file():
    try:
        # Use glob to find XML files in the current directory
        xml_files = glob.glob("*.xml")

        # Check if exactly one XML file is found
        if len(xml_files) == 1:
            xml_file_path = xml_files[0]
            print(f"Found XML: {xml_file_path}")
            return xml_file_path
        else:
            # Raise FileNotFoundError if not exactly one XML file is found
            raise FileNotFoundError("Exactly one XML file in the folder was not found.")
    except FileNotFoundError as e:
        # Handle FileNotFoundError and exit the program
        print(f"Error: {e}")
        return None

def read_xml_content(file_path):
    try:
        # Open the XML file and read its content
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError as e:
        # Handle FileNotFoundError and exit the program
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle other exceptions during file reading and exit the program
        print(f"Error reading XML file: {e}")
        return None

def extract_data_from_xml(xml_content):
    try:
        # Define a regex pattern to extract data from XML content
        pattern = r'name&quot;:&quot;(.*?)&quot;|key&quot;:&quot;(.*?)&quot;|localKey&quot;:&quot;(.*?)&quot;'

        # Use re.findall to extract data based on the pattern
        return re.findall(pattern, xml_content)
    except re.error as e:
        # Handle regex error and exit the program
        print(f"Error in regex pattern: {e}")
        return None

def print_data(matches):
    try:
        # Iterate through the matches and print relevant data
        print("------------------------------")
        print("Devices found in XML file")
        print("------------------------------")
        for i, match in enumerate(matches):
            name, key, local_key = match
            if local_key:
                print(f"Friendly Name: {matches[i + 1][0]}")
                print(f"Device ID: {matches[i - 1][1]}")
                print(f"Local Key: {html.unescape(local_key)}")
                print("------------------------------")
    except IndexError as e:
        # Handle IndexError and exit the program
        print(f"Error accessing matches: {e}")
        return None

def main():
    # Find the XML file and get its path
    xml_file_path = find_xml_file()

    if xml_file_path is None:
        input("Press Enter to exit...")
        return

    # Read the content of the XML file
    xml_content = read_xml_content(xml_file_path)

    if xml_content is None:
        input("Press Enter to exit...")
        return

    # Extract data from the XML content using regex
    matches = extract_data_from_xml(xml_content)

    if matches is None:
        input("Press Enter to exit...")
        return

    # Print the extracted data
    print_data(matches)

    # Wait for user input before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
