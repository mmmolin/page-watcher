import watcher
import notifier

if watcher.check_for_changes():
    print('something has happened')
    notifier.send_mail('Page changed', 'The web page has been updated')
else:
    print('no changes')
