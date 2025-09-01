import watcher
import notifier

if watcher.check_for_changes():
    try:
        notifier.send_mail('Page changed', 'The web page has been updated')
    except Exception as e:
        print('Error sending notification: {e}')
else:
    print('no changes')
