import speedtest
import tkinter as tk
from tkinter import messagebox

test = speedtest.Speedtest()
root = tk.Tk()
root.geometry("400x400")
root.title("Speed Test")
font = ("Verdana", 15, "bold")

def function():
    
    messagebox.showinfo("confirmation", '''
                    It may take some time 
    ''')

    downlod.configure(text = f"{str(test.download()//10**6)} Mbps")
    upload.configure(text = f"{str(test.upload()//10**6)} Mbps")
    
    results.configure(text = "Test is compleat")

download_speed = tk.Label(root, text = "Downoad Speed-", font = font)
download_speed.place(x = 10, y = 10)
downlod = tk.Label(root, text = "0 Mbps", font = font)
downlod.place(x = 250, y = 10)
upload_speed = tk.Label(root, text = "Upload Speed-", font = font)
upload_speed.place(x = 10, y = 50)
upload = tk.Label(root, text = "0 Mbps", font = font)
upload.place(x = 250, y = 50)

results = tk.Label(root, text = "click bello to start the test", font = (15))
results.place(x = 50, y = 250)

btn = tk.Button(root, text = "Test", command = function, font = font)
btn.place(x = 50, y = 300, height = 40, width = 300)

root.mainloop()