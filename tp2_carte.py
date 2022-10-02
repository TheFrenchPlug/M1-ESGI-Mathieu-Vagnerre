import os
import sys, re
from threading import local
import geocoder
import folium 

map = folium.Map(location=[48.866667, 2.33333], tiles="Stamen Terrain", zoom_start=5)


#lecture du fichier de log
f = open("access.log.txt", "r")
text = f.read()
                    
#Extraction des IP 
ips = [""] 
list= []

try:
    for data in text:
        try:
            regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',data)
            if regex is not None:
                for match in regex:
                    ips.append(match)
                    
        except AttributeError:
            pass
        
    for i in range(0, len(list)):
        localisation = geocoder.ip(list[i])
        latitude = localisation.lat
        longitude = localisation.lng
        
        if (latitude or longitude) != None:
            folium.Marker(location=[latitude,longitude], popup=list[i]).add_to(map)
            
            if match not in ips:
                        
                        current_ip = {
                            'ip':match,
                            'Latitude':"",
                            'Longitude':"",
                            }
                        loca= geocoder.ip(match)
                        current_ip["Latitude"] = loca.lat
                        current_ip["Longitude"] = loca.lng
                            
                        ips.append(match)
    
#Geolocalisation des IP


    map.save('index.html')

except KeyboardInterrupt:
    exit
