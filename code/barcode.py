'''
Author: Manan Shah
Team: Terminators - Robonox
Date: June 28, 2020
'''

# ***** Import Block *****

from __future__ import print_function
from pyzbar import pyzbar
import numpy as np
import cv2

# ***** End of Import Block *****

'''
Function to decode image to get information from barcode 
Find barcodes and QR codes
'''
def decode(im):
  '''
  params: im - The image file

  return: decodedObjects - The result of the decoded image
  '''
  decodedObjects = pyzbar.decode(im) # decode image

  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data, '\n')  # return type is bytes: b''

  return decodedObjects

# ***** End of decode function *****


'''
Function to sort the parcels according to the pincodes
Put your ranges to sort the parcel based on its pincode
'''
def pincode(pincode_int):
  '''
  params: pincode_int - Integer - The pincode id of the places

  It runs the conveyer belt according to the pincode

  return : none
  '''

  # used for this demo: https://finkode.com/hp/mandi.html  Mandi pincodes

  if pincode_int <= 175040:                 # For the first place
    conveyor_1()
  elif 175040 < pincode_int <= 175080:      # For the second place
    conveyor_2()
  elif 175080<pincode_int <=175126:         # For the third place
    conveyor_3()
  else:
    print("Faulty code, unable to determine!")

# ***** End of pincode determiner *****


# ***** start conveyor belts functions *****

# ''' Function for running belt 1 '''
def conveyor_1():
  print("belt 1 executing..")

# ''' Function for running belt 2 '''
def conveyor_2():
  print("belt 2 executing..")

# ''' Function for running belt 3 '''
def conveyor_3():
  print("belt 3 executing..")
  
# ***** End of conveyor belt functions ******


'''
start Display barcode and QR code location(optional) 
'''
def display(im, decodedObjects):
  '''
  params: 
    im - The image file
    decodeObjects -  The decoded objects

  returns: none
  '''

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4:
      hull = cv2.convexHull(
          np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else:
      hull = points

    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0, n):
      cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

  # Display results
  cv2.imshow("Results", im)
  cv2.waitKey(0)

# ***** End  of Display barcode and QR code location function ***** 


'''
Function to scan box start
If box found found, make suction, scan the barcode and execute the appropriate conveyer.
else return;
'''
def scan_boxes(x_cord,y_cord,z_cord):
  '''
  params:
    x_cord - The x coordinate
    y_cord - The y coordinate
    z_cord - The Z coordinate

  return:
    none
  '''
  # Read image(example)
  im = cv2.imread('175040.png') # A mandi pincode barcode image.

  decodedObjects = decode(im)

  # display(im, decodedObjects) # if you want to display the scan uncomment!

  # Loop across and find the result
  for obj in decodedObjects:
    pincode(int(obj.data))  # need to convert to int.
  
# ***** End of scan box function *****


# ******** MAIN CODE *********

# MAX_X=width of truck
# MAX_Y=height of truck
# MAX_Z=Depth of truck

'''
start from top-left and scan for boxes in xy plane and gradually increase the depth.
'''


# for k in range(MAX_Z):
#  for i in range(MAX_Y):
#    for j in range(MAX_X):# loops run in actual situation
if __name__ == "__main__":
  scan_boxes(1,2,1) # Put i,j,k parameters

