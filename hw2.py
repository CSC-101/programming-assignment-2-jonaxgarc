import data
from data import Point, Duration, Rectangle, Song

# Write your functions for each part in the space below.

# Part 1
def create_rectangle (point1:Point, point2:Point) -> Rectangle:
    #Get coordinates from points
    x1, y1 = point1.x, point1.y
    x2, y2 = point2.x, point2.y
    #Decides which coordinate should go where
    top_left_x = min(x1, x2)
    top_left_y = max(y1, y2)
    bottom_right_x = max(x1, x2)
    bottom_right_y = min(y1, y2)
    #creates the top left point and the bottom right point
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    return Rectangle(top_left, bottom_right) #returns the rectangle object


# Part 2
def shorter_duration_than(duration1:Duration, duration2:Duration) -> bool:
    def total_seconds(self) -> int: # Converts minutes to seconds and adds the total
        return self.minutes * 60 + self.seconds
    return total_seconds(duration1) < total_seconds(duration2) # Compares the duration between the two values

# Part 3
def songs_shorter_than(song:list[Song], duration:Duration) ->list[Song]:
    shorter_songs = [] # Creates an empty list
    for i in song: # Checks every song in the list
        if i.duration.minutes * 60 + i.duration.seconds < duration.minutes * 60 + duration.seconds: #If song is shorter than the duration it adds it to the list
            shorter_songs.append(i)
    return shorter_songs

# Part 4
def running_time(songs:list[Song], playlist: list[int]) -> Duration:
    duration = Duration(0, 0)  # The duration starts with no time

    for i in playlist:
        if 0 <= i < len(songs):  # Checks the index is valid
            duration += songs[i].duration  # Adds the song's duration

    return duration

# Part 5
def validate_route(cityLinks:list[list[str]],cityNames:list[str]) -> bool:
    # Makes a list to make checking for links easier
    links_list = [links for links in cityLinks]
    # Checks if links happen by looking in the list for the city
    for i in range(len(cityNames)-1):
        city1 = cityNames[i]
        city2 = cityNames[i+1]
        if not (([city1, city2] in links_list) or ([city2, city1] in links_list)):
            return False # Returns false if the pair is not valid
        else:
            return True # Returns true if the pair is valid
# Part 6
def longest_repetition(lst:list[int]) -> int:
    max_count = 0 #makes it so there is no repetitions in the beginning
    max_index = -1 #makes it so index 0 replaces max_index
    current_count = 1 # Makes it so it count the first index
    current_index = 0 #Starts in the very first index
    for i in range(1, len(lst)): # Goes through the list of numbers
        if lst[i] == lst[i - 1]: #Compares the current index with the one before that
            current_count += 1 # Adds 1 to current count if the program sees another again in a row
        else:
            if current_count > max_count: # Compares the current count to the max count
                max_count = current_count # If larger the current_count becomes the new max one
                max_index = current_index # If larger the current_index becomes the new max_index
            current_count = 1 # After the repetition is over the count restarts
            current_index = i # The current index goes to the next index

    #Checks at the end of the loop if the current count is bigger than the max
    if current_count > max_count:
        max_index = current_index
    return max_index