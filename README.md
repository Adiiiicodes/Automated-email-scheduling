# Email Automation System - The Ultimate Email Scheduler!

Welcome to the Email Automation System! 🎉 Ever wished you could just send out tons of emails without lifting a finger? Well, we’ve got you covered—kind of. This ambitious project aims to make your email life easier by scheduling emails to various recipients at various times.

## The Dream

We envisioned a sleek, GUI-based Desktop app that would take your email scheduling to the next level. You know, the kind of app where you just set it and forget it, while sipping your coffee. ☕️

## The Reality

The app is a work in progress, and here’s what’s currently on the plate:

- **Current Status**: 
  - The app can schedule emails, but it’s not exactly a smooth operator yet. After sending emails, it tends to hang around like that one guest who just doesn’t take the hint to leave. 🕵️‍♂️
  - Once you close the app, it’s like it’s on vacation—emails won’t be sent, and any scheduled tasks reset to null. Who knew email scheduling could be so rebellious? 🚪🚫

## The Best Tool for Cold Mailing

Looking to up your cold mailing game? Look no further! This tool is designed for cold mailing with the power to schedule emails to multiple recipients at different times. It’s your new best friend for sending out those outreach emails like a pro. 🥂📧

## Important Note on Passkey

When entering the password for the sender's email, **please use an "App Password"** instead of your regular Gmail password. This is a special password generated specifically for applications and services that need access to your Gmail account. You can generate an App Password in your Google Account settings under "Security" -> "App passwords."

## Dependencies

To get this app up and running, you'll need the following Python packages:

- `tkinter` (for the GUI)
- `pywin32` (for Windows service management)
- `schedule` (for scheduling tasks)
- `smtplib` (for sending emails)
- `email` (for crafting email messages)

You can install the required packages using pip:

```bash
pip install pywin32 schedule
```

Note: `tkinter` and `smtplib` are included with Python, so you don't need to install them separately.

## Installation and Running

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/email-automation-system.git
   cd email-automation-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install pywin32 schedule
   ```

3. **Set Up the Windows Service**:
   Open Command Prompt as Administrator and run:
   ```bash
   python email_scheduler.py install
   ```

4. **Start the Service**:
   ```bash
   python email_scheduler.py start
   ```

5. **Use the GUI**:
   Run the GUI script:
   ```bash
   python gui_email_scheduler.py
   ```

6. **Uninstall the Service** (if needed):
   ```bash
   python email_scheduler.py remove
   ```

## Screenshots

![{87DC1C6E-6DA5-49E5-8DAC-C456D0640077}](https://github.com/user-attachments/assets/027cbf48-79b8-4829-a2f6-5f3f103c9d0e)
![Screenshot 2024-09-17 142043](https://github.com/user-attachments/assets/31be6f57-4bad-415c-9f75-f5f2a74a639d)
![Screenshot 2024-09-17 142100](https://github.com/user-attachments/assets/5226f56b-610f-46c1-8562-4aab851b894c)
![Screenshot 2024-09-17 142108](https://github.com/user-attachments/assets/8b4d3641-712f-44c2-a610-d95a1099ae24)

*Look at that beauty—ignore the bugs, focus on the style!*

## How to Contribute

If you’ve got a knack for fixing bugs or just want to help make this app less of a digital hot mess, feel free to fork this repo and add your magic! ✨ Here’s how you can jump in:

1. **Fork the Repo**: Show us your love by making a copy!
2. **Fix Bugs**: Patch up those pesky issues.
3. **Add Features**: Got a brilliant idea? Implement it!
4. **Submit a Pull Request**: We’d love to see what you’ve been working on.

## Known Bugs

- **Program Hangs**: The app might decide to stay around for an indefinite coffee break.
- **App Closure**: Closing the app might result in emails taking an unscheduled vacation.

## License

Feel free to use, modify, and share this code. Just remember, with great power comes great responsibility! 🦸‍♂️

---

Thanks for checking out our project. Happy emailing! 🚀

