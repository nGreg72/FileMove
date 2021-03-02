from watchdog.observers import Observer
import os
import time

from watchdog.events import FileSystemEventHandler

print("Перемещение файлов в разные поддиректории по типам!\n Видео хуярят в папку Videos\n фотки в Photos\n музончик в Music")

# Создаём класс наследник. Через него может отслеживаться изменения в папках.4
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # Перебираем все файлы в папке
        for filename in os.listdir(folder_track):
            # Проверяем расширение файла
            extension = filename.split(".")
            print(extension)

            # Если это фото
            if len(extension) > 0 and extension[-1].lower() == "jpg" or extension[-1].lower() == "png":
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Photos/" + filename
                os.rename(file, new_path)

            # Если это видео
            elif len(extension) > 0 and extension[-1].lower() == "mpg" or extension[-1].lower() == "mp4":
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Videos/" + filename
                os.rename(file, new_path)

            # Если это музыка
            elif len(extension) > 0 and extension[-1].lower() == "mp3":
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Music/" + filename
                os.rename(file, new_path)


folder_track = 'e:/Downloads/'
folder_dest = 'e:/Downloads/'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while (True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

