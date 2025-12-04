from setuptools import setup, find_packages

setup(
    name="devops_final_app",       # Name of your project
    version="0.1.0",               # Start with 0.1.0
    packages=find_packages(),      # Finds your app folder automatically
    install_requires=[
        "fastapi",
        "uvicorn",
        # Add other packages from your requirements.txt here
    ],
)
