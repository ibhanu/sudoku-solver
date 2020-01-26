import cv2 
from main_img import main_process_img
from tensorflow.keras.models import load_model
def capture():
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)
	while True:
		try:
			check, frame = webcam.read()
			print(check) #prints true as long as the webcam is running
			print(frame) #prints matrix values of each framecd 
			cv2.imshow("Capturing", frame)
			key = cv2.waitKey(1)
			if key == ord('s'):
				cv2.imwrite(filename='images_test/saved_img.jpg', img=frame)
				webcam.release()
				img_new = cv2.imread('images_test/saved_img.jpg', cv2.IMREAD_GRAYSCALE)
				img_new = cv2.imshow("Captured Image", img_new)
				im_path = 'images_test/saved_img.jpg'
				model = load_model('model/my_model.h5')
				main_process_img(im_path, model, save=True, display=True)
				#cv2.waitKey(1650)
				#cv2.destroyAllWindows()        
				#capture()
			elif key == ord('q'):
				print("Turning off camera.")
				webcam.release()
				print("Camera off.")
				print("Program ended.")
				cv2.destroyAllWindows()
				break
			
		except(KeyboardInterrupt):
			print("Turning off camera.")
			webcam.release()
			print("Camera off.")
			print("Program ended.")
			cv2.destroyAllWindows()
			break
    
if __name__ == '__main__':
	capture()
