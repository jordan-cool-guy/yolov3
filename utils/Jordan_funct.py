import cv2
import numpy as np



def line_draw(id,class_ids,knee_loc_2,hip_loc_2,foot_loc_2,box_2):
    '''
    for desired id, stored x and y coords in loc_2 list 
    '''
    if id in class_ids:
        if id == 0:
            knee_loc_2.append(box_2[class_ids.index(id)])
        elif id == 1:
            hip_loc_2.append(box_2[class_ids.index(id)])
        elif id == 2:
            foot_loc_2.append(box_2[class_ids.index(id)])
        else:
            pass
                

def depth(point_id,cls):
    '''
    of the different class ids (0,1,2),
    depth() finds the desired id in the class_ids list, finds the index of that id,
    and finds the y coordinates of that
    index in the box list. It then appends it to its own body part lsit.
    '''
    if point_id in cls:
        if point_id == 0:
            knee_loc.append(box[cls.index(point_id)])
        elif point_id == 1:
           hip_loc.append(box[cls.index(point_id)])
        else:
            pass
    

def outputs(layerOutputs,height,width,boxes,confidences,class_ids,box,box_2, xyxy):
    '''
    goes through the output of the network and 
    gets the scores, highest class ids, and the confidence of the class id
    if the confidence is higher than thresh, it finds the coords and appends to boxes,
    box, box_2. It also appendes the confidences. box list is for depth, and box_2 is for the limb connection
    '''
  
   
    box.append(int(x[3]))




def plot(indexes,boxes,classes,class_ids,confidences,colors,image,font):
    #plots bounding box on image
    #same thing as plot_one_box
    if len(indexes)>0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(image, (x,y), (x+w, y+h), color, 2)
            cv2.putText(image, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
