# Page Watcher

A Python script that monitors a web page and sends an email if the content changes.

## Quick Start

1. **Install dependencies**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure**
   - Edit `config.yaml` with your URL and email settings.
   - Set the `EMAIL_PASSWORD` environment variable to your app password.

3. **Run**
   ```bash
   python main.py
   ```

## Tips

- Add `state.json` to `.gitignore`.
- Use a separate Gmail account and app password for sending emails.