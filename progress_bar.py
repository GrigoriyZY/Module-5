# Progress bar for project

import time

playback_time = 0
duration = 25
width = 50
percent = 0
while playback_time <= duration:
    percent = int(playback_time / duration * 100)
    left_side = width * percent // 100
    right_side = width - left_side
    print('\r[', '▓' * left_side, '-' * right_side, ']',
          f'Воспроизведение: ', playback_time // 60, ':', playback_time % 60, ' из ', duration // 60, ':', duration % 60,
          f' - {percent}%', sep='', end='')
    time.sleep(0.1)
    playback_time += 1
    if percent == 100:
        print('\nВоспроизведение завершено.')
