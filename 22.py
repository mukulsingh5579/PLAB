#High-Speed Pattern Matching (Structural Pattern Matching)
def handle_command(command):
    match command.split():
        case ["quit"]:
            print("Shutting down...")
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["move", ("up" | "down" | "left" | "right") as direction, steps]:
            print(f"Moving {direction} by {steps} units.")
        case _:
            print("Command not recognized.")

handle_command("move left 10")