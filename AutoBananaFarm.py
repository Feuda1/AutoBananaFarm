import pyautogui
import time
import subprocess
import win32gui
import win32con

def open_steam_app(app_name):
    subprocess.Popen(['C:/Program Files (x86)/Steam/Steam.exe', '-applaunch', app_name])    # Измените путь к стиму

def minimize_steam_window():
    hwnd = win32gui.FindWindow(None, 'Banana')
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def close_steam_app(app_name):
    subprocess.Popen(['taskkill', '/F', '/IM', app_name])

while True:
    open_steam_app('2923300')
    time.sleep(2)
    minimize_steam_window()
    
    timer_duration = 60
    print(f'Таймер установлен на {timer_duration} секунд')
    
    start_time = time.time()
    while (time.time() - start_time) < timer_duration:
        remaining_time = int(timer_duration - (time.time() - start_time))
        print(f'Осталось времени: {remaining_time} секунд', end='\r')
        time.sleep(1)
    print('\nТаймер завершился')
    
    close_steam_app('Banana.exe')
    
    timer_duration = 3 * 60 * 60
    print(f'Таймер установлен на {timer_duration//3600} часов')
    
    start_time = time.time()
    while (time.time() - start_time) < timer_duration:
        remaining_time = int(timer_duration - (time.time() - start_time))
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        seconds = remaining_time % 60
        print(f'Осталось времени: {hours} часов {minutes} минут {seconds} секунд', end='\r')
        time.sleep(1)
    print('\nТаймер завершился')