import os
import json
import random
import string

class VCardGenerator:
    def generate_vcard(self, count, country_code, phone_number_digits):
        # Load the contacts data from the JSON file
        with open('contacts-4k.json', 'r') as f:
            contacts = json.load(f)

        # Create the output file
        output_file = f'contacts_{count}.vcf'

        with open(output_file, 'w') as f:
            for _ in range(count):
                # Select a random contact from the list
                contact = random.choice(contacts)
                name = contact['NAME']
                phone_number = self.generate_phone_number(phone_number_digits)
                email_list = contact['EMAIL_LIST']
                addresses = contact['ADDRESSES']

                # Generate the vCard
                vcard = [
                    'BEGIN:VCARD',
                    'VERSION:3.0',
                    f'N:{name.split(" ")[1]};{name.split(" ")[0]};;;',
                    f'FN:{name}',
                    *[f'EMAIL;type=HOME:{email}' for email in email_list],
                    *[f'TEL;type=HOME:{self.modify_phone_number(phone_number, country_code)}'],
                    *[f'TEL;type=WORK:{self.modify_phone_number(phone_number, country_code)}'],
                    *[f'ADR;type=HOME:;;;{address.get("address", "")};{address.get("city", "")};{address.get("state", "")};{address.get("zip", "")}' for address in addresses],
                    'END:VCARD'
                ]

                f.write('\n'.join(vcard) + '\n')

    def generate_phone_number(self, digits):
        return ''.join(random.choices(string.digits, k=digits))

    def modify_phone_number(self, phone_number, country_code):
        # Modify the phone number by changing one digit
        digits = list(phone_number.replace('+', '').replace(' ', '').replace('-', ''))
        index = random.randint(0, len(digits) - 1)
        digits[index] = str(random.randint(0, 9))
        phone_number = ''.join(digits)

        # Prefix the phone number with the country code
        if not phone_number.startswith(country_code):
            phone_number = country_code + phone_number

        return phone_number

if __name__ == '__main__':
    generator = VCardGenerator()

    while True:
        count = input('Enter the number of vCards to generate (Ex: 100): ')
        if count.isdigit() and int(count) > 0:
            count = int(count)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    while True:
        country_code = input('Enter the mobile number country code (Ex: +1): ')
        if country_code.startswith('+') and len(country_code) > 1:
            break
        else:
            print("Invalid input. Please enter a valid country code starting with '+'.")

    while True:
        phone_number_digits = input('Enter the number of mobile number digits: ')
        if phone_number_digits.isdigit() and int(phone_number_digits) > 0:
            phone_number_digits = int(phone_number_digits)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    generator.generate_vcard(count, country_code, phone_number_digits)
    print(f'vCards written to {os.path.abspath(f"contacts-{count}.vcf")}')