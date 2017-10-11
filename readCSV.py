
import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    with open('heatmap_data_10_200_out.csv','wb') as file:
	    reader = csv.DictReader(file_obj, delimiter=',')
	    for line in reader:
	    	# data = "{location: new google.maps.LatLng(" + str(line["latitude"])  + ", " + str(line["longitude"]) + ") , weight: " + str(float(line["predicted_price"])/1000) + " }, "
	    	data =  line["predicted_price"] + ";" + str(line["latitude"])  + "; " + str(line["longitude"]) 
	    	# data = "new google.maps.LatLng(" + str(line["latitude"]) + ", " + str(line["longitude"]) + "),"
	    	print data
	        # print(line["latitude"]),
	        # print(line["longitude"])

	   
	    	file.write(data)
	    	file.write('\n')	    	

#----------------------------------------------------------------------
if __name__ == "__main__":
    # with open("heatmap_data_5_500.csv") as f_obj:
    with open("heatmap_data_10_200.csv") as f_obj:
    	
        csv_dict_reader(f_obj)


