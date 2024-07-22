# VCCAssignment1Q2

# Steps 

## Created a basic hello world app
Inside fastapiapp directory perform the following:

  1. Create a virtual environment using command `python3 -m venv venv`
  2. Activate the virtual environment using command `. .\venv\Scripts\activate` (In windows).
  3. Install fastapi and uvicorn using `pip install fastapi` and `pip install uvicorn`.
  4. Create a new directory app.
  5. Inside app directory create main.py with code as mentioned.
  6. Go back a directory and create a requirements.txt file using command `pip freeze > requirements.txt`

## Docker
Inside fastaiapp directory perform the following:
  1. Create a Dockerfile.
  2. Build docker image by using command `docker build -t fastapiapp .`
  3. Run the docker container using command `docker run -p 8000:8000 fastapiapp`

#G23AI2047 - Karan Sharma (g23ai2047@iitj.ac.in)
