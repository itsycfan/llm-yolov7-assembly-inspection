# PS C:\Users\Tesisti> python -m venv hrcreading
# PS C:\Users\Tesisti> .\hrcreading\Scripts\activate
# (hrcreading) PS C:\Users\Tesisti> C:/Python310/python.exe c:/Users/Tesisti/AppData/Local/Temp/Reading_CaseStudy_3.py

# import os
# os.environ['OPENAI_API_KEY'] = 'set-your-key-in-shell-or-.env'  # do not hardcode

# sys.path.append(yolov7_path)
# print("sys.path:", sys.path) 
import cv2
import torch
import pyttsx3
from datetime import datetime
import numpy as np
import requests
from IPython.display import display, Audio
import openai
import time
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import pygame
import os
from GUI import AssemblyGUI
import tkinter as tk
from playsound import playsound
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
from PIL import Image, ImageTk
from playsound import playsound


# from ultralytics.yolo.utils.downloads import non_max_suppression, check_img_size, scale_coords
# from utils.general import non_max_suppression, check_img_size, scale_coords
# from utils.torch_utils import select_device



# ———————————————————————————————————————————————————————————— GUI design ————————————————————————————————————————————————————————————
def load_and_play(speech=None):
    try:
        playsound(speech)
    except Exception as e:
        print(f"Error playing {speech}: {e}")

def pause_audio():
    pygame.mixer.music.pause()

def set_volume(value):
    volume_level = float(value) / 100
    pygame.mixer.music.set_volume(volume_level)

def change_voice(selected_voice_type):
    voice_type = selected_voice_type
    load_and_play()

