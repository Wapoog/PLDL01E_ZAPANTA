# display_data.py

from Midterms_quiz_prototype import gather_data

def display_data():
    customer, service, billing, electricity_bill = gather_data()

    # Print thank-you message before displaying information
    print("\nThank you for paying!")
    print("=" * 60)

    # Display all the gathered information
    customer.display()
    service.display()
    billing.display()
    electricity_bill.display()

if __name__ == "__main__":
    display_data()