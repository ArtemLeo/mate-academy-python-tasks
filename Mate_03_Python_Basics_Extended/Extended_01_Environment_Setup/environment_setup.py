"""
Setting up a Python environment involves installing Python itself, managing packages,
and possibly creating virtual environments for different projects:

1. Install Python
2. Verify Python Installation
3. Package Manager (pip)
4. Virtual Environments
5. Install Packages
6. Requirements.txt
7. IDEs and Text Editors


# 1. Install Python:
Visit the official Python website (https://www.python.org/) and download the latest version
of Python. Follow the installation instructions for your operating system.

# 2. Verify Python Installation:
Open a command prompt or terminal and type the following command to check if Python is installed
successfully:

--> python --version <--

# 3. Package Manager (pip):
Python comes with a package manager called pip that allows you to install
and manage Python packages. You should have pip installed by default.
You can check its version with:

--> pip --version <--

If pip is not installed, or you want to upgrade it, you can use:

--> python -m ensurepip --default-pip <--
--> python.exe -m pip install --upgrade pip <--

# 4. Virtual Environments:
Virtual environments help manage dependencies for different projects.
They provide an isolated space for each project, preventing conflicts between package versions.

Create a Virtual Environment:
# On Windows
--> python -m venv venv <--

# On macOS or Linux
--> python3 -m venv venv <--

Activate a Virtual Environment:
# On Windows
--> venv\Scripts\activate <--

# On macOS or Linux
--> source venv/bin/activate <--

# 5. Install Packages:
Once inside your virtual environment, you can use pip to install packages:

--> pip install package_name <--

# 6. Requirements.txt:
For project consistency, create a requirements.txt file with a list of your project's dependencies.

You can generate it using:
--> pip freeze > requirements.txt <--

To install dependencies from a requirements.txt file:
--> pip install -r requirements.txt <--

# 7. IDEs and Text Editors:
Choose an Integrated Development Environment (IDE) or text editor for coding.
Popular choices include VSCode, PyCharm, Atom, Sublime Text, and others.

"""
