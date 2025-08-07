# Simple LLM Chat with Google Gemini

This is a basic command-line Python application that demonstrates how to interact with Google's Gemini 1.5 Pro model using the LangChain framework.

---

## Features

-   **Direct Interaction**: Send a query directly to the Gemini model from your terminal.
-   **Secure**: Uses a `.env` file to keep your Google API key safe and out of version control.
-   **Clean Setup**: Leverages a virtual environment and a `requirements.txt` file for a clean, reproducible setup.

---

## Prerequisites

-   Python 3.8 or higher
-   A Google API key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Setup & Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository:**

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

**2. Create and activate a virtual environment:**

This keeps your project's dependencies isolated from your system's Python installation.

  - **Windows (PowerShell):**

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

  - **macOS / Linux:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

**3. Create your environment file:**

Create a file named `.env` in the root of your project folder. This file will store your secret API key. Add the following line to it:

```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

*Replace `YOUR_API_KEY_HERE` with your actual Google API key.*

**4. Install the required packages:**

The `requirements.txt` file contains all the necessary Python libraries for this project.

```bash
pip install -r requirements.txt
```

*(If you haven't created a `requirements.txt` file yet, you can do so by running `pip freeze > requirements.txt` after installing the packages manually.)*

-----

## Usage

Once the setup is complete, you can run the main script.

```bash
python your_script_name.py
```
![Uploading image.png…]()



*(Replace `your_script_name.py` with the actual name of your Python file.)*

The script will then print the model's response to the hardcoded question "what is llms?" directly to your terminal.

-----

## Built With

  - [Python](https://www.python.org/)
  - [LangChain](https://python.langchain.com/)
  - [LangChain Google Generative AI](https://python.langchain.com/docs/integrations/chat/google_generative_ai)

\