def create_gui():
    root.title("Assembly Monitoring System")
    root.geometry("1200x800")  # Adjust window size

    # Frames for different sections
    left_column = tk.Frame(self.root, width=800, bg='white')
    right_column = tk.Frame(self.root, width=400, bg='light gray')
    left_column.pack(side='left', fill='both', expand=True)
    right_column.pack(side='right', fill='both', expand=True)

    # Sub-frames within the left frame
    image_display_frame = tk.Frame(left_column, width=800)
    label_description_0 = tk.Label(image_display_frame, text="Multi-form Instructions", font=('Arial', 16, 'bold'))
    label_description_0.pack(pady=(20, 0))
    image_display_frame.pack(side="top", fill="both", expand=True)
    command_frame = tk.Frame(left_column, width=400)
    command_frame.pack(side="top", fill="both", expand=False)

    # Sub-frames for each image and its description
    left_image_frame = tk.Frame(image_display_frame, width=400)
    right_image_frame = tk.Frame(image_display_frame, width=400)
    left_image_frame.pack(side="left", fill="both", expand=True)
    right_image_frame.pack(side="right", fill="both", expand=True)

    # Labels and images in the left image frame
    label_description_1 = tk.Label(left_image_frame, text="Component", font=('Arial', 14))
    canvas_com = tk.Canvas(left_image_frame, bg="gray", height=80, width=80)
    label_operation_1 = tk.Label(left_image_frame, text="Operation", font=('Arial', 14))
    canvas_ope = tk.Canvas(left_image_frame, bg="gray", height=80, width=80)
    label_description_1.pack(pady=(20, 0))
    canvas_com.pack(pady=(5, 5), fill="both", expand=True)
    label_operation_1.pack(pady=(5, 0))
    canvas_ope.pack(pady=(5, 20), fill="both", expand=True)

    # Labels and images in the right image frame
    label_description_2 = tk.Label(right_image_frame, text="Tool", font=('Arial', 14))
    canvas_too = tk.Canvas(right_image_frame, bg="gray", height=80, width=80)
    label_operation_2 = tk.Label(right_image_frame, text="Assembly Result", font=('Arial', 14))
    canvas_res = tk.Canvas(right_image_frame, bg="gray", height=80, width=80)
    label_description_2.pack(pady=(20, 0))
    canvas_too.pack(pady=(5, 5), fill="both", expand=True)
    label_operation_2.pack(pady=(5, 0))
    canvas_res.pack(pady=(5, 20), fill="both", expand=True)

    # Text box for instructions
    text_frame = tk.Frame(left_column, width=400)
    text_frame.pack(side="top", fill="both", expand=False, pady=(0, 0))
    text_instruction = tk.Text(text_frame, height=10, width=80)
    text_instruction.pack(pady=(5, 5), padx=0)

    # Main command frame for holding all control elements
    command_frame = tk.Frame(left_column, bg='white')
    command_frame.pack(fill="x")

    # Controls frame for holding buttons and sliders horizontally
    controls_frame = tk.Frame(command_frame)
    controls_frame.pack(fill="x", expand=True)

    # Buttons and controls in the command frame
    play_button = tk.Button(controls_frame, text="Play Instructions", font=('Arial', 12), command=load_and_play(speech=None))
    pause_button = tk.Button(controls_frame, text="Pause Instructions", font=('Arial', 12), command=pause_audio())
    volume_control = tk.Scale(controls_frame, from_=0, to=100, orient="horizontal", label="Volume", font=('Arial', 12), command=set_volume)
    volume_control.set(50)  # Default volume set to 50%
    sound_type = ttk.Combobox(controls_frame, values=["Male", "Female"], font=('Arial', 12), state="readonly")
    sound_type.set("Male")  # Default sound type
    play_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    pause_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    volume_control.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
    sound_type.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    # Right column single image frame
    realtime_image_frame = tk.Frame(right_column, width=400, bg='light blue')
    realtime_image_frame.pack(side="top", fill="both", expand=True)
    label_description_3 = tk.Label(realtime_image_frame, text="Actual Statu", font=('Arial', 16, 'bold'), bg='light blue')
    label_description_3.pack(pady=(20, 0))

    # Image and label in the right column
    label_description_realtime = tk.Label(realtime_image_frame, text="Real-time Image", font=('Arial', 14), bg='light blue')
    realtime_canvas = tk.Canvas(realtime_image_frame, bg="gray", height=300, width=450)
    label_description_realtime.pack(pady=(20, 0))
    realtime_canvas.pack(pady=(5, 5), fill="none", expand=False)

    # Text box for assembly progress
    progress_frame = tk.Frame(right_column, width=400, bg='light blue')
    progress_frame.pack(side="top", fill="both", expand=False, pady=(0, 0))
    progress_label = tk.Label(progress_frame, text="Assembly Status", font=('Arial', 14), bg='light blue')
    progress_label.pack()
    progress_text = tk.Text(progress_frame, height=15, width=56)
    progress_text.pack(pady=(5, 20), padx=20)

    # Button frame at the bottom of right_column
    button_frame = tk.Frame(right_column, bg='light blue')
    button_frame.pack(side='bottom', fill='x', expand=False)
    exit_button = tk.Button(button_frame, text="Exit", font=('Arial', 12), command=root.destroy, width=10)
    error_button = tk.Button(button_frame, text="Report Error", font=('Arial', 12), command=lambda: messagebox.showerror("Error", "System Error Reported"), width=20)
    exit_button.pack(side="left", padx=35, pady=25)
    error_button.pack(side="right", padx=35, pady=25)




# ———————————————————————————————————————————————————————————— Data and model Setting ————————————————————————————————————————————————————————————
# YOLOv7
# loading the pre-trained YOLOv7 model
yolov7_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/yolov7'
weights_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/yolov7/best.pt'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.hub.load(yolov7_path, 'custom', weights_path, source='local').to(device)
model.eval() # 确保模型处于评估模式
yolov7_label_order = ['Allen key', 'Hex cap screw (big)', 'Drive shaft companion flange', 'Nuts', 'Pump housing', 'S12', 'S6', 'S9', 'Washers', 'Wrench size 13']
    
# Assembly data loading
assembly_tasks_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/assembly_tasks.xlsx'
assembly_tasks_df = pd.read_excel(assembly_tasks_path)
index_total = assembly_tasks_df.dropna(how='all').shape[0] - 1

steps_classes = assembly_tasks_df['step'].dropna().to_dict()
components_classes = assembly_tasks_df['components'].dropna().to_dict()
tools_classes = assembly_tasks_df['tools'].dropna().to_dict()
operations_classes = assembly_tasks_df['operations'].dropna().to_dict()
time_classes = assembly_tasks_df['time'].dropna().to_dict()
lastorder_classes = assembly_tasks_df['lastorder'].dropna().to_dict()
print(steps_classes)
print(components_classes)
print(tools_classes)

