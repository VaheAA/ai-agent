# 🤖 AI Coding Agent - Learning Project

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-Educational%20Only-red.svg)
![Status](https://img.shields.io/badge/status-Learning%20Project-yellow.svg)

## ⚠️ IMPORTANT DISCLAIMER - FOR LEARNING PURPOSES ONLY ⚠️

**THIS PROJECT IS STRICTLY FOR EDUCATIONAL AND LEARNING PURPOSES ONLY.**

🚫 **NOT FOR PRODUCTION USE** 🚫

This is a simplified, demonstration-only AI agent implementation created to help understand the basic concepts of building AI-powered coding assistants. It should **NOT** be used as:

- A real coding assistant in professional environments
- A production-ready AI agent solution
- A replacement for established development tools
- A secure system for handling sensitive code or data

**Key limitations include but are not limited to:**

- Basic error handling and security measures
- Limited functionality scope
- No comprehensive testing suite
- Simplified architecture not suitable for real-world scenarios
- Potential security vulnerabilities
- No data protection or privacy safeguards

## 📚 What This Project Demonstrates

This educational project showcases fundamental concepts of building an AI coding agent using Google's Gemini AI model. It demonstrates:

- **Function Calling**: How AI models can interact with external tools and APIs
- **File System Operations**: Basic file reading, writing, and directory listing
- **Code Execution**: Running Python scripts with parameters
- **Conversational AI**: Multi-turn conversations with function call capabilities
- **Tool Integration**: Connecting AI models with custom functions

## 🏗️ Project Structure

```
ai-agent/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── functions/             # AI function declarations and implementations
│   ├── get_files_info.py   # List directory contents
│   ├── get_file_content.py # Read file contents
│   ├── write_file.py       # Write/overwrite files
│   ├── run_python.py       # Execute Python scripts
│   └── call_function.py    # Function dispatcher
├── calculator/            # Example project for the agent to work with
│   ├── main.py           # Calculator application
│   ├── tests.py          # Test suite
│   └── pkg/              # Calculator package
└── tests.py              # Agent tests
```

## 🚀 Quick Start (For Learning Only)

### Prerequisites

- Python 3.12 or higher
- Google AI API key (Gemini)
- Basic understanding of AI concepts and Python

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd ai-agent
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   # OR if using uv:
   uv sync
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_google_ai_api_key_here
   ```

### Usage Examples

**Basic usage:**

```bash
python main.py "List all files in the current directory"
```

**With verbose output:**

```bash
python main.py "Fix the calculator and run tests" --verbose
```

**File operations:**

```bash
python main.py "Read the calculator README and explain what it does"
```

**Code execution:**

```bash
python main.py "Run the calculator with the expression '2 + 3 * 4'"
```

## 🔧 Available Functions

The AI agent has access to these learning-focused functions:

| Function           | Description                              | Learning Purpose                     |
| ------------------ | ---------------------------------------- | ------------------------------------ |
| `get_files_info`   | Lists directory contents with file sizes | Understanding file system navigation |
| `get_file_content` | Reads and returns file contents          | File I/O operations                  |
| `write_file`       | Creates or overwrites files              | File manipulation                    |
| `run_python_file`  | Executes Python scripts with arguments   | Code execution and testing           |

## ⚙️ Configuration

Key configuration options in `config.py`:

- `MAX_CHARS = 10000`: Maximum characters to read from files
- `WORKING_DIR = "./calculator"`: Sandboxed working directory
- `MAX_ITERS = 20`: Maximum conversation iterations

## 🎯 Learning Objectives

By studying this project, you can learn about:

1. **AI Function Calling**: How to define and implement functions that AI models can call
2. **Prompt Engineering**: Crafting system prompts for AI agents
3. **API Integration**: Working with Google's Gemini AI API
4. **Error Handling**: Basic error management in AI applications
5. **Conversation Flow**: Managing multi-turn AI conversations
6. **Tool Design**: Creating tools for AI agents to use

## 🧪 Example Interactions

**File Analysis:**

```
User: "What files are in the calculator directory?"
Agent: [Calls get_files_info] → Lists all files with sizes and types
```

**Code Review:**

```
User: "Read the calculator main.py and explain how it works"
Agent: [Calls get_file_content] → Reads file and provides explanation
```

**Testing:**

```
User: "Run the calculator tests and tell me the results"
Agent: [Calls run_python_file] → Executes tests and reports results
```

## 🚨 Security and Safety Notes

**For Educational Use Only - Not Production Ready:**

- ❌ No input sanitization for file paths
- ❌ Limited error handling and validation
- ❌ No authentication or authorization
- ❌ No rate limiting or resource protection
- ❌ Potential for directory traversal vulnerabilities
- ❌ No logging or audit trail
- ❌ Basic exception handling only

**Remember**: Keep contributions focused on educational value, not production readiness.

## 📄 License

This project is for educational purposes only. No warranty or support is provided. Use at your own risk for learning only.

## 🙋 Support and Questions

This is a learning project with no formal support. However, you can:

- Review the code to understand the concepts
- Experiment with modifications (in a safe environment)
- Use it as a starting point for your own educational projects
- Share your learning experiences with the community

---

**Remember: This is a learning tool, not a production system. Always prioritize security, testing, and best practices in any real-world application.**
