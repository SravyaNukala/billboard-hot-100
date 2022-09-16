"""
Generating Sorted List of Artists from “Billboard Hot 100” based on the total number of letters in their track title.

Run the below command to install billboard during first run
pip install billboard.py

some artists have multiple tracks. So, used List instead of dictionary as it won't allow duplicate keys
"""
import billboard

# Fetching Hot-100 data into a variable
data = billboard.ChartData('hot-100')

# Iterating data and assigning artist name and title track length by removing spaces and special characters to a list
data_list = [(song.artist, len(''.join(title for title in song.title if title.isalnum()))) for song in data]
print(f"Data list before sorting: {data_list} \n")

# Sorting the list values in the ascending order and those with the same values will be in alphabetical order
data_list.sort(key=lambda item: item[::-1])
print(f"Data list after sorting: {data_list} \n")

# Iterating the sorted list and appending artist names to artist_list
artist_list = [artist[0] for artist in data_list]
print(f"Sorted List of Artists: {artist_list} \n")
print(f"Length of Artists with all duplicate keys: {len(artist_list)}")
