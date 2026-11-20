from pyscript import document,display

# New Club members list
members = ["ethan apelo"]

def check_member(event=None):
    Fname = document.getElementById("Fname").value.strip()
    Lname = document.getElementById("Lname").value.strip()
    full_name = f"{Fname} {Lname}"

    # Dictionary mapping names to messages (no conditionals/loops)
    messages = {
        **{name: f"Congratulations {name}! You are now part of the ICT club." for name in members}
    }

    display(members, target="output1")
