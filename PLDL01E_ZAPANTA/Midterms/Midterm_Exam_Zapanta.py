# Service Information class
class ServiceInfo:
    def __init__(self):
        # Gather data directly from the user
        self.contract_account_no = input("ENTER CONTRACT ACCOUNT No.:")
        self.account_name = input("ENTER ACCOUNT NAME:")
        self.service_address = input("ENTER SERVICE ADDRESS:")
        self.tin = input(" ENTER TIN:")
        self.rate_class = input("ENTER RATE CLASS:")
        self.business_area = input("ENTER BUSINESS AREA:")

    def display(self):
        print("-" * 80)
        print("t\t\t\t\t\t\t\t\t\t\tMaynilad Water Services, INC.")
        print("\t\t\t\t\t\t\t\t\t\t8390 DR A SANTOS AVE BF HOMES")
        print("\t\t\t\t\t\t\t\t\t\tPARANAQUE CITY.")
        print("\t\t\t\t\t\t\t\t\t\tVAT Reg TIN: 005-393-442-0000")
        print("-" * 80)
        print("\t\t\t\t\t\tSERVICE INFORMATION\t\t\t\t\t\t")
        print(f" Contract Account No: {self.contract_account_no}")
        print(f" Account Name: {self.account_name}")
        print(f" Service Address: {self.service_address}")
        print(f" TIN: {self.tin}")
        print(f" Rate Class: {self.rate_class}")
        print(f" Business Area: {self.business_area}")
        print("-" * 80)


# Billing Summary & Metering Information class
class BillingSummary:
    def __init__(self):
        # Gather data directly from the user
        self.meter_no = input("ENTER METER NO.:")
        self.mru_no = input("ENTER MRU NO.:")
        self.seq_no = input("ENTER SEQ NO.:")
        self.reading_rate = input("ENTER READING RATE:")
        self.present_reading = float(input("ENTER PRESENT READING:"))
        self.previous_reading = float(input("ENTER PREVIOUS READING:"))
        self.consumption = self.present_reading - self.previous_reading
        # Consumption calculation
        self.billing_period = input("ENTER BILLING PERIOD:")
        self.current_charges = float(input("ENTER CURRENT CHARGES:"))
        self.basic_charge = 0.0
        # Placeholder to be calculated
        self.environment_charge = 0.0
        # Placeholder to be calculated
        self.maintenance_charge = float(input("ENTER MAINTENANCE CHARGE:"))
        self.total_current = 0.0
        # Placeholder to be calculated
        self.government_tax = 0.0
        # Placeholder to be calculated
        self.total_amount_due = 0.0
        # Placeholder to be calculated
        self.payment_due = float(input("ENTER PAYMENT DUE:"))

    def display(self):
        print(f"\t\t\t\t\t\tMETERING INFORMATION\t\t\t\t")
        print(f" Meter No: {self.meter_no}")
        print(f" MRU No: {self.mru_no}")
        print(f" Seq No: {self.seq_no}")
        print(f" Reading Rate: {self.reading_rate}")
        print(f" Present Reading: {self.present_reading}")
        print(f" Previous Reading: {self.previous_reading}")
        print(f" Consumption (cu.m): {self.consumption}")
        print("-" * 80)
        print(f"\t\t\t\t BILL & PAYMENT HISTORY\t\t\t\t")
        print(f"Desc\t\t\t\tTotal Amount\t\t\t\t\tOR#\t\t\t\t\tDATE")
        print("Description: WB-Water Bill, GD-Guarantee Deposit, MISC-Reopening Fee, Connection Fee, Metering Charge")
        print("-" * 80)

    def billing_summary(self):
        # Calculating charges
        self.basic_charge = self.consumption * 23.52
        self.environment_charge = self.basic_charge * 0.20
        self.total_current = self.basic_charge + self.environment_charge + self.maintenance_charge
        self.government_tax = self.total_current * 0.025
        self.total_amount_due = self.total_current + self.government_tax

        # Display billing summary
        print("\t\t\t\t\t\tBILLING SUMMARY\t\t\t\t")
        print(f" Basic Charge: {self.basic_charge:.2f}")
        print(f" Environmental Charge: {self.environment_charge:.2f}")
        print(f" Maintenance Charge: {self.maintenance_charge:.2f}")
        print(f" Total Current Charges: {self.total_current:.2f}")
        print(f" Government Tax (2.5%): {self.government_tax:.2f}")
        print(f" Total Amount Due: {self.total_amount_due:.2f}")
        print("-" * 80)