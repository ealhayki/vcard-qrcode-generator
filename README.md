# vCard QR Code Generator

This project is a Python-based tool that allows users to generate a digital **vCard** and encode it into a **QR code**. The QR code contains all the contact details in the vCard format (.vcf), making it easy to share and add contact information directly to a mobile device’s address book by simply scanning the code.

The tool helps automate the creation of a vCard file with essential details such as:

- Name
- Phone number
- Email address
- Job Title (Position)
- Organization (Company)

## Features:
- **vCard Creation**: Creates a vCard file containing personalized contact information such as name, phone, email, job title, etc.
- **QR Code Generation**: Generates a QR code that encodes the contact information in a scannable format, making it easy to add the contact to a device's address book.
- **Downloadable vCard (.vcf)**: The generated vCard file can be downloaded and saved for importing into contact management systems.

## Tech Stack:
- **Python**: The main programming language used to generate the vCard and QR code.
- **Libraries**:
  - `qrcode`: To generate the QR code.
  - `vobject`: To create and manipulate vCard data.
  
## How It Works:
1. Run the `generate-qr.py` Python script.
2. Provide your contact details (e.g., name, phone number, email, job title).
3. The script will generate a vCard file (.vcf) containing the contact information.
4. A QR code is also created, which can be scanned by mobile devices to automatically add the contact details to the address book.
5. Both the QR code and vCard file are saved locally on (qr_codes) and (vcard_files) directories, and you can share the QR code or distribute the .vcf file as needed.

## Usage:
1. **Run the Script**: Run the script using Python .
2. **Scan QR Code**: After running the script, you can scan the generated QR code to instantly add the contact to your device.
3. **Download the vCard**: You can also download and manually import the vCard file into your contact manager.

## How to Run:
1. Clone the repository `https://github.com/ealhayki/vcard-qrcode-generator.git` or download the `generate-qr.py` file.
2. Install the required libraries using pip:
   ```bash
   pip install qrcode[pil] vobject
   ```
3. Run the `generate-qr.py` file:
   ```bash
   python generate-qr.py
   ```
4. The script will generate a `CONTACT-NAME_contact.vcf` file and a `CONTACT-NAME_qr.png` QR code image with your contact details.
