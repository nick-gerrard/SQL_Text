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

test_input = ['apples\n', 'oranges\n']

text_processor(test_input, "test_file.txt")



