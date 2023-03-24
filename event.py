from tkinter import filedialog
from PIL import Image
from utils import pillow_to_tk_image
import tkinter as tk

def start_event(root, label, json_dict, image_size):
    # TODO: implement

    img = Image.new(mode='RGB', size=image_size)
    imgtk = pillow_to_tk_image(img)
    label.config(image=imgtk)
    label.image=imgtk

def load_event(root, label, json_dict, image_size): #대화상자
    root.file = filedialog.askopenfile(
        initialdir='path',
        title='사용자 정의 json파일을 선택해주세요',
        filetypes=(('json files', '*.json'), ('all files', '*.*'))
    )

    #TODO: make json files
    json_dict['image']=True
    print(json_dict)
    print(root.file.name)

def save_event(root, label, json_dict, image_size):
    import json
    with open('user_defined_layout.json', 'w') as f:
        json.dump(json_dict, f, indent='\t')
    popup_window=tk.Toplevel()
    popup_window.title("SAVED")
    popup_window.geometry("200x200")
    