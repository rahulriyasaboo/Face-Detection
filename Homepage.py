import os  # accessing the os functions
import cv2
from check_camera import camer
from Capture_Image import takeImages
from Train_Image import TrainImages
from Recognize import  recognize_attendence
def title_bar():
    os.system('cls')  # for windows
    # title of the program

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                print("check camera...")
                """jmnxzbgkjserkgkhj"""
                checkCamera()
                break
            elif choice == 2:
                print("Capture image from video...")
                CaptureFaces()
                break
            elif choice == 3:
                print("Train images...")
                Trainimages()
                break
            elif choice == 4:
                print("Recognize face...")
                RecognizeFaces()
                break
            elif choice == 5:
                print("Thank You, bye...")
                break
            else:
                print("Invalid Choice. Enter 1-5")
                mainMenu()
        except Exception as e:
            print("Error:",e)
            print("Invalid Choice. Enter 1-5\n Try Again")

# calling the camera test function from check camera.py file
def checkCamera():
    camer()
    print("For check camera...")
    key = input("Enter any key to return main menu")
    mainMenu()
# calling the take image function form capture image.py file

def CaptureFaces():
    takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()
# -----------------------------------------------------------------
# calling the train images from train_images.py file
def Trainimages():
    TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()
# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file
def RecognizeFaces():
    recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()
mainMenu()

