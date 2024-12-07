# Customer information class
class CustomerData:
    def __init__(self, name, street, barangay, city):
        self.name = name
        self.street = street
        self.barangay = barangay
        self.city = city

    def display(self):
        print("Customer Information:")
        print("-" * 60)
        print(f"  Name: {self.name}")
        print(f"  Street: {self.street}")
        print(f"  Barangay: {self.barangay}")
        print(f"  City: {self.city}")
        print("-" * 60)

# Service information class
class ServiceInfo:
    def __init__(self, service_id, rate, contract_name, service_address):
        self.service_id = service_id
        self.rate = rate
        self.contract_name = contract_name
        self.service_address = service_address

    def display(self):
        print("Service Information:")
        print("-" * 60)
        print(f"  Service ID: {self.service_id}")
        print(f"  Rate: {self.rate}")
        print(f"  Contract in the Name of: {self.contract_name}")
        print(f"  Service Address: {self.service_address}")
        print("-" * 60)

# Billing information class
class BillingInfo:
    def __init__(self, customer_type, bill_date, meter_reading_date, bill_period, due_date, total_kwh, total_amount):
        self.customer_type = customer_type
        self.bill_date = bill_date
        self.meter_reading_date = meter_reading_date
        self.bill_period = bill_period
        self.due_date = due_date
        self.total_kwh = total_kwh
        self.total_amount = total_amount

    def display(self):
        print("Billing Information:")
        print("-" * 60)
        print(f"  Customer Type: {self.customer_type}")
        print(f"  Bill Date: {self.bill_date}")
        print(f"  Meter Reading Date: {self.meter_reading_date}")
        print(f"  Bill Period: {self.bill_period}")
        print(f"  Due Date: {self.due_date}")
        print(f"  Total kWh Used: {self.total_kwh}")
        print(f"  Total Current Amount: PHP {self.total_amount}")
        print("-" * 60)

# Electricity bill calculation class
class ElectricityBill:
    def __init__(self, previous_balance, generation, transmission, system_loss, distribution, subsidies, taxes, universal, fit_all, installment=0):
        self.previous_balance = previous_balance
        self.generation = generation
        self.transmission = transmission
        self.system_loss = system_loss
        self.distribution = distribution
        self.subsidies = subsidies
        self.taxes = taxes
        self.universal = universal
        self.fit_all = fit_all
        self.installment = installment

    def compute_total_due(self):
        total_charges = (self.generation + self.transmission + self.system_loss +
                         self.distribution + self.subsidies + self.taxes +
                         self.universal + self.fit_all)
        return self.previous_balance + total_charges + self.installment

    def display(self):
        print("Electricity Bill Charges:")
        print("-" * 60)
        print(f"  Previous Balance: PHP {self.previous_balance}")
        print(f"  Generation Charge: PHP {self.generation}")
        print(f"  Transmission Charge: PHP {self.transmission}")
        print(f"  System Loss Charge: PHP {self.system_loss}")
        print(f"  Distribution Charge: PHP {self.distribution}")
        print(f"  Subsidies: PHP {self.subsidies}")
        print(f"  Government Taxes: PHP {self.taxes}")
        print(f"  Universal Charges: PHP {self.universal}")
        print(f"  FIT-All (Renewable) Charge: PHP {self.fit_all}")
        print(f"  Installment Due: PHP {self.installment}")
        print(f"\nTotal Amount Due: PHP {self.compute_total_due():.2f}")
        print("-" * 60)

def gather_data():
    # Input for customer information
    name = input("Enter customer name: ")
    street = input("Enter customer street: ")
    barangay = input("Enter customer barangay: ")
    city = input("Enter customer city: ")
    customer = CustomerData(name, street, barangay, city)

    # Input for service information
    service_id = input("Enter service ID: ")
    rate = input("Enter rate (e.g., Residential): ")
    contract_name = input("Enter contract in the name of: ")
    service_address = input("Enter service address: ")
    service = ServiceInfo(service_id, rate, contract_name, service_address)

    # Input for billing information
    customer_type = input("Enter customer type: ")
    bill_date = input("Enter bill date: ")
    meter_reading_date = input("Enter meter reading date: ")
    bill_period = input("Enter bill period: ")
    due_date = input("Enter due date: ")
    total_kwh = float(input("Enter total kWh used: "))
    total_amount = float(input("Enter total current amount: "))
    billing = BillingInfo(customer_type, bill_date, meter_reading_date, bill_period, due_date, total_kwh, total_amount)

    # Input for electricity bill computation
    previous_balance = float(input("Enter previous balance: "))
    generation = float(input("Enter generation charge: "))
    transmission = float(input("Enter transmission charge: "))
    system_loss = float(input("Enter system loss charge: "))
    distribution = float(input("Enter distribution charge: "))
    subsidies = float(input("Enter subsidies: "))
    taxes = float(input("Enter government taxes: "))
    universal = float(input("Enter universal charges: "))
    fit_all = float(input("Enter FIT-All (Renewable) charge: "))
    installment = float(input("Enter installment due (if any): "))
    electricity_bill = ElectricityBill(previous_balance, generation, transmission, system_loss, distribution, subsidies, taxes, universal, fit_all, installment)

    return customer, service, billing, electricity_bill
