from tkinter.constants import *
from tkinter.font import BOLD
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from detect import *
from apiCall import *


class Nutrition:

    # Constructor:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title('Nutrition Application')
        self.__window.resizable(False, False)
        self.__window.configure(bg='#c2bebe')

        self.__capturing = True

        self.__win_width = 1000
        self.__win_height = 700

        screen_width = self.__window.winfo_screenwidth()
        screen_height = self.__window.winfo_screenheight()
        x_pos = int((screen_width - self.__win_width) / 2)
        y_pos = int((screen_height - self.__win_height) / 2)

        self.__window.geometry(
            f'{self.__win_width}x{self.__win_height}+{x_pos}+{y_pos}')

        self.title_bar()
        self.webcam()

    def title_bar(self):
        title_bar = tk.Frame(self.__window, bg='#2D6CFC',
                             pady=20, padx=20, width=self.__win_width, height=80)
        title_bar.pack(side=TOP)
        title_bar.pack_propagate(0)

        title = tk.Label(title_bar, text='Kindly Place Fruit In Front of Camera and Press the Nutritional Information Button!',
                         font=('Times New Roman', 18, BOLD), fg='WHITE',
                         bg='#2D6CFC')

        title.pack(side=LEFT)

    def webcam(self):
        # Config - Frame
        camera_frame = tk.Frame(self.__window, bg='WHITE',
                                width=self.__win_width, height=self.__win_height)
        camera_frame.pack(side=TOP)
        camera_frame.propagate(0)

        # Config - Webcam
        widgets_width = self.__win_width - 100

        img_lbl = tk.Label(camera_frame, border=0, background='WHITE', width=widgets_width,
                           height=int(self.__win_height / 1.5))
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Used on On-Click - Checks if Camera is Running - If it is, Takes a Picture.
        def take_picture():
            if cap.isOpened():
                _, frame = cap.read()
                cv2.imwrite(
                    '/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Thesis-Resubmission-Development/Prototype/nutritionApp/assets/imageTaken/takenImage.jpg', frame)
                create_img_label(frame)

        def detection_result():
            # Output:
            detect_output = detect(
                '/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Thesis-Resubmission-Development/Prototype/nutritionApp/assets/model/best.pt', '/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Thesis-Resubmission-Development/Prototype/nutritionApp/assets/imageTaken/takenImage.jpg')
            self.display_prediction(detect_output)

        # On Click:
        btn = tk.Button(camera_frame, text='Nutritional\nInformation',
                        height=self.__win_height, width=250,
                        command=detection_result,
                        fg='#2D6CFC', pady=15, padx=15, border=0, highlightthickness=0)

        def create_img_label(frame):
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)

            img_tk = ImageTk.PhotoImage(image=img)
            img_lbl.img_tk = img_tk

            img_lbl.configure(image=img_tk)
            img_lbl.after(20, take_picture)

        if self.__capturing:
            take_picture()

        img_lbl.pack(side=LEFT)
        btn.pack(side=RIGHT)

    def display_prediction(self, detections):
        predictions = tk.Toplevel(self.__window, background='#ababab')
        predictions.title(f"Your Predictions")
        predictions.propagate(0)

        print(f"detections: {detections}")

        for detection in detections:
            item_frame = tk.Frame(predictions)
            item_frame.pack(fill=tk.X, padx=10, pady=5)

            label = tk.Label(item_frame, text=detection)
            label.pack(side=tk.LEFT)

            button = tk.Button(item_frame, text="Macros",
                               command=lambda i=detection: nutrition_retrieval(i))
            button.pack(side=tk.LEFT)

        def nutrition_retrieval(item):
            item_window_2 = tk.Toplevel(self.__window, background='#ababab')
            item_window_2.title(f"Dietary Macros for: {item}")
            item_window_2.propagate(0)

            label = tk.Label(item_window_2, text=f"Details for: {item}")
            label.pack(padx=20, pady=10)

            nutritionHeaders = ['Serving Size (in grams)', 'Calories', 'Fat', 'Cholesterol', 'Sodium', 'Carbohydrates',
                                'Sugars', 'Protein']
            nutritionResults = apiResults(item)

            row = 1
            for x in range(8):
                print(nutritionHeaders[x], ':', nutritionResults[x])
                item_lbl = tk.Label(item_window_2, text=f'{nutritionHeaders[x]}:', fg='WHITE', bg='#ababab',
                                    font=('Times New Roman', 17, BOLD), padx=10)
                value_lbl = tk.Label(item_window_2, text=f'{nutritionResults[x]}', bg='#ababab', fg='WHITE',
                                     font=('Times New Roman', 17, BOLD), padx=10)

                item_lbl.grid(row=row, column=0, sticky=NW)
                value_lbl.grid(row=row, column=1, sticky=NE)
                row += 1

    def display_predictionOld(self, detection):
        predictions = tk.Toplevel(self.__window, background='#ababab')
        predictions.title(f"Your Predictions")
        predictions.propagate(0)

        #
        # API Results:
        nutritionHeaders = ['Serving Size (in grams)', 'Calories', 'Fat', 'Cholesterol', 'Sodium', 'Carbohydrates',
                            'Sugars', 'Protein']
        nutritionResults = apiResults(detection)
        #

        win_width = 500
        win_height = 500

        screen_width = self.__window.winfo_screenwidth()
        screen_height = self.__window.winfo_screenheight()
        x_pos = int((screen_width - win_width) / 2)
        y_pos = int((screen_height - win_height) / 2)

        predictions.geometry(f'{win_width}x{win_height}+{x_pos}+{y_pos}')

        title = tk.Label(predictions, text='Food Item/s', width=win_width, fg='BLACK', bg='#d4d4d4',
                         font=('Times New Roman', 20, BOLD), pady=10)
        title.pack()

        predictions_list = tk.Frame(
            predictions, bg='#ababab', border=0, highlightthickness=0, pady=5)
        predictions_list.columnconfigure(
            0, minsize=int(win_width / 1.5), weight=1)
        predictions_list.rowconfigure(15, minsize=win_height)
        predictions_list.pack()

        item_lbl = tk.Label(predictions_list, text=f'{detection}', fg='WHITE', bg='#ababab',
                            font=('Times New Roman', 17, BOLD), padx=10)

        item_lbl.grid(row=0, column=0)

        row = 1
        for x in range(8):
            print(nutritionHeaders[x], ':', nutritionResults[x])
            item_lbl = tk.Label(predictions_list, text=f'{nutritionHeaders[x]}:', fg='WHITE', bg='#ababab',
                                font=('Times New Roman', 17, BOLD), padx=10)
            value_lbl = tk.Label(predictions_list, text=f'{nutritionResults[x]}', bg='#ababab', fg='WHITE',
                                 font=('Times New Roman', 17, BOLD), padx=10)

            item_lbl.grid(row=row, column=0, sticky=NW)
            value_lbl.grid(row=row, column=1, sticky=NE)
            row += 1

    def start(self):
        self.__window.mainloop()
