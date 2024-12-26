class Customerinfo:
    # Inititalization of values
    def __init__(self):
        self.customer_name = input("Enter customer name: ")
        self.contract_account_no = input("Enter contract account number: ")
        self.service_address = input("Enter service address: ")
        self.tin_number = input("Enter customer TIN number: ")
        self.rate_class = input("Enter rate class (residential or commercial: ")
        self.business_area = input("Enter the business area: ")

class Billing:
    # Initialization of values for class billing
    def __init__(self):
        self.meter_num = input("Enter meter no.: ")
        self.mru_num = input("Enter MRU no.: ")
        self.seq_num = input("Enter Seq no.: ")
        self.reading_date = input("Enter reading date (m/d/y): ")
        self.consumption = float(input("Enter the consumption (cu.m): "))
        self.present_reading = self.consumption
        self.previous_reading = input("Enter the previous reading: ")
        self.consumption_period = input("Enter previous consumption period in months: ")
        self.billing_period_start = input("Enter the start of reading period (m/d/y): ")
        self.due_date = input("Enter the due date of the bill: ")
        self.billing_period_end = self.reading_date
        self.basic_charge = 0.00
        self.environmental_charges = 0.00
        self.total_charges_bef_tax = 0.00
        self.government_taxes = 0.00
        self.total_amount_due = 0.00
        self.maintence_service_charge = 1.53

    def billing_summary(self):
        # Computation of values
        self.basic_charge = self.consumption * 23.52
        self.environmental_charges = self.basic_charge * 0.20
        self.total_charges_bef_tax = self.basic_charge + self.environmental_charges + self.maintence_service_charge
        self.government_taxes = self.total_charges_bef_tax * 0.025
        self.total_amount_due = self.total_charges_bef_tax + self.government_taxes




