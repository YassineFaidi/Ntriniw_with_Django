from .models import Notification

def create_notification(recipient, sender, notification_type, post=None, message_preview=None):
    Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        post=post,
        message_preview=message_preview
    )
