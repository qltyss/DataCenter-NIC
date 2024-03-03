
# Face_Recognition
path = 'persons'
images = []
classNames = []
names = set()
counter = 0
face = ''

black_list = ['Sarah_AlTujjar','Dania_Hamdallah', 'Amera_Alokail','Mohamed_Adil', 'Sara_Almashali', 'Bernard_Baloukjy', 'Yousef_Fathallah','Anthony_Najem', 'Bilal_Anwar',]
white_list = ['Dr_Elie','Esraa_Alqarni', 'Abdullah_AbuSelmiya', ]
black_white = {}

# Others
tcp_value = None
response = ''
detected_objects = {'red': 0, 'green': 0}
red = 0
start_timer = None
condition_met = False
fire_alert = ''
PATH_TO_JOIN = 'datacenterapp/static/mydetect'
detected_labels = []
new_list = []
person_positions = []
value = ''
notification_value = ''

# Fire Detection
image_counter = 0
image_name = ''
fire_image_saved = False  # Initialize the flag
fire_detection_start = None  # To track when fire is first detected
# API URL for the recognition endpoint
recog_url = 'http://192.168.100.64:3005/face_recognition'

frame_counter = 0  # Initialize the frame counter

# Arm 
ip = "192.168.100.243"
port = 6001
