import watcher
import notifier

try:
    has_changed =watcher.check_for_changes()
except Exception as e:
    print(f'Error checking web page for changes: {e}')
    exit(1)

if has_changed:
    try:
        notifier.send_mail('Page changed', 'The web page has been updated')
    except Exception as e:
        print(f'Error sending notification: {e}')
        exit(1)
