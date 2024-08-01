# VCard Generator
This Python script generates a set of vCard (Virtual Contact File) files based on a predefined set of contacts. The generated vCards can be used to import contacts into various address book applications.

## Features
- Generates a specified number of vCard files
- Loads contact data from a JSON file
- Modifies phone numbers by randomly changing one digit
- Prefixes phone numbers with a specified country code
- Writes the generated vCards to a file in the current directory
## Requirements
- Python 3.x

## Usage
Clone the repository or download the script file VCardGenerator.py.
Ensure you have the contacts-4k.json file in the same directory as the script.
Run the script using the following command:

```
python generate-vcf.py
```

The script will prompt you to enter the following information:
- Number of vCards to generate (e.g., 100)
- Mobile number country code (e.g., +1)
- Number of mobile number digits (e.g., 10)
The script will generate the specified number of vCards and write them to a file named contacts_<count>.vcf in the current directory.

## Customization
You can customize the script by modifying the following:

- The contacts-4k.json file to use your own contact data.
- The generate_vcard method to include additional vCard fields or modify the existing ones.
- The generate_phone_number and modify_phone_number methods to change the phone number generation and modification logic.

## License
This project is licensed under the MIT License.
