import numpy as np #for data operations
import os #for easy access of systeme to read and write files
import matplotlib.pyplot as plt #for data visualization

#in this section we will loop through data of each sensor one by one
sensors = ["blickfeld", "radar", "velodyne"]

folder_paths_all = {"clear" : "D:\MASTERS\ACADEMICS\RADAR LIDAR\CBuilding\CBuilding\csv\c_building_pedestrian_clear_anon/" , 
                    "fog" : "D:\MASTERS\ACADEMICS\RADAR LIDAR\CBuilding\CBuilding\csv\c_building_pedestrian_fog_anon/"} #this folder path can vary system by system

for condition in folder_paths_all.keys():
    for sensor in sensors:
        f = folder_paths_all[condition] + sensor + "/"
        files = os.listdir(f)
        
        
        if (sensor == "blickfeld" and condition == "clear"):
            blickfeld_data_clear = np.zeros((1,5))
        elif(sensor == "radar" and condition == "clear"):
            radar_data_clear = np.zeros((1,5))
        elif(sensor == "velodyne" and condition == "clear"):
            velodyne_data_clear = np.zeros((1,6))

        elif(sensor == "blickfeld" and condition == "fog"):
            blickfeld_data_fog = np.zeros((1,5))
        elif(sensor == "radar" and condition == "fog"):
            radar_data_fog = np.zeros((1,5))
        elif(sensor == "velodyne" and condition == "fog"):
            velodyne_data_fog = np.zeros((1,6))


        csv_files = [file for file in files if file.endswith('.csv')]  # two lines may be redundant
        print(csv_files)


        for file in csv_files:
            print(folder_paths_all[condition] + file)
            arr = np.loadtxt(f + file, delimiter=" ")
            print(arr.shape)
            
            print("Reading {0} data for {1} conditions ".format(sensor, folder_paths_all[condition]))

            if(sensor == "blickfeld" and condition == "clear"):
                blickfeld_data_clear = np.concatenate((blickfeld_data_clear, arr), axis=0)
            elif(sensor == "radar" and condition == "clear"):
                radar_data_clear = np.concatenate((radar_data_clear, arr), axis=0)
            elif(sensor == "velodyne" and condition == "clear"):
                velodyne_data_clear = np.concatenate((velodyne_data_clear, arr), axis = 0)
            

            elif(sensor == "blickfeld" and condition == "fog"):
                blickfeld_data_fog = np.concatenate((blickfeld_data_fog, arr), axis=0)
            elif(sensor == "radar" and condition == "fog"):
                radar_data_fog = np.concatenate((radar_data_fog, arr), axis=0)
            elif(sensor == "velodyne" and condition == "fog"):
                velodyne_data_fog = np.concatenate((velodyne_data_fog, arr), axis = 0)

     


#####################################################################################################



blickfeld_data_clear = blickfeld_data_clear[ : , 0:3]

radar_data_clear = radar_data_clear[:,0:3]

velodyne_data_clear = velodyne_data_clear[:, 0:3]

blickfeld_data_fog = blickfeld_data_fog[: , 0:3]

radar_data_fog = radar_data_fog[:,0:3]

velodyne_data_fog = velodyne_data_fog[:, 0:3]



blickfeld_clear = np.sqrt(np.sum(np.square(blickfeld_data_clear), axis=1))

radar_clear = np.sqrt(np.sum(np.square(radar_data_clear), axis = 1))

velodyne_clear = np.sqrt(np.sum(np.square(velodyne_data_clear), axis = 1))




blickfeld_fog = np.sqrt(np.sum(np.square(blickfeld_data_fog), axis=1))

radar_fog = np.sqrt(np.sum(np.square(radar_data_fog), axis = 1))

velodyne_fog = np.sqrt(np.sum(np.square(velodyne_data_fog), axis = 1))



#---------Blickfeld clear plot------------------------------------------------------------------------------------
plt.hist(blickfeld_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "blue", edgecolor="black")
plt.title("Histogram for Blickfeld Point Cloud- Clear Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tpbc = len(blickfeld_clear)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tpbc}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(blickfeld_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,2100000)
plt.show()

#--------------Blickfeld Fog plot------------------------------------------------------------------------------------
plt.hist(blickfeld_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "red", edgecolor="black")
plt.title("Histogram for Blickfeld Point Cloud- Fog Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tpbf = len(blickfeld_fog)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tpbf}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(blickfeld_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,2100000)
plt.show()

#-----------------Radar Clear Plot---------------------------------------
plt.hist(radar_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "blue", edgecolor="black")
plt.title("Histogram for Radar Point Cloud- Clear Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tprc = len(radar_clear)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tprc}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(radar_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,60000)
plt.show()

#-----------Radar Fog Plot--------------
plt.hist(radar_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "red", edgecolor="black")
plt.title("Histogram For Radar Point Cloud- Fog Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tprf = len(radar_fog)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tprf}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(radar_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,60000)
plt.show()
#------------Velodyne Puck Clear---------------------
plt.hist(velodyne_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "blue", edgecolor="black")
plt.title("Histogram For Velodyne Point Cloud- Clear Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tpvc = len(velodyne_clear)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tpvc}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(velodyne_clear, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,13000000)
plt.show()

#------------Velodyne Puck Fog---------------------
plt.hist(velodyne_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color = "red", edgecolor="black")
plt.title("Histogram For Velodyne Point Cloud- Fog Scenario")  # Set the title for the plot
plt.xlabel("Distance in Meters")  # Set the x-axis label
plt.ylabel("Number of Points in a Range")  # Set the y-axis label
plt.xticks(range(0,70,5))
# Add text annotation for the total number of values
tpvf = len(velodyne_fog)
plt.text(0.8*plt.xlim()[1], 0.9*plt.ylim()[1], f'Total Number of Points: {tpvf}', ha='right', va='top')

# Add text annotations for each bar
for i, value in enumerate(plt.hist(velodyne_fog, bins=[0,5,10,15,20,25,30,35,40,45,50], color="red", edgecolor="black")[0]):
    # Calculate the x-coordinate for the text (center of the bin)
    x_coordinate = ([0,5,10,15,20,25,30,35,40,45,50][i] + [0,5,10,15,20,25,30,35,40,45,50][i + 1]) / 2
    plt.text(x_coordinate,value, str(int(value)), ha='center', va='bottom', rotation='vertical')
plt.ylim(0,13000000)
plt.show()
