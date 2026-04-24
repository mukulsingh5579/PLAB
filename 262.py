#Desktop Notification Sender
from plyer import notification

notification.notify(
    title="Python Alert",
    message="Your background task is officially complete! 🎉",
    app_name="Python Script",
    timeout=10  # Seconds the toast stays on screen
)