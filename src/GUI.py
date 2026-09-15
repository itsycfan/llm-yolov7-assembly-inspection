import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import os
from playsound import playsound

class AssemblyGUI:
    def __init__(self):
        pygame.mixer.init()
        self.voice_type = "0"
        self.root = tk.Tk()
        self.create_gui()


    def load_and_play(self, speech=None):
        try:
            playsound(speech)
        except Exception as e:
            print(f"Error playing {speech}: {e}")

    '''
    def load_and_play(self, speech=None):
        if speech and os.path.exists(speech):
            try:
                pygame.mixer.music.load(speech)
                pygame.mixer.music.play(loops=-1)
            except Exception as e:
                print(f"Error playing {speech}: {e}")
        else:
            print(f"Audio file not found: {speech}")
    '''

    def pause_audio(self):
        pygame.mixer.music.pause()

    def set_volume(self, value):
        volume_level = float(value) / 100
        pygame.mixer.music.set_volume(volume_level)

    def change_voice(self, selected_voice_type):
        self.voice_type = selected_voice_type
        self.load_and_play()

    def create_gui(self):
        self.root.title("Assembly Monitoring System")
        self.root.geometry("1200x800")  # Adjust window size

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
        self.canvas_com = tk.Canvas(left_image_frame, bg="gray", height=80, width=80)
        label_operation_1 = tk.Label(left_image_frame, text="Operation", font=('Arial', 14))
        self.canvas_ope = tk.Canvas(left_image_frame, bg="gray", height=80, width=80)
        label_description_1.pack(pady=(20, 0))
        self.canvas_com.pack(pady=(5, 5), fill="both", expand=True)
        label_operation_1.pack(pady=(5, 0))
        self.canvas_ope.pack(pady=(5, 20), fill="both", expand=True)

        # Labels and images in the right image frame
        label_description_2 = tk.Label(right_image_frame, text="Tool", font=('Arial', 14))
        self.canvas_too = tk.Canvas(right_image_frame, bg="gray", height=80, width=80)
        label_operation_2 = tk.Label(right_image_frame, text="Assembly Result", font=('Arial', 14))
        self.canvas_res = tk.Canvas(right_image_frame, bg="gray", height=80, width=80)
        label_description_2.pack(pady=(20, 0))
        self.canvas_too.pack(pady=(5, 5), fill="both", expand=True)
        label_operation_2.pack(pady=(5, 0))
        self.canvas_res.pack(pady=(5, 20), fill="both", expand=True)

        # Text box for instructions
        text_frame = tk.Frame(left_column, width=400)
        text_frame.pack(side="top", fill="both", expand=False, pady=(0, 0))
        self.text_instruction = tk.Text(text_frame, height=10, width=80)
        self.text_instruction.pack(pady=(5, 5), padx=0)

        # Main command frame for holding all control elements
        command_frame = tk.Frame(left_column, bg='white')
        command_frame.pack(fill="x")

        # Controls frame for holding buttons and sliders horizontally
        controls_frame = tk.Frame(command_frame)
        controls_frame.pack(fill="x", expand=True)

        # Buttons and controls in the command frame
        play_button = tk.Button(controls_frame, text="Play Instructions", font=('Arial', 12), command=self.load_and_play(speech=None))
        pause_button = tk.Button(controls_frame, text="Pause Instructions", font=('Arial', 12), command=self.pause_audio())
        volume_control = tk.Scale(controls_frame, from_=0, to=100, orient="horizontal", label="Volume", font=('Arial', 12), command=self.set_volume)
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
        self.realtime_canvas = tk.Canvas(realtime_image_frame, bg="gray", height=300, width=450)
        label_description_realtime.pack(pady=(20, 0))
        self.realtime_canvas.pack(pady=(5, 5), fill="none", expand=False)

        # Text box for assembly progress
        progress_frame = tk.Frame(right_column, width=400, bg='light blue')
        progress_frame.pack(side="top", fill="both", expand=False, pady=(0, 0))
        progress_label = tk.Label(progress_frame, text="Assembly Status", font=('Arial', 14), bg='light blue')
        progress_label.pack()
        self.progress_text = tk.Text(progress_frame, height=15, width=56)
        self.progress_text.pack(pady=(5, 20), padx=20)

        # Button frame at the bottom of right_column
        button_frame = tk.Frame(right_column, bg='light blue')
        button_frame.pack(side='bottom', fill='x', expand=False)
        exit_button = tk.Button(button_frame, text="Exit", font=('Arial', 12), command=self.root.destroy, width=10)
        error_button = tk.Button(button_frame, text="Report Error", font=('Arial', 12), command=lambda: messagebox.showerror("Error", "System Error Reported"), width=20)
        exit_button.pack(side="left", padx=35, pady=25)
        error_button.pack(side="right", padx=35, pady=25)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = AssemblyGUI()
    gui.run()

