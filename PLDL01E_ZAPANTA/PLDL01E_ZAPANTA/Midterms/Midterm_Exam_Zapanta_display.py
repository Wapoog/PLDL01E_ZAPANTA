#Import data from another file

from Midterm_Exam_Zapanta import ServiceInfo, BillingSummary

def main():


    # Collect service information
    service_info = ServiceInfo()
    service_info.display()

    # Collect billing and metering information
    billing_summary = BillingSummary()
    billing_summary.display()  # Display metering and billing information

    # Calculate and display billing summary
    billing_summary.billing_summary()


if __name__ == "__main__":
    main()
