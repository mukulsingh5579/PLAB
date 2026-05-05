#Instant Modern Web UI with Reflex
import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

def index():
    return rx.vstack(
        rx.heading(f"Count: {State.count}"),
        rx.button("Increment", on_click=State.increment),
    )

app = rx.App()
app.add_page(index)