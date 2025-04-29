"""
ALBASIL AL-RAWAHI     138410      HW1

This script extracts email addresses from a text file.

Algorithm:

1. Function get_emails(line)
   - Splits the line into words.
   - Iterates through each word:
     - Checks if the word contains both "@" and "." (basic email format validation).
     - If valid, splits the word at "@" to separate email ID and domain.
     - Ensures the domain has at least two parts (e.g., "example.com").
     - Removes special characters from the potential email address (cleaning).
     - If the cleaned email doesn't end with a period (".") (optional validation), adds it to the list.
   - Returns the list of extracted email addresses.

2. Function email_extractor(lines)
   - Creates a set to store unique emails (avoids duplicates).
   - Iterates through each line in the input:
     - Checks if the line contains "@" (basic presence check).
     - Calls `get_emails` to extract emails from the line.
     - Adds extracted emails to the unique email set.
   - Returns the set of unique email addresses.

3. Function main()
   - Opens the input text file for reading.
   - Reads all lines from the file and stores them in a list.
   - Calls `email_extractor` to get unique emails from the lines.
   - Prints each unique email address.
   - Prints the total number of emails found.
   - Closes the input file.

"""

def get_emails(line):
    """
    Extracts email addresses from a line of text, performing basic validation.
    Returns: A list of extracted email addresses from the line.
    """
    words = line.split()
    emails = []

    for word in words:
        # Basic email format validation (must contain "@" and ".")
        if "@" not in word or "." not in word:
            continue

        # Separate email ID and domain
        format_parts = word.split("@")

        # Ensure only two parts after splitting by "@" (ID and domain)
        if len(format_parts) != 2:
            continue

        domain_parts = format_parts[1].rstrip(".").split(".")

        #Ensure domain has at least one "."
        if len(domain_parts) < 2:
            continue

        final_word = word.replace("<", "").replace(">", "").replace("(", "").replace(")", "").replace(",", "").replace(
            ":", "").replace(";", "").replace("\"", "").replace("/", "").replace("\\", "")

        # exclude emails not ending with "."
        if ( final_word.endswith(".") == False):
            emails.append(final_word)

    return emails


def email_extractor(lines):
    """
    Extracts unique email addresses from a list of lines.
    Returns: A set of unique email addresses found in the lines.
    """
    unique_emails = set()

    for line in lines:
        # look for "@" in the line
        if "@" not in line:
            continue

        emails = get_emails(line)

        # Add extracted emails to the unique email set
        for email in emails:
            unique_emails.add(email)

    return unique_emails

def main():
    # Open the input text file
    inputFile = open("text_file_part1_10klines.txt", "r")
    
    # Read all lines from the file
    inputLines = inputFile.readlines()
    
    # Extract unique emails
    emails = email_extractor(inputLines)

    # Close the input file
    inputFile.close()

    # Open the output text file
    outputFile = open("sample_output.txt", "w")

    # Write each unique email address to the output file
    for email in emails:
        outputFile.write(email + "\n")

    # Close the output file
    outputFile.close()
    # Close the input file
    inputFile.close()
    
    print("Output written to sample_output.txt")

# Call main
main()















