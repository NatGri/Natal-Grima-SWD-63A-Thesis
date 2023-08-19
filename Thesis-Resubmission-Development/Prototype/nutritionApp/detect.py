import torch


def detect(model_path, image_path):
    # Model Loading
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    # model = torch.hub.load('ultralytics/yolov5', 'custom', path = '/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Thesis-Resubmission-Development/Prototype/nutritionApp/assets/model/best.pt')

    # Images
    im = image_path
    # im = '/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Thesis-Resubmission-Development/Prototype/nutritionApp/assets/imageTaken/test.jpeg'

    # Inference
    results = model(im)

    # Results
    data = results.pandas().xyxy[0]

    unique_names = data['name'].unique()

    print(unique_names)
    return(unique_names)
