# Flask API Example

This is a simple RESTful API built with Flask, a micro web framework for Python.

## Features
- RESTful endpoints to manage resources.
- JSON responses.
- Error handling for common issues.
- Lightweight and easy to extend.

## Requirements

- Python 3.10+

  
### Clone the repository
```bash
git clone https://github.com/y1220/python-api.git
cd python-api
```

## Setting up the Conda Environment

This project uses a Conda environment for dependency management. Follow the steps below to activate the environment:

### 1. Install Conda

If you don't already have Conda installed, download and install it from [Conda's official website](https://docs.conda.io/en/latest/miniconda.html). 

### 2. Create the Conda Environment (Skip this if you use venv)

If you haven't already created the environment, you can create it by running:
```bash
conda create --name python-api python=3.10
```

## 3. Setting up the Python Interpreter
When working on a Python project, it's essential to configure the Python **interpreter** correctly. 
The interpreter is the program that reads and executes your Python code. Configuring the correct interpreter ensures that your project uses the proper version of Python and the required libraries.

**In PyCharm or IntelliJ IDEA**:
   - In PyCharm or IntelliJ IDEA, you can set the Python interpreter by navigating to:
     - **File** → **Settings** → **Project Interpreter**.
     - Choose the interpreter linked to your virtual environment (e.g., `python-api` in Conda, or the `venv` directory).

**In Visual Studio Code (VS Code)**:
   - In **VS Code**, you can change the interpreter by:
     - Pressing `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and typing `Python: Select Interpreter`.
     - Choose the appropriate interpreter, either from the Conda environment or the virtual environment (`venv`).


## Installing Flask and Running the API

## 4. Install Flask

To install Flask, you need to ensure you're in the correct environment (e.g., `python-api` if you're using a Conda environment). Then, install Flask using `pip`:

```bash
pip install flask
```

## 5. Run Flask
```bash
flask run
```

## Example API Endpoint

To interact with the API, you can use the following example endpoint:

### `GET /store`

- **URL**: `http://127.0.0.1:5000/store`
- **Description**: This endpoint returns a list of all stores and their items.
- **Method**: `GET`
- **Response**: 
  - **Status**: `200 OK`
  - **Example Response**:
    ```json
    {
      "stores": [
        {
          "name": "My Store",
          "items": [
            {
              "name": "Chair",
              "price": 15.99
            }
          ]
        }
      ]
    }
    ```

### Summary of API Endpoints

| Method | Endpoint                        | Description                                          | Possible Status Codes  |
|--------|---------------------------------|------------------------------------------------------|------------------------|
| `GET`  | `/store`                        | Returns a list of all stores and their items.         | `200 OK`               |
| `POST` | `/store`                        | Creates a new store with the given name.              | `201 Created`          |
| `POST` | `/store/<string:name>/item`      | Adds a new item to the specified store by its name.   | `201 Created`, `404 Not Found` |
| `GET`  | `/store/<string:name>`           | Retrieves a specific store by its name.               | `200 OK`, `404 Not Found` |
| `GET`  | `/store/<string:name>/item`      | Retrieves all items from the specified store.         | `200 OK`, `404 Not Found` |


