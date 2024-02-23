import cv2
import os
import shutil

def extract_frames(video_folder, image_folder):
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    for video_file in os.listdir(video_folder):
        if video_file.endswith(('.mp4', '.avi')):
            video_path = os.path.join(video_folder, video_file)
            cap = cv2.VideoCapture(video_path)
            
            video_name = os.path.splitext(video_file)[0]
            video_image_folder = os.path.join(image_folder, video_name)
            if not os.path.exists(video_image_folder):
                os.makedirs(video_image_folder)

            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                if frame_count % 20 == 0:
                    frame_path = os.path.join(video_image_folder, f"{video_name}_frame_{frame_count:05d}.jpg")  # Formatira brojač sa vodećim nulama
                    cv2.imwrite(frame_path, frame)
                
                frame_count += 1
            
            cap.release()
            distribute_frames_into_parts(video_image_folder)

def distribute_frames_into_parts(video_image_folder):
    frames = [f for f in os.listdir(video_image_folder) if f.endswith('.jpg')]
    frames.sort()  # Sortira frejmove po imenima kako bi osigurali redosled
    total_frames = len(frames)
    part_size = total_frames // 3

    for part in range(1, 4):
        part_folder = os.path.join(video_image_folder, f'part_{part}')
        if not os.path.exists(part_folder):
            os.makedirs(part_folder)

        start_index = (part - 1) * part_size
        end_index = start_index + part_size if part < 3 else total_frames  # Osigurava da poslednji podfolder sadrži sve preostale frejmove

        for frame in frames[start_index:end_index]:
            original_frame_path = os.path.join(video_image_folder, frame)
            new_frame_path = os.path.join(part_folder, frame)
            shutil.move(original_frame_path, new_frame_path)

# Primer upotrebe
video_folder = './videos'
image_folder = './images'
extract_frames(video_folder, image_folder)
