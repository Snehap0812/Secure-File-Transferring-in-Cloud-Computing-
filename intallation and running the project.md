##Installation & Running the Project
#1️.Install Python

Make sure Python 3.x is installed on your system.

Check with:
  ```python --version (or) python3 --version```

#2️.Clone the Repository
  ```git clone https://github.com/your-username/Secure-File-Transfer-System.git```

#3️.Navigate to the Project Folder
  ```cd Secure-File-Transfer-System```
#4️.Install Dependencies

All required libraries are listed in requirements.txt:

  ```pip install -r requirements.txt```

#Explanation of dependencies:

Flask → for web application and routing

cryptography → for ECC key generation, AES encryption, and SHA-256 hashing

#Test installation:

Open Python and try:

import flask
import cryptography

If no errors appear, dependencies are installed correctly.

#5️.Run the Flask Application
  ```python app.py```

or if your system uses Python 3:

  ```python3 app.py```

You should see output like:

  ``` Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```

#6️.Open in Browser

Visit:
  ```http://127.0.0.1:5000```

Now you can upload, encrypt, and download files via the web interface.

#7️.Optional: ECC Key Generation

If your project requires ECC keys, run:
  ```python keysend.py```

This will generate ecc_private.pem and ecc_public.pem in the keys/ folder.
