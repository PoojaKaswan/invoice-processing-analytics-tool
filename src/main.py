from utils import load_data
from analytics import (
    total_revenue,
    paid_revenue,
    unpaid_revenue,
    pending_revenue,
    invoice_count,
    paid_invoice_count,
    unpaid_invoice_count,
    pending_invoice_count,
)


def main():
    df = load_data("../Data/invoices.csv")

    print("===== Invoice Analytics =====")
    print(f"Total Revenue      : ₹{total_revenue(df):,}")
    print(f"Paid Revenue       : ₹{paid_revenue(df):,}")
    print(f"Unpaid Revenue     : ₹{unpaid_revenue(df):,}")
    print(f"Pending Revenue    : ₹{pending_revenue(df):,}")
    print()

    print(f"Total Invoices     : {invoice_count(df)}")
    print(f"Paid Invoices      : {paid_invoice_count(df)}")
    print(f"Unpaid Invoices    : {unpaid_invoice_count(df)}")
    print(f"Pending Invoices   : {pending_invoice_count(df)}")


if __name__ == "__main__":
    main()