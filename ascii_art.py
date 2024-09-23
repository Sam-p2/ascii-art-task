import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    name = "Samuel"  # Replace with your first name
    print(generate_ascii_art(name))
