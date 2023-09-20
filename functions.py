import os 

def make_directories(): 
    INPUT_IMAGE = os.path.join('application_data', 'input_images')
    V_IMAGE = os.path.join('application_data', 'verification_images')
    os.makedirs(INPUT_IMAGE, exist_ok = True)
    os.makedirs(V_IMAGE, exist_ok = True)

make_directories()