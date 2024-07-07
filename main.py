import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import tkinter as tk
from tkinter import messagebox

# import ping_hosts
# import install_apache
# import run_additional_playbook
# import update_packages

from config import set_environment
set_environment()

def send_email(subject, body):
    sender_email = os.getenv("SENDER_MAIL")
    receiver_email = os.getenv("SENDER_MAIL")
    password = os.getenv("MAIL_PASS")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def store_data(filename, data):
    with open(filename, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {data}\n")

def send_report():
    filename = "report.txt"
    try:
        with open(filename, 'r') as file:
            data = file.read()
            send_email("Report", data)
        print("Report sent successfully.")
    except Exception as e:
        print(f"Failed to send report: {e}")

def ping_hosts_function():
    result = ping_hosts.ping_hosts()
    store_data("report.txt", result)
    messagebox.showinfo("Result", result)

def install_apache_function():
    result = install_apache.install_apache()
    store_data("report.txt", result)
    messagebox.showinfo("Result", result)

def run_python_playbook_function():
    result = run_additional_playbook.run_additional_playbook()
    store_data("report.txt", result)
    messagebox.showinfo("Result", result)

def update_packages_function():
    result = update_packages.update_packages()
    store_data("report.txt", result)
    messagebox.showinfo("Result", result)

def send_report_function():
    send_report()

def create_main_window():
    root = tk.Tk()
    root.title("Automation Tool")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Choose a function to run:").pack(pady=5)

    tk.Button(frame, text="Ping Hosts", command=ping_hosts_function, width=25).pack(pady=5)
    tk.Button(frame, text="Install Apache", command=install_apache_function, width=25).pack(pady=5)
    tk.Button(frame, text="Run Python Playbook", command=run_python_playbook_function, width=25).pack(pady=5)
    tk.Button(frame, text="Update Packages", command=update_packages_function, width=25).pack(pady=5)
    tk.Button(frame, text="Send Report", command=send_report_function, width=25).pack(pady=5)
    tk.Button(frame, text="Exit", command=root.quit, width=25).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
