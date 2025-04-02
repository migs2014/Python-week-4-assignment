# Function to modify the content (makes text uppercase)
def edit (content):
   return content.upper()
    
# Main program
try:
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read: ")

    # Open the input file and read its content
    with open(input_file, 'r') as file:
        content = file.read()

    # Modify the content
    modified_content = edit(content)

    # Ask the user for the output file name
    output_file = input("Enter the name of the file to save: ")

    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        file.write(modified_content)

    print("The file has been modified and saved!")
except FileNotFoundError:
    print("Error: The file was not found!")
except Exception as e:
    print("An error occurred:", e)