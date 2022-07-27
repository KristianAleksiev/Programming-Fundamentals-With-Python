def pass_reset():
    data = input()

    while True:
        command = input().split()

        if command[0] == "Done":
            print(f"Your password is: {data}")
            break

        elif command[0] == "TakeOdd":
            data = "".join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)

        elif command[0] == "Cut":
            start_index = int(command[1])
            cut_length = int(command[2])
            data = "".join([data[i] for i in range(len(data)) if i < start_index or i >= start_index + cut_length])
            print(data)

        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]

            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")


pass_reset()
