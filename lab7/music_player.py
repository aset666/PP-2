import pygame
import os

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Экран и настройки
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

# Папка с музыкой
music_folder = "."
playlist = [file for file in os.listdir(music_folder) if file.endswith((".mp3", ".wav"))]
playlist.sort()

# Проверим, что список не пуст
if not playlist:
    print("Нет музыкальных файлов в папке!")
    pygame.quit()
    exit()

current_track = 0
is_paused = False

# Функция для воспроизведения трека
def play_track(index):
    global is_paused
    track = playlist[index]
    print(f"Now Playing: {track}")
    pygame.mixer.music.load(os.path.join(music_folder, track))
    pygame.mixer.music.play()
    is_paused = False

play_track(current_track)

# Главный цикл
running = True
while running:
    screen.fill((30, 30, 30))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause/Unpause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_paused = True
                    print("Paused")
                elif is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                    print("Unpaused")
                else:
                    play_track(current_track)

            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                is_paused = False
                print("Stopped")

            elif event.key == pygame.K_n:  # Next Track
                current_track = (current_track + 1) % len(playlist)
                play_track(current_track)

            elif event.key == pygame.K_b:  # Previous Track
                current_track = (current_track - 1) % len(playlist)
                play_track(current_track)

# Завершаем работу Pygame
pygame.quit()

