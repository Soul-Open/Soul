#include <iostream>
#include <string>
#include <cstdlib>  // For system() to open the browser
#include <map>  // For std::map
#ifdef _WIN32
#include <windows.h>  // For Sleep() on Windows
#else
#include <unistd.h>  // For sleep() on Unix/Linux systems
#endif

// Function to simulate the installation process
void handleInstall(const std::string& packageName) {
    std::cout << "Installing package: " << packageName << std::endl;
    std::cout << "Downloading..." << std::endl;

    // Simulate delay of 1 second
    #ifdef _WIN32
    Sleep(1000);  // Sleep for 1 second (Windows Sleep is in milliseconds)
    #else
    sleep(1);  // Sleep for 1 second (Unix sleep is in seconds)
    #endif

    // Simulating download status
    std::cout << "[https://example.com/some-library = 1m 23s, 500KB/s, 10MB remaining]" << std::endl;

    // Searching the URL on Google
    std::string searchQuery = "https://www.google.com/search?q=" + packageName;
    std::string command = "start chrome \"" + searchQuery + "\"";  // Command for Windows (using Chrome)
    system(command.c_str());  // This opens Google in your default browser

    // Simulate some more downloading time
    #ifdef _WIN32
    Sleep(2000);  // Sleep for 2 seconds (Windows Sleep is in milliseconds)
    #else
    sleep(2);  // Sleep for 2 seconds (Unix sleep is in seconds)
    #endif

    std::cout << "Download complete!" << std::endl;
}

// Function to display a message
void displayMessage(const std::string& message) {
    std::cout << message << std::endl;
}

// Function to simulate taking input like Python's input() function
std::string takeInput(const std::string& prompt) {
    std::cout << prompt;
    std::string input;
    std::getline(std::cin, input);
    return input;
}

// Function to define a variable and store it in a map
void defineVar(std::map<std::string, std::string>& variables, const std::string& varName, const std::string& value) {
    variables[varName] = value;
    std::cout << "Variable " << varName << " set to " << value << std::endl;
}

// Function to handle mathematical operations
void handleMath(const std::string& operation, int a, int b) {
    if (operation == "add") {
        std::cout << "Result: " << a + b << std::endl;
    } else if (operation == "subtract") {
        std::cout << "Result: " << a - b << std::endl;
    } else if (operation == "multiply") {
        std::cout << "Result: " << a * b << std::endl;
    } else if (operation == "divide") {
        if (b != 0) {
            std::cout << "Result: " << a / b << std::endl;
        } else {
            std::cout << "Error: Division by zero!" << std::endl;
        }
    }
}

// Function to display the help information
void displayHelp() {
    std::cout << "\nAvailable commands:\n";
    std::cout << "1. install <package>    - Simulate the installation of a package.\n";
    std::cout << "2. display              - Displays example text.\n";
    std::cout << "3. take                 - Simulate taking user input.\n";
    std::cout << "4. var <variable_name>  - Defines a variable with the specified name.\n";
    std::cout << "5. var -c               - Define multiple variables at once.\n";
    std::cout << "6. add <a> <b>          - Add two numbers.\n";
    std::cout << "7. subtract <a> <b>     - Subtract two numbers.\n";
    std::cout << "8. multiply <a> <b>     - Multiply two numbers.\n";
    std::cout << "9. divide <a> <b>       - Divide two numbers.\n";
    std::cout << "10. exit                - Exit the interpreter.\n";
    std::cout << "11. help                - Display this help message.\n";
}

// Main function where user inputs commands
int main() {
    std::map<std::string, std::string> variables;

    // Example commands
    std::string command;
    while (true) {
        std::cout << "Soul Interpreter> ";
        std::getline(std::cin, command);

        if (command == "exit") {
            break;
        } else if (command == "help") {
            displayHelp();  // Show the help message
        } else if (command.find("install") != std::string::npos) {
            std::string package = command.substr(8);  // Remove "install " from the command
            handleInstall(package);
        } else if (command.find("display") != std::string::npos) {
            displayMessage("Example text here");
        } else if (command.find("take") != std::string::npos) {
            std::string userInput = takeInput("Please enter a value: ");
            std::cout << "You entered: " << userInput << std::endl;
        } else if (command.find("var") != std::string::npos) {
            if (command.find("-c") != std::string::npos) {
                std::cout << "Number of variables to define: 3" << std::endl;
                defineVar(variables, "name1", takeInput("Enter value for name1: "));
                defineVar(variables, "name2", takeInput("Enter value for name2: "));
                defineVar(variables, "name3", takeInput("Enter value for name3: "));
            } else {
                std::string varName = command.substr(4);  // Remove "var " from the command
                std::string value = takeInput("Enter value for " + varName + ": ");
                defineVar(variables, varName, value);
            }
        } else if (command.find("add") != std::string::npos || command.find("subtract") != std::string::npos || 
                   command.find("multiply") != std::string::npos || command.find("divide") != std::string::npos) {
            std::string operation;
            int a, b;
            if (command.find("add") != std::string::npos) {
                operation = "add";
            } else if (command.find("subtract") != std::string::npos) {
                operation = "subtract";
            } else if (command.find("multiply") != std::string::npos) {
                operation = "multiply";
            } else if (command.find("divide") != std::string::npos) {
                operation = "divide";
            }

            std::cout << "Enter two numbers: ";
            std::cin >> a >> b;
            handleMath(operation, a, b);
        } else {
            std::cout << "Command not recognized! Type 'help' for a list of commands." << std::endl;
        }
    }

    return 0;
}
