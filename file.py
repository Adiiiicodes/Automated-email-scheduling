import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time
import schedule
import tkinter as tk
from tkinter import messagebox

# Function to send email
def send_email(sender_email, sender_password, subject, body, recipients):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        print(f"Email sent to: {', '.join(recipients)}")
    except Exception as e:
        print(f"Error: {e}")

# Function to schedule emails
def schedule_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END).strip()
    recipients = recipients_entry.get().split(",")
    send_times = send_times_entry.get().split(",")

    def task():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        if current_time in send_times:
            print(f"Attempting to send email at {current_time}.")
            send_email(sender_email, sender_password, subject, body, recipients)
            send_times.remove(current_time)
            if not send_times:
                messagebox.showinfo("Info", "All emails have been sent.")
                root.quit()

    schedule.every(1).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

# GUI Setup
root = tk.Tk()
root.title("Email Scheduler")

tk.Label(root, text="Sender's Email:").grid(row=0, column=0, padx=10, pady=5)
sender_email_entry = tk.Entry(root, width=50)
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sender's Password:").grid(row=1, column=0, padx=10, pady=5)
sender_password_entry = tk.Entry(root, width=50, show='*')  # 'show' hides the password
sender_password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=2, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Body:").grid(row=3, column=0, padx=10, pady=5)
body_entry = tk.Text(root, width=50, height=10)
body_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Recipients (comma-separated):").grid(row=4, column=0, padx=10, pady=5)
recipients_entry = tk.Entry(root, width=50)
recipients_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Send Times (comma-separated YYYY-MM-DD HH:MM):").grid(row=5, column=0, padx=10, pady=5)
send_times_entry = tk.Entry(root, width=50)
send_times_entry.grid(row=5, column=1, padx=10, pady=5)

schedule_button = tk.Button(root, text="Schedule Email", command=schedule_email)
schedule_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
