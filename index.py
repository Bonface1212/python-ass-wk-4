def modify_content(content):
    # Example modification: Convert content to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the name of the file to read: ")
        
        # Try opening and reading the file
        with open(input_filename, "r") as infile:
            original_content = infile.read()
        
        # Modify the content
        modified_content = modify_content(original_content)

        # Ask the user for the output file name
        output_filename = input("Enter the name of the new file to write: ")

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except IOError:
        print("❌ Error: There was a problem reading or writing the file.")

if __name__ == "__main__":
    main()
