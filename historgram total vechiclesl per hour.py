import csv

filename = "traffic_data16062024.csv"

with open (filename, "r" ) as traffic:
        
    csv_reader = csv.reader(traffic)
    
    headerline = next(traffic)


    hanley_hours =[] # append karanna hadanawa each hour eka 
    Elm_hours = []
    hanley_total_vechicle_list = []
    
    for i in csv_reader:

        if i[0] == "Hanley Highway/Westway":
            hanley_hours.append(i[2][0:2])
            
        if i[0] == "Hanley Highway/Westway":
            Elm_hours.append(i[2][0:2])

    hanley_total_vechicle_list =  [
            hanley_hours.count("00"),            
            hanley_hours.count("01"),
            hanley_hours.count("02"),
            hanley_hours.count("03"),
            hanley_hours.count("04"),
            hanley_hours.count("05"),
            hanley_hours.count("06"),
            hanley_hours.count("07"),
            hanley_hours.count("08"),
            hanley_hours.count("09"),
            hanley_hours.count("10"),
            hanley_hours.count("11"),
            hanley_hours.count("12"),
            hanley_hours.count("13"),
            hanley_hours.count("14"),
            hanley_hours.count("15"),
            hanley_hours.count("16"),
            hanley_hours.count("17"),
            hanley_hours.count("18"),
            hanley_hours.count("19"),
            hanley_hours.count("20"),
            hanley_hours.count("21"),
            hanley_hours.count("22"),
            hanley_hours.count("23")]
    
    Elm_total_vechicle_list = [
            Elm_hours.count("00"),            
            Elm_hours.count("01"),
            Elm_hours.count("02"),
            Elm_hours.count("03"),
            Elm_hours.count("04"),
            Elm_hours.count("05"),
            Elm_hours.count("06"),
            Elm_hours.count("07"),
            Elm_hours.count("08"),
            Elm_hours.count("09"),
            Elm_hours.count("10"),
            Elm_hours.count("11"),
            Elm_hours.count("12"),
            Elm_hours.count("13"),
            Elm_hours.count("14"),
            Elm_hours.count("15"),
            Elm_hours.count("16"),
            Elm_hours.count("17"),
            Elm_hours.count("20"),
            Elm_hours.count("21"),
            Elm_hours.count("22"),
            Elm_hours.count("23")]

hanley_vechiles = list(map(int, hanley_total_vechicle_list))
Elm_vechiles = list(map(int, Elm_total_vechicle_list))

    
def adding (num):
    return   600 - (num * 75) 

hanley_output = list(map(adding, hanley_vechiles))
Elm_output = list(map(adding, Elm_vechiles))

#print(hanley_total_vechicle_list)
#print(Elm_total_vechicle_list)
print(hanley_output)
print(Elm_output) 


