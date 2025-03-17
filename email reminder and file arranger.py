import os
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Function to organize files in a directory
def organize_files(directory):
    # Define file types and their corresponding folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Music": [".mp3", ".wav"],
        "Others": []  # For files that don't match any category
    }

    # Create folders if they don't exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder_name, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))

    print("File organization completed!")

# Function to send email reminders
def send_email_reminder(subject, body, to_email, from_email, password):
    # Set up the email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Use Gmail's SMTP server
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email reminder sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to run the tasks
def main():
    # Task 1: Organize files in a directory
    directory_to_organize = r"C:\Users\YourUsername\Downloads"  # Replace with your directory path
    organize_files(directory_to_organize)

    # Task 2: Send an email reminder
    email_subject = "Reminder: Complete Your Task"
    email_body = "This is a reminder to complete your pending tasks. Don't forget!"
    recipient_email = "recipient@example.com"  # Replace with recipient's email
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    send_email_reminder(email_subject, email_body, recipient_email, sender_email, sender_password)

if __name__ == "__main__":
    main()