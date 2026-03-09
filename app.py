from flask import Flask, render_template, request, send_file
import os
import time
import hashlib
from cryptography.fernet import Fernet

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CLOUD_FOLDER = "cloud"
KEY_FILE = "key.key"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CLOUD_FOLDER, exist_ok=True)

# Generate key if not exists
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    files = [f for f in os.listdir(CLOUD_FOLDER) if f.endswith(".bin")]
    return render_template("index.html", files=files)


# ---------------- ENCRYPT ----------------
@app.route("/encrypt", methods=["POST"])
def encrypt_file():

    file = request.files["file"]

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    start = time.time()

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)

    enc_filename = file.filename + ".bin"
    enc_path = os.path.join(CLOUD_FOLDER, enc_filename)

    with open(enc_path, "wb") as f:
        f.write(encrypted_data)

    # SHA256 HASH
    file_hash = hashlib.sha256(data).hexdigest()

    # Save hash
    hash_path = os.path.join(CLOUD_FOLDER, file.filename + ".hash")
    with open(hash_path, "w") as f:
        f.write(file_hash)

    end = time.time()
    encryption_time = round(end - start, 5)

    file_size = len(data)

    return render_template(
        "encrypt_result.html",
        filename=enc_filename,
        file_hash=file_hash,
        time=encryption_time,
        size=file_size
    )


# ---------------- DECRYPT ----------------
@app.route("/decrypt", methods=["POST"])
def decrypt_file():

    filename = request.form["filename"]

    enc_path = os.path.join(CLOUD_FOLDER, filename)

    start = time.time()

    with open(enc_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    dec_filename = filename.replace(".bin", "")
    dec_path = os.path.join(UPLOAD_FOLDER, dec_filename)

    with open(dec_path, "wb") as f:
        f.write(decrypted_data)

    end = time.time()
    decryption_time = round(end - start, 5)

    # NEW HASH
    new_hash = hashlib.sha256(decrypted_data).hexdigest()

    # READ ORIGINAL HASH
    hash_file = dec_filename + ".hash"
    hash_path = os.path.join(CLOUD_FOLDER, hash_file)

    with open(hash_path, "r") as f:
        original_hash = f.read()

    # INTEGRITY CHECK
    if new_hash == original_hash:
        status = "VERIFIED"
    else:
        status = "FAILED"

    return render_template(
        "decrypt_result.html",
        filename=dec_filename,
        time=decryption_time,
        integrity_hash=new_hash,
        status=status
    )


# ---------------- DOWNLOAD ----------------
@app.route("/download/<filename>")
def download(filename):

    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)