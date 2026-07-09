def total_revenue(df):
    return df["Amount"].sum()


def paid_revenue(df):
    return df[df["Status"] == "Paid"]["Amount"].sum()


def unpaid_revenue(df):
    return df[df["Status"] == "Unpaid"]["Amount"].sum()


def pending_revenue(df):
    return df[df["Status"] == "Pending"]["Amount"].sum()


def invoice_count(df):
    return len(df)


def paid_invoice_count(df):
    return len(df[df["Status"] == "Paid"])


def unpaid_invoice_count(df):
    return len(df[df["Status"] == "Unpaid"])


def pending_invoice_count(df):
    return len(df[df["Status"] == "Pending"])