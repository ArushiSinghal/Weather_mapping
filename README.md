# Installation #
sudo apt install python-pip

pip install BeautifulSoup4

sudo pip install requests

sudo pip install pandas

sudo pip install lxml

# Scraped Weather Data files #
https://drive.google.com/file/d/1LPn-xfeXa2wIGgi0JQQ0seAAnOolBpKY/view?usp=sharing

https://drive.google.com/file/d/18hR-aOaA52VlNmL9tRSLh7m3FBRlXhi6/view?usp=sharing

https://drive.google.com/file/d/1QOMIStFLEO6VhJKUxcparIikfpOH3OWu/view?usp=sharing

All HTML files without names

https://drive.google.com/file/d/1hAMWSxrFjdisKXBz3CaSW09KIqpJBy9M/view?usp=sharing

All 3034 weather data files of all the region (epw files)

https://drive.google.com/file/d/1tXkb8R0xJ62z3f9SBp1pctN1SQ0OYBX5/view?usp=sharing

Simulations HTML Files (version 1)

https://drive.google.com/open?id=15tNDddwi4cKhnoWZF6BNfrxef_NpqZei

All 3034 weather data files of all the region (stat files)

https://drive.google.com/drive/folders/1-oaBjOUQDTkVfgnU2VqpKj9lFtA7RYXO?usp=sharing


# Documentation #
1) https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2) https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
3) https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
4) EnergyPlus weather data: https://energyplus.net/weather

# Code files Description #
1) scrapper.py -  to scrap epw weather files.
2) scrap_stat_weather_type.py - to find the weather zone from already scrapped stat files.
3) scrapper_stat.py - to scrap stat weather files.
4) simualtion_scrapper_id.py - to find the unique id of weather files from the html files generated after simulations.
5) simualtion_scrapper.py - to find heating, cooling energy cosumption of weather files from the html files generated after simulations.

# Errors #
1) htm file missing of KWT_KISR.Coastal.Station.405850_KISR.epw

2) File present in stat but not in htm:-
  KWT_KISR.Coastal.Station.405850_KISR
  
3) File not present in stat but in htm:-

  USA_WY_Cody.Muni.AWOS.726700_TMY3
  
  USA_WY_Evanston-Uinta.County.AP-Burns.Field.725775_TMY3
  
  USA_WY_Gillette-Gillette.County.AP.726650_TMY3
  
  USA_WY_Green.River-Greater.Green.River.Intergalactic.Spaceport.725744_TMY3
  
  USA_WY_Green.River-Greater.Green.River.Intergalactic.Spaceport.725744_TMY
  
  USA_WY_Jackson.Hole.AP.725776_TMY3
  
  USA_WY_Lander.725760_TMY2
  
  USA_WY_Lander-Hunt.Field.725760_TMY3
  
  USA_WY_Laramie-General.Brees.Field.725645_TMY3
  
  USA_WY_Rawlins.Muni.AP.725745_TMY3
  
  USA_WY_Riverton.Rgnl.AP.725765_TMY3
  
  USA_WY_Rock.Springs.725744_TMY2
  
  USA_WY_Sheridan.726660_TMY2
  
  USA_WY_Sheridan.County.AP.726660_TMY3
  
  USA_WY_Sheridan.County.AP.726660_TMY
  
  USA_WY_Worland.Muni.AP.726665_TMY3
  
  # Error in Files:-
  1) 747185
  2) 832480
  3) 783670
  4) 785260
  5) 828990
  6) 726810
  
  # Very Important link with many details on weather zones of US and other countries:-
  https://xp20.ashrae.org/standard169/index.html
  
  # Papers for literature review
  1) http://www.ibpsa.org/proceedings/BS2011/P_1550.pdf
  2) http://orbit.dtu.dk/files/68467948/p_1481.pdf
