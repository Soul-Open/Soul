import time
import webbrowser
import os

class SoulInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.language_name = "Soul"
        self.youtube_channel = "https://www.youtube.com/channel/UCMOdyupQQE-wWuBfqg6b_3A"

    def start(self):
        print(f"{self.language_name} Interpreter")
        print("Type 'help' to see the list of commands.")
        print(f"Visit our channel: {self.youtube_channel}\n")
        while True:
            command = input(f"{self.language_name}>>> ")
            self.execute(command)

    def execute(self, command):
        parts = command.split()
        if not parts:
            return
        action = parts[0].lower()
        if action == "open" and len(parts) >= 3 and parts[1].lower() == "alan_dasher" and parts[2].lower() == "yt":
            print("Opening the YouTube channel...")
            webbrowser.open(self.youtube_channel)
        elif action == "print":
            print(" ".join(parts[1:]))
        elif action == "open":
            url = parts[1]
            webbrowser.open(url)
        elif action == "var":
            var_name = "var"
            value = " ".join(parts[1:]) if len(parts) > 1 else None
            self.variables[var_name] = value
            print(f"Created single variable '{var_name}' with value: {value}")
        elif action == "varx":
            if len(parts) == 1:
                print("Usage: varx <mode> [...]")
                print("Modes:")
                print("1. Single value assignment: varx <value>")
                print("2. Naming mode: varx <name> [...]")
                print("3. Combined mode: varx-\"<value> Indicates the value\"-<name>")
                print("4. Named pairs mode: varx 2var name1=value1 name2=value2")
            elif len(parts) > 1:
                mode = parts[1]
                if mode == "2var":
                    for pair in parts[2:]:
                        if "=" in pair:
                            name, value = pair.split("=")
                            self.variables[name] = value
                            print(f"Created variable '{name}' with value: {value}")
                        else:
                            print(f"Invalid syntax: '{pair}'. Expected name=value.")
                elif mode.startswith("\"") and "-" in mode:
                    value_part = mode.split("-")[0].strip("\"")
                    name_part = mode.split("-")[1] if len(mode.split("-")) > 1 else None
                    if name_part:
                        self.variables[name_part] = value_part
                        print(f"Created variable '{name_part}' with value: {value_part}")
                    else:
                        print("Invalid combined mode syntax.")
                else:
                    for i, value in enumerate(parts[1:], start=1):
                        var_name = f"varx{i}"
                        self.variables[var_name] = value
                        print(f"Created variable '{var_name}' with value: {value}")
        elif action == "delay":
            delay_time = int(parts[1])
            time.sleep(delay_time)
        elif action == "allow":
            print("Instruction allowed.")
        elif action == "cd":
            if len(parts) > 1:
                try:
                    os.chdir(parts[1])
                    print(f"Changed directory to {os.getcwd()}")
                except FileNotFoundError:
                    print("Directory not found.")
            else:
                print("Please specify a directory.")
        elif action == "dir":
            print("\n".join(os.listdir()))
        elif action == "exit":
            print("Exiting the Soul interpreter.")
            exit()
        elif action == "help":
            self.show_help()
        elif action == "createfunction":
            self.create_function(parts[1:])
        elif action == "run":
            function_name = parts[1]
            self.run_function(function_name)
        elif action == "if":
            self.handle_if(parts[1:])
        elif action == "add":
            self.handle_math(parts[1:], "add")
        elif action == "subtract":
            self.handle_math(parts[1:], "subtract")
        elif action == "multiply":
            self.handle_math(parts[1:], "multiply")
        elif action == "divide":
            self.handle_math(parts[1:], "divide")
        elif action == "createfile":
            self.create_file(parts[1:])
        elif action == "readfile":
            self.read_file(parts[1:])
        elif action == "writefile":
            self.write_file(parts[1:])
        elif action == "deletefile":
            self.delete_file(parts[1:])
        else:
            print(f"Unknown command: {action}")

    def show_help(self):
        help_text = """
        Available commands:
        - print <text>             : Prints the specified text to the screen.
        - open <url>               : Opens the specified URL in the default web browser.
        - open Alan_dasher YT      : Opens the YouTube channel.
        - var <value>              : Creates a single variable named 'var' with the specified value.
        - varx <mode> [...]        : Creates multiple variables or uses special modes.
        - delay <seconds>          : Delays execution for the specified number of seconds.
        - allow                    : Allows the instruction to pass.
        - cd <directory>           : Changes the current working directory.
        - dir                      : Lists all files and directories in the current directory.
        - exit                     : Exits the Soul interpreter.
        - createfunction <name> <commands> : Defines a custom function.
        - run <function_name>      : Runs a previously defined custom function.
        - if <var> <operator> <value> <command> : Executes a command if the condition is met.
        - add <var1> <var2>        : Adds values of var1 and var2, stores in 'result'.
        - subtract <var1> <var2>   : Subtracts var2 from var1, stores in 'result'.
        - multiply <var1> <var2>   : Multiplies var1 by var2, stores in 'result'.
        - divide <var1> <var2>     : Divides var1 by var2, stores in 'result'.
        - createfile <filename>    : Creates an empty text file with the specified name.
        - readfile <filename>      : Displays the contents of the specified file.
        - writefile <filename> <text> : Writes the specified text to the file.
        - deletefile <filename>    : Deletes the specified file.
        """
        print(help_text)

    def create_function(self, parts):
        name = parts[0]
        command = " ".join(parts[1:])
        self.functions[name] = command
        print(f"Function '{name}' created.")

    def run_function(self, name):
        if name in self.functions:
            self.execute(self.functions[name])
        else:
            print(f"Function '{name}' not found.")

    def handle_if(self, parts):
        var_name, operator, value, *command = parts
        if var_name in self.variables:
            var_value = self.variables[var_name]
            if operator == "==" and var_value == value:
                self.execute(" ".join(command))
            elif operator == "!=" and var_value != value:
                self.execute(" ".join(command))
            else:
                print("Condition not met.")

    def handle_math(self, parts, operation):
        var1, var2 = parts
        if var1 in self.variables and var2 in self.variables:
            val1 = int(self.variables[var1])
            val2 = int(self.variables[var2])
            if operation == "add":
                self.variables["result"] = val1 + val2
            elif operation == "subtract":
                self.variables["result"] = val1 - val2
            elif operation == "multiply":
                self.variables["result"] = val1 * val2
            elif operation == "divide":
                self.variables["result"] = val1 / val2 if val2 != 0 else None
            print(f"Result of {operation}: {self.variables['result']}")
        else:
            print("Variables not found.")

    def create_file(self, parts):
        filename = parts[0]
        open(filename, 'w').close()
        print(f"File '{filename}' created.")

    def read_file(self, parts):
        filename = parts[0]
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")

    def write_file(self, parts):
        filename = parts[0]
        text = " ".join(parts[1:])
        with open(filename, 'a') as file:
            file.write(text + "\n")
        print(f"Text written to '{filename}'.")

    def delete_file(self, parts):
        filename = parts[0]
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        except FileNotFoundError:
            print("File not found.")

if __name__ == "__main__":
    SoulInterpreter().start()
