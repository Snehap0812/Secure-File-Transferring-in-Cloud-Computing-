# Secure File Transfer System in Cloud Computing

A web-based application built using **Python** and **Flask** that demonstrates secure file uploading, transferring, and downloading. The system is designed to simulate cloud storage environments while ensuring files are managed safely during runtime using **Elliptic Curve Cryptography (ECC)**.



## Features

1.  **Secure File Transfer:** Robust upload and download functionality.
2.  **ECC Integration:** Uses Elliptic Curve Cryptography for secure key handling (via `keysend.py`).
3.  **Simulated Cloud Storage:** Emulates cloud-like storage architecture using localized runtime folders.
4.  **User-Friendly Interface:** Clean, responsive web UI built with HTML5 and CSS3.
5.  **Dynamic Runtime Handling:** Automatic management of temporary `uploads/` and persistent `cloud/` storage.
6.  **Extensible:** Ready for integration with real providers like AWS S3 or Google Cloud Storage.

## Technologies Used

### Core Stack
1. **Backend:** Python 3.x, Flask  
2. **Frontend:** HTML5, CSS3, JavaScript  
3. **Storage:** Localized Folder-based handling (Cloud Simulation)  

### Security & Cryptography
1. **ECC (Elliptic Curve Cryptography):** Used for secure key generation and handling.  
2. **AES Encryption:** Ensures data confidentiality during file transfer.  
3. **SHA-256 Hashing:** Used for verifying file integrity and security checks.

## Project Structure
```
Secure-File-Transfer-System/
├── app.py              # Main Flask application logic
├── keygen.py           # ECC key generation and handling
├── requirements.txt    # Project dependencies 
├── README.md           # Project documentation
├── templates/          # HTML templates
│   └── index.html
├── static/             # CSS, JS, and UI assets
│   └── style.css
├── uploads/            # Temporary runtime folder for incoming files
├── cloud/              # Simulated cloud storage destination
└── keys/               # Directory for ECC private/public keys
    ├── dummy_private.pem
    └── dummy_public.pem
```
```
> Note: ECC key files are generated at runtime by running `keysend.py`.  
> The `keys/` folder contains only dummy files for demonstration.
```

## Installation:
Follow these steps to run the project locally:

1️.Clone the repository:

```git clone https://github.com/your-username/Secure-File-Transfer-System.git```

2️.Navigate to the project folder:

```cd Secure-File-Transfer-System```

3️.Install dependencies:

```pip install -r requirements.txt```
> Note: The requirements.txt contains all the necessary Python packages such as Flask and cryptography.

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

## System Workflow

The application follows a structured lifecycle to ensure data integrity and simulated cloud security:

1.  **User Upload:** The user selects a file through the web interface.
2.  **Staging:** The file is initially stored in the `uploads/` directory for temporary processing.
3.  **Cloud Transfer:** The system moves the file to the `cloud/` folder, which acts as the simulated persistent storage.
4.  **Secure Retrieval:** Users can browse and download files directly from the cloud storage via the secure interface.
5.  **Runtime Management:** The system automatically manages local directories to ensure a smooth experience without needing pre-existing manual folder creation.

## Future Enhancements

To take this project to a production-ready level, the following features are planned:

1. **User Authentication:** Implement robust login systems with role-based access control (RBAC).
2. **Production Cloud Integration:** Replace the simulated storage with **AWS S3** or **Google Cloud Storage** buckets.
3. **Version Control & Logging:** Add file versioning and a detailed audit trail for every upload and download action.
4. **Multi-Tenancy:** Support multi-user environments with private, isolated folders for each account.

---

Author: Sneha P

## Disclaimer

This project is intended for educational purposes regarding cloud simulation and ECC logic.  
Ensure proper security protocols are followed before deploying to a production environment.