# Error information
error_templates_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/error_templates.xlsx'
error_templates_df = pd.read_excel(error_templates_path)
error_templates = dict(zip(error_templates_df['error_type'], error_templates_df['template']))
print(error_templates)



# ———————————————————————————————————————————————————————————— Image Capture and Process ————————————————————————————————————————————————————————————
# Image display 
def show_image(frame):
    try:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(frame_rgb)
        plt.axis('off')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        plt.title(f'Image_{timestamp}')
        plt.show()  # Ensure the image is displayed when the function is called
    except Exception as e:
        print(f"Failed to display image: {e}")

# Image preprocessing
def preprocess_image(frame):
    try:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, 0)
        img = torch.from_numpy(img).float()
        return img
    except Exception as e:
        print(f"Error during image preprocessing: {e}")
        return None

# Image preprocessing cancel
def postprocess_image(tensor):
    if isinstance(tensor, torch.Tensor):
        tensor = tensor.cpu()
        image_np = tensor.numpy()
        image_np = image_np[0]
        if image_np.shape[0] < image_np.shape[2]:
            image_np = image_np.transpose(1, 2, 0)
        if image_np.max() <= 1.0:
            image_np = (image_np * 255).astype(np.uint8)
        return image_np
    else:
        print("传入的数据不是 torch.Tensor 类型")
        return None

# Image capturing
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        # show_image(frame)
        img = preprocess_image(frame)
        return img
    else:
        return None


# ———————————————————————————————————————————————————————————— YOLOv7 Detection and classification ————————————————————————————————————————————————————————————
# Image YOLOv7 detection
def detect_items(image):
    frame = image.squeeze().numpy().transpose(1, 2, 0) * 255  # 转换图像为适合显示的格式
    frame = frame.astype(np.uint8)

    with torch.no_grad():
        predictions = model(image)  # 使用模型进行预测
        predictions = predictions[0] if isinstance(predictions, tuple) else predictions
        predictions = non_max_suppression(predictions, conf_thres=0.6, iou_thres=0.45)

    detected_items = []  # 初始化检测到的物体列表

    # 检查predictions是否存在且不为空
    if predictions is not None and len(predictions) > 0 and len(predictions[0]) > 0:
        detected_items = predictions[0]  # 提取检测到的物体
        print(f"YOLOv7 detections found: {len(detected_items)}")  # 打印检测到的物体数量
    else:
        print("No detections found.")

    return detected_items

# detected items classification
def classify_detections(detected):
    classified_items = {
        'components': [],
        'tools': [],
        'steps': []
    }
    for detection in detected:
        x1, y1, x2, y2, conf, cls = detection[:6]
        if conf > 0.5:
            label = yolov7_label_order[int(cls)]
            print('label:' + label)
            if any(label == step for step in steps_classes.values()):
                classified_items['steps'].append(label)
            if any(label in component for component in components_classes.values()):
                classified_items['components'].append(label)
            if any(label in tool for tool in tools_classes.values()):
                classified_items['tools'].append(label)
    return classified_items



# ———————————————————————————————————————————————————————————— Annotate by Error ————————————————————————————————————————————————————————————
# Error validation and handle
def error_validation(classified, step_details, operator_name, location, item_type, task):
    details = {
        'now': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'operator_name': operator_name,
        'location': location,
        'expected': step_details[item_type],
        'actual': classified[item_type],
        'step': step_details['step'],
        'task': task
    }
    
    error_result = {
        'type': item_type,
        'specific': details['actual'],
        'result': True
    }
    
    if set(details['actual']).issubset(set(details['expected'])):
        error_result['result'] = True
        error_log = None
    else:
        error_result['result'] = False
        error_log = error_templates[item_type].format(**details)  # Ensure error_templates is defined with proper templates.
        
    errorLog_dir = "C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/Results_ErrorLog"
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    errorLog_filename = f"{errorLog_dir}/text{current_time}.txt"
    with open(errorLog_filename, "w") as text_file:
        text_file.write(error_log)
    print(f"Error log saved.")
    
    return error_result, error_log

