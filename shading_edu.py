import sys
import random as rd
from eppy import modeleditor
from eppy.modeleditor import IDF

iddfile = "C:/Users/Anmol/Desktop/UEM__6_amd_edu/EnergyPlus/ep8.9_windows/Energy+.idd"

# fname1 = "C:/Users/Home/Desktop/session_9_downloads/idf_files/bi_1.idf"

IDF.setiddname(iddfile)
#idf1 = IDF(fname1)


residential = [ "37_00084_0003","37_00084_0006","37_00084_0010","37_00084_0011","37_00084_0017","37_00084_0028","37_00084_0030","37_00256_0002","37_00256_0004","37_00256_0005","37_00257_0005","37_00257_0006","37_00257_0007","37_00257_0008","37_00257_0009","37_00257_0010","37_00257_0011","37_00257_0013","37_00257_0014","37_00257_0015","37_00257_0017","38_00084_0021","38_00257_0008","38_00257_0011","38_00257_0013","37_00084_0001","37_00084_0002","37_00256_0006","37_00257_0012"]
education = ["37_00084_0007","37_00084_0008","37_00084_0013","37_00084_0014","37_00084_0015","37_00084_0018","37_00084_0019","37_00084_0021","37_00084_0022","37_00084_0025","37_00084_0026","37_00084_0027","37_00257_0018","38_00084_0026","38_00257_0018","39_00084_0021","39_00088_0021","39_00084_0026"]

for i in range(0,52):
    fname1 = "C:/Users/Anmol/Desktop/UEM__6_amd_edu/idf_files/bi_{}.idf".format(i+1)
    #print(fname1)
    idf1 = IDF(fname1)
    window_list = idf1.idfobjects['WINDOW']
    window_names = list()
    for item in window_list:
        window_names.append(item.Name)
    
    #print(window_names)

    residential_win = list()
    for item in window_names:
        if item[0:13] in residential:
            residential_win.append(item)
    #print(residential_win)
    
    for win in residential_win:
        idf1.newidfobject(
        "Shading:Overhang".upper(),
        Name = "Overhang_{}".format(win),
        Window_or_Door_Name = win, 
        Height_above_Window_or_Door = 0,
        Tilt_Angle_from_WindowDoor = 90,
        Left_extension_from_WindowDoor_Width = 0,
        Right_extension_from_WindowDoor_Width = 0,
        Depth = 0.1 * rd.randint(3,6))
		
    education_win = list()
    for item in window_names:
        if item[0:13] in education:
            education_win.append(item)
			
    for win in education_win:
        idf1.newidfobject(
        "Shading:Overhang".upper(),
        Name = "Overhang_{}".format(win),
        Window_or_Door_Name = win, 
        Height_above_Window_or_Door = 0,
        Tilt_Angle_from_WindowDoor = 90,
        Left_extension_from_WindowDoor_Width = 0,
        Right_extension_from_WindowDoor_Width = 0,
        Depth = 0.1 * rd.randint(3,6))
		
		
		
    idf1.saveas("C:/Users/Anmol/Desktop/UEM__6_amd_edu/idf_files_overhang/bi_{}_overhang.idf".format(i+1))
