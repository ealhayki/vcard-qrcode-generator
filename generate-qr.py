import vobject
import qrcode
import os

# Function to create a vCard
def create_vcard(name, title, phone, email, org):
    # Create a vCard object
    vcard = vobject.vCard()
    
    # Add contact details
    vcard.add('fn').value = name

    # Add the Name (N) field explicitly (First, Last, etc.)
    name_parts = name.split()
    vcard.add('n').value = vobject.vcard.Name(family=name_parts[-1], given=' '.join(name_parts[:-1]))

    vcard.add('title').value = title
    vcard.add('tel').value = phone
    vcard.add('email').value = email
    vcard.add('org').value = org

    # Specify the folder for saving the vCard file
    folder = 'vcard_files'
    if not os.path.exists(folder):
        os.makedirs(folder)  # Create the folder if it doesn't exist
    
    # Save the vCard as a .vcf file
    vcard_filename = os.path.join(folder, name.replace(" ", "-") + "_contact.vcf")
    with open(vcard_filename, 'w') as f:
        f.write(vcard.serialize())
    
    return vcard_filename

# Function to generate a QR code from the vCard
def generate_qrcode(name, vcard_file):
    # Read the vCard file content
    with open(vcard_file, 'r') as file:
        vcard_data = file.read()
    
    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    # Specify a folder for QR code images
    folder = 'qr_codes'
    if not os.path.exists(folder):
        os.makedirs(folder)  # Create the folder if it doesn't exist
    
    # Create and save the QR code image with the name (replace spaces with '-')
    qr_filename = os.path.join(folder, name.replace(" ", "-") + "_qr.png")
    img = qr.make_image(fill='black', back_color='white')
    img.save(qr_filename)
    
    print(f"QR code saved as {qr_filename}")

# Main function to handle input and process contact info
def main():
    # Get user input for contact details
    name = input("Enter contact name: ")
    title = input("Enter position title: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    org = input("Enter organization: ")
    
    # Create vCard file
    vcard_file = create_vcard(name, title, phone, email, org)
    print(f"vCard saved as {vcard_file}")
    
    # Generate QR code from vCard
    generate_qrcode(name, vcard_file)

if __name__ == "__main__":
    main()