# Label with different colors according to different situation
def annotate_image_with_labels(image, detected_items, classified_items, item_type, error_result):
    # Define colors for different scenarios
    correct_color = (0, 255, 0)  # Green for "True"
    wrong_color = (255, 0, 0)    # Red for "False"
    neutral_color = (128, 128, 128)  # Gray for other categories

    # Process the image once
    processed_image = postprocess_image(image)

    for detection in detected_items:
        x1, y1, x2, y2, conf, cls = detection[:6]
        detection_label = yolov7_label_order[int(cls)]  # Convert class ID to readable label
        
        # Determine the color based on classification and result
        if detection_label in classified_items[item_type]:
            color = correct_color if error_result['result'] else wrong_color
        else:
            color = neutral_color
        
        # Draw rectangle and label on the same processed image
        cv2.rectangle(processed_image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(processed_image, detection_label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Save and optionally display the annotated image
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    annotated_image_path = f'./Results_Image/annotated_{item_type}_{timestamp}.jpg'
    cv2.imwrite(annotated_image_path, processed_image)
    print(f"Annotated image saved.")

    return processed_image



# ———————————————————————————————————————————————————————————— GPT promt and speech ————————————————————————————————————————————————————————————
# Load gpt prompt
def generate_prompt(step_details, error_description):
    gpt_prompt_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/gpt_prompt.xlsx'
    gpt_prompt_df = pd.read_excel(gpt_prompt_path)
    prompt_template = gpt_prompt_df['prompt'].iloc[0]
    prompt = prompt_template.format(step_details=step_details, error_description=error_description)
    return prompt

def GPT_TTS(prompt):
    # Check GPT API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key is not set. Please ensure the 'OPENAI_API_KEY' environment variable is defined.")
    
    # Step1: Text generation
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.choices[0].message.content.strip()
    # print("Generated text:", text)
    
    # Text result save
    results_text_dir = "C:/Users/Tesisti/Desktop/Yuchen 2023-2024/06 GPT+YOLOV7/Results_Text"
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    text_filename = f"{results_text_dir}/text{current_time}.txt"
    with open(text_filename, "w") as text_file:
        text_file.write(text)
    print(f"Results text saved.")

    # Step2: Speech generation
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "tts-1",
        "input": text,
        "voice": "alloy"
    }
    response = requests.post('https://api.openai.com/v1/audio/speech', headers=headers, json=data)
    if response.status_code == 200:
        results_speech_dir = "C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/Results_Speech"
        speech_filename = f"{results_speech_dir}/speech{current_time}.mp3"
        with open(speech_filename, 'wb') as file:
            file.write(response.content)
        print("Error instruction speech saved.")
        # display(Audio(speech_filename, autoplay=True))
    else:
        print("Failed to generate speech:", response.status_code, response.text)
    return speech_filename

# Text to speech
def text_to_speech(text):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    voice_path = f'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/TTS_Speech/voice_{timestamp}.mp3'
    try:
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')  # Obatain current speed
        engine.setProperty('rate', rate - 80)  # Modify speed
        volume = engine.getProperty('volume')  # Obatain current volume
        engine.setProperty('volume', volume + 0.25)  # Modify volume
        voices = engine.getProperty('voices')  # Obatain aviable voice
        engine.setProperty('voice', voices[0].id)  # Modify voice（0-male，1-female）
        engine.say(text)
        engine.save_to_file(text, voice_path)
        engine.runAndWait()
        return voice_path
    except Exception as e:
        print(f"Error with text-to-speech: {e}")
        return None
        # print(text)

def play_audio(filename):
    # pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



# ———————————————————————————————————————————————————————————— GUI Update ————————————————————————————————————————————————————————————
# 更新四大块图像的显示：canvas_com，canvas_ope，canvas_too，canvas_res
def update_gui_4image(gui, step):
    base_path = 'C:/Users/Tesisti/Desktop/Yuchen 2023-2026/06 GPT+YOLOV7/CS_CIRP2024/'

    # 构建每个图像的完整路径和对应的画布
    image_paths = {
        'component': f'{base_path}component/step{step}_com.png',
        'tool': f'{base_path}tool/step{step}_too.png',
        'operation': f'{base_path}operation/step{step}_ope.png',
        'result': f'{base_path}result/step{step}_res.png'
    }

    canvases = {
        'component': gui.canvas_com,
        'tool': gui.canvas_too,
        'operation': gui.canvas_ope,
        'result': gui.canvas_res
    }

    # 循环检查每个图像路径并更新相应的画布
    for key, path in image_paths.items():
        canvas = canvases[key]
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.LANCZOS) #Image.ANTIALIAS
            img = ImageTk.PhotoImage(img)
            canvas.image = img
            canvas.create_image(0, 0, anchor='nw', image=img)
        else:
            canvas.delete("all")



