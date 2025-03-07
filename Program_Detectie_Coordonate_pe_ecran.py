import pyautogui
import time
from PIL import ImageGrab  # Pentru a obține culoarea pixelului de la coordonatele mouse-ului

# Culoarea țintă, pe care o poți modifica în funcție de ceea ce cauți
target_color = (255, 255, 255)  # culoarea albă

# Afișează coordonatele și culoarea pixelului sub cursor în timp real
try:
    while True:
        x, y = pyautogui.position()  # Obține coordonatele cursorului
        # Obține culoarea pixelului la coordonatele (x, y)
        screenshot = ImageGrab.grab()  # Capturează ecranul
        color = screenshot.getpixel((x, y))  # Obține culoarea pixelului de la poziția (x, y)
        
        print(f"Poziția curentă a mouse-ului: X={x}, Y={y}, Culoare={color}")
        
        # Verifică dacă culoarea la poziția cursorului este culoarea țintă
        if color == target_color:
            print("Culoarea țintă a fost detectată!")
        
        time.sleep(1)  # Updatează la fiecare secundă
except KeyboardInterrupt:
    print("Ieșire din program.")
