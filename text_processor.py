def text_processor(input_list, text_to_process):
    with open(text_to_process, "r+") as input_file, open("processed_file.txt", "w+") as output_file:
        for line in input_file:
            remove = False
            for value in input_list:
                if value == line:
                    print("Removing Line...")
                    remove = True
            if remove == True:
                print("Line removed...")

            else:
                output_file.write(line)

        input_file.seek(0)
        output_file.seek(0)
        print(output_file.read())

#test_input = ['apples\n', 'oranges\n']

#text_processor(test_input, "test_file.txt")

#Selecting and testing files

file_to_process = input("Enter the name of the file to process: ")
valid_file = False
try:
    with open(file_to_process, "r") as testing_valid_file:
        head = [next(testing_valid_file) for x in range(5)]
        print("Valid File...printing first 5 lines...")
        print(head)
        valid_file = True
except:
    print("Not a valid file...")

print("\n\n\n")

#Testing the input list

list_of_terms_to_remove = input("Enter the name of the list of values to remove: ")

valid_file = False

try:
    with open(list_of_terms_to_remove, "r") as testing_valid_file:
        head = [next(testing_valid_file) for x in range(5)]
        print("Valid Input list File...printing first 5 lines...")
        print(head)
        valid_file = True
except:
    print("Not a valid file...")

#Generating the input list.

if valid_file == True:
    input_list = []

    with open(list_of_terms_to_remove) as input_values:
        for value in input_values:
            input_list.append(value)
        
#Calling the function

    text_processor(input_list, file_to_process)
    
else:
    print("Invalid files...please try again...")