# ———————————————————————————————————————————————————————————— Main Function ————————————————————————————————————————————————————————————
# main
def main():
    GUI = AssemblyGUI()
    operator_name = input("Please enter the operator's name: ")
    location = "Assembly Line 3, Workstation 7"

    pygame.mixer.init()
    # GUI.create_gui()
    # update_gui()

    for index in range(index_total):
        # Obtain all the information for this step
        step_details = {
            'components': components_classes[index],
            'tools': tools_classes[index],
            'operations': operations_classes[index],
            'time': time_classes[index],
            'step': steps_classes[index],
            'steps': steps_classes[index]
        }
        GUI.progress_text.delete('1.0', tk.END) # 清空GUI的process框中的所有文字内容
        step_number = int(step_details['step'][1:])
        update_gui_4image(GUI, step_number) # 根据当下步骤更新GUI左上角的四张图
        # print(step_details)

        for item_type in ['components', 'tools', 'steps']:
            text = f"Start assembly step{index+1}.{item_type}."
            GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
            GUI.root.update_idletasks()
            if step_details[item_type] != "None":
                retry = True
                retry_count = 0
                while retry and retry_count < 3:
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    file_name = f"{item_type}_{timestamp}.mp4"
                    if item_type in ['components', 'tools']:
                        Task = f"Please prepare the following {item_type}: {step_details[item_type]}."
                        sleep_time = 6
                    else:
                        Task = f"Please follow the instructions to complete the step: {step_details['operations']}."
                        sleep_time = step_details['time']

                    GUI.text_instruction.delete('1.0', tk.END)
                    GUI.text_instruction.insert(tk.END, Task) # 更新GUI的instruction框中的文字内容
                    GUI.root.update_idletasks()
                    voice = text_to_speech(Task)
                    print(voice)
                    GUI.load_and_play(voice) # 更新GUI的播放button的command
                    GUI.root.update_idletasks()
                    # play_audio(voice)

                    time.sleep(sleep_time)

                    image = capture_image()
                    image_np = postprocess_image(image) # 把图像从tensor格式转换到numpy
                    image_pil = Image.fromarray(image_np)  # 把图像从numpy格式转换到pil
                    photo_image = ImageTk.PhotoImage(image_pil)
                    GUI.realtime_canvas.image = photo_image
                    GUI.realtime_canvas.create_image(0, 0, anchor='nw', image=photo_image) # 更新GUI的realtime image框中的图片
                    GUI.root.update_idletasks()
                    
                    detected_items = detect_items(image)
                    text = f"\nDetected: {detected_items}."
                    GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
                    GUI.root.update_idletasks()
                    # print(detected_items)
                    classified_items = classify_detections(detected_items)
                    # print(classified_items)
                    error_result, error_log = error_validation(classified_items, step_details, operator_name, location, item_type, Task)
                    # print(error_log)
                    text = f"\nError Log: {error_log}."
                    GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容

                    image = annotate_image_with_labels(image, detected_items, classified_items, item_type, error_result)
                    GUI.realtime_canvas.image = image
                    GUI.realtime_canvas.create_image(0, 0, anchor='nw', image=image) # 更新GUI的realtime image框中的图片

                    if error_result['result'] == False:
                        if retry_count < 2:
                            prompt = generate_prompt(step_details, error_log)
                            speech_filename = GPT_TTS(prompt)
                            play_audio(speech_filename)
                            text = f"\nRedo step{index+1}.{item_type}"
                            GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
                            retry_count += 1
                        else:
                            text = f"\nFailed to correct the error after 2 attempts."
                            GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
                            retry = False
                    else:
                        text = f"\nYou did it correctly. Now let's proceed to the next step."
                        voice = text_to_speech(text)
                        play_audio(voice)
                        GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
                        text = f"\nEnd step{index+1}.{item_type}"
                        GUI.progress_text.insert(tk.END, text) # 更新GUI的process框中的文字内容
                        retry = False

    GUI.run()

if __name__ == '__main__':
    main()
