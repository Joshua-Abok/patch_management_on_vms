import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import tkinter as tk 
from tkinter import messagebox

from config import set_environment
set_environment()


def send_email(subject, body): 
    sender_email =  os.getenv("SENDER_MAIL")           
    receiver_email =  os.getenv("SENDER_MAIL")              
    password =  os.getenv("MAIL_PASS")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try: 
        # with smtplib.SMTP('smtp.ethereal.email', 587) as server: 
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e: 
        print(f"Failed to send email: {e}")


# def store_data(filename, data):
#     with open(filename, 'a') as file:
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file.write(f"{timestamp}: {data}\n")

# def send_report():
#     filename = "report.txt"
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#             send_email("Report", data)
#         print("Report sent successfully.")
#     except Exception as e:
#         print(f"Failed to send report: {e}")

# def main():
#     while True:
#         print("\nChoose a function to run:")
#         print("1. Ping Hosts")
#         print("2. Install Apache")
#         print("3. Run Python Playbook")
#         print("4. Update Packages")
#         print("5. Send Report")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == '1':
#             result = ping_hosts.ping_hosts()
#             store_data("report.txt", result)
#         elif choice == '2':
#             result = install_apache.install_apache()
#             store_data("report.txt", result)
#         elif choice == '3':
#             result = run_additional_playbook.run_additional_playbook()
#             store_data("report.txt", result)
#         elif choice == '4':
#             result = update_packages.update_packages()
#             store_data("report.txt", result)
#         elif choice == '5':
#             send_report()
#         elif choice == '6':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 6.")

# if __name__ == "__main__":
#     main()

def on_send_email(): 
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    send_email(subject, body)


# create main window 
root = tk.Tk()
root.title("Email Sender")

# create and place the subject label and entry
tk.Label(root, text='Subject:').grid(row=0, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=0, column=1, padx=10, pady=5)

# create and place the body label and text box 
tk.Label(root, text="Body:").grid(row=1, column=0, padx=10, pady=5)
body_text = tk.Text(root, width=50, height=15)
body_text.grid(row=1, column=1, padx=10, pady=5)

# create and place the send email button 
send_button = tk.Button(root, text="Send Email", command=on_send_email)
send_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

# run main event loop 
root.mainloop()
