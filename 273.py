#Structural Pattern Matching (match-case)
def handle_status(status_code):
    match status_code:
        case 200:
            return "Success!"
        case 404:
            return "Not Found."
        case 500 | 501 | 502: # Multiple cases in one
            return "Server Error."
        case _:
            return "Unknown status."

print(handle_status(404))