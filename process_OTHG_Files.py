def process_OTHG_files():
    # Step 1: Modify line endings in the binary file
    # Define the replacement bytes sequence (CR, CR, LF)
    bte_replace = [13, 13, 10]
    # Open the original file for reading in binary mode and a new file for writing the modified content
    with open("YOUR FILE PATH/YOUR FILE.txt", "rb") as infile, \
         open("YOUR FILE PATH/YOUR FILE.txt", "wb") as outfile:
        prev_byte = None
        # Read through each byte in the input file
        for current_byte in iter(lambda: infile.read(1), b''):
            # Check if the previous and current bytes are newline characters to replace them
            if prev_byte == b'\n' and current_byte == b'\n':
                outfile.write(bytes(bte_replace))
                prev_byte = None  # Reset prev_byte to avoid duplication in replacements
            else:
                # Write the previous byte (if not the first iteration) and update prev_byte
                if prev_byte is not None:
                    outfile.write(prev_byte)
                prev_byte = current_byte
        # Write the last byte to the output file if it wasn't a newline
        if prev_byte is not None:
            outfile.write(prev_byte)

    print("Line ending modification complete.")

    # Step 2: Process the modified file based on the first character of each line
    # Initialize counters for different categories
    counters = {
        "line_number": 0,
        "blank_line_number": 0,
        "packet_number": 0,
        "contact_rpt_number": 0,
        "x_position_number": 0,
        "ais_rpt_number": 0,
        "slash_number": 0,
        "unclas_number": 0,
        "msgid_number": 0,
        "end_packet_number": 0,
        "delete_number": 0,
        "unexpected_number": 0,
    }

    # Open the modified file for reading and a file for writing unexpected lines
    with open("YOUR FILE PATH/YOUR FILE", "r") as infile, \
         open("YOUR FILE PATH/YOUR FILE", "w") as outfile:
        # Iterate through each line in the modified file
        for line in infile:
            counters["line_number"] += 1
            # Skip processing and increment counter if the line is blank
            if not line.strip():
                counters["blank_line_number"] += 1
                continue
            str_first_char = line[0]

            # Categorize the line based on its first character and update corresponding counter
            # Write specific information to the output file for certain categories
            if str_first_char == "B":
                lng_str_length = len(line)
                outfile.write(f"{counters['line_number']} {lng_str_length}\n")
                counters["packet_number"] += 1
            elif str_first_char == "C":
                counters["contact_rpt_number"] += 1
            elif str_first_char == "X":
                counters["x_position_number"] += 1
            elif str_first_char == "A":
                counters["ais_rpt_number"] += 1
            elif str_first_char == "/":
                counters["slash_number"] += 1
            elif str_first_char == "U":
                counters["unclas_number"] += 1
            elif str_first_char == "M":
                counters["msgid_number"] += 1
            elif str_first_char == "E":
                counters["end_packet_number"] += 1
            elif str_first_char == "D":
                counters["delete_number"] += 1
            else:
                # If the line does not fit any category, mark it as unexpected
                counters["unexpected_number"] += 1
                outfile.write(f"First Character {str_first_char} Line Number {counters['line_number']}\n")

    print("First character processing complete.")

    # Print a summary of the counts for each category
    for key, value in counters.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

# Run the process_OTHG_files function
process_OTHG_files()
