# Week 4: File Handling

def main():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return
    
    # Modify content 
    modified_content = content.upper()
    
    # Write to new file
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to '{new_filename}'.")

if __name__ == "__main__":
    main()
