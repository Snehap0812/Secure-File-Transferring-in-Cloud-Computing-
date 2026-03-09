# Secure File Transferring in Cloud Computing

A web-based application built using Python and Flask that allows users to upload, transfer, and download files securely.
The system is designed to handle file storage in local or cloud-like folders and ensures files are safely managed during runtime.

## Features
 1.Secure file upload and download
 2.Simulated cloud storage integration
 3.User-friendly web interface
 4.Runtime handling of uploaded files
 5.Placeholder folders for uploads and cloud storage
 6.Easy to extend for real cloud integration or authentication

## Technologies Used
 1.Python
 2.Flask
 3.HTML / CSS
 4.Cloud / Local Storage (simulated)
 5.Folder-based file handling at runtime

## Project Structure
Secure-File-Transfer-System/
│
├── app.py                # Main Flask application
├── keysend.py            # Key handling (optional / dummy)
├── README.md
├── templates/            # HTML templates
│   ├── index.html
├── static/               # CSS, JS, images
|   ├── style.css
├── uploads/              # Runtime folder for uploaded files
│   └── README.md         # Explains purpose of folder
├── cloud/                # Runtime folder simulating cloud storage
│   └── README.md         # Explains purpose of folder
└── keys/                 # Dummy key files (real keys excluded)
│   ├── ecc_private.pem
│   ├── ecc.public.pem

> Note: ECC key files are generated at runtime by running `keysend.py`.  
> The `keys/` folder contains only dummy files for demonstration.

## Installation:
Follow these steps to run the project locally:

1️.Clone the repository:

```git clone https://github.com/your-username/Secure-File-Transfer-System.git```

2️.Navigate to the project folder:

```cd Secure-File-Transfer-System```

3️.Install dependencies:

```pip install -r requirements.txt```

4️.Run the Flask application:

```python app.py```

5️. Open in browser:

```http://127.0.0.1:5000```

## Screenshots

**File Upload Page**  
![Upload Page](screenshots/upload.png)

**Cloud / Runtime Storage Interaction**  
![Cloud Storage](screenshots/cloud.png)

**File Download Page**  
![Download Page](screenshots/download.png)

## System Workflow:
 1.User uploads a file via the web interface.
 2.File is stored in the uploads/ folder temporarily.
 3.Application moves the file to the cloud/ folder (simulated storage).
 4.Users can download files from the cloud folder via the interface.
 5.Runtime folders ensure the system works smoothly without pre-existing files.

## Future Enhancements:
 1.Add user authentication and access control
 2.Integrate real cloud storage (AWS S3 / Google Cloud)
 3.Add file versioning or logging for uploads/downloads
 4.Support multi-user environments

Author: Sneha P
