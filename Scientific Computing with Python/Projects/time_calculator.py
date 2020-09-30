def add_time(start, duration, day=None):
    """
    Created for Free Code Camp project.
    
    https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
    """
    
    # Create dictionary for days of the week
    WEEK = {1:"sunday",2:"monday",3:"tuesday",4:"wednesday",5:"thursday",6:"friday",7:"saturday"}
    
    # Create variables from start time
    start_noon = start[-2:]
    start_colon_index = start.find(":")
    start_hour = start[:start_colon_index]
    start_min = start[start_colon_index+1:len(start)-3]
    
    # Create variables from duration
    dur_colon_index = duration.find(":")
    dur_hour = duration[:dur_colon_index]
    dur_min = duration[dur_colon_index+1:]

    # Find the total minutes by adding start and duration
    beg_total_min = int(start_hour) * 60 + int(start_min)
    if start_noon == 'PM':
        beg_total_min += 12*60
    end_total_min = beg_total_min + int(dur_hour) * 60 + int(dur_min)
    
    # Find days passed using total minutes
    days_passed = int(end_total_min/60//24)
    
    # Use divmod function to find hours and minutes passed in "non whole day"
    # https://www.programiz.com/python-programming/methods/built-in/divmod
    hours,minutes = divmod(end_total_min/60%24*60,60)
    hours = round(hours,0)
    minutes = round(minutes,0)
    
    # Check for AM vs PM, adjust hours based on result
    if hours < 12:
        answer_noon = "AM"
        if hours == 0:
            hours = 12
    else:
        answer_noon = "PM"
        if hours > 12:
            hours -= 12
    
    # Add time to answer variable
    answer = str(int(hours)) + ":" + str(int(minutes)).zfill(2) + " " + answer_noon
        
    # Add day of week to answer variable if called in function argument
    if day != None:
        day = day.lower()
        # Convert dictionary to list to "reverse look up key with value"
        # Not certain this is ideal way to do this but it works
        start_day = list(WEEK.keys())[list(WEEK.values()).index(day)]
        new_day = WEEK[(start_day + days_passed)%7]
        answer += ", " + new_day.capitalize()
        
    # Add days passed to answer variable (if any)
    if days_passed > 0:
        if days_passed == 1:
            answer += " (next day)"
        else:
            answer += " (" + str(days_passed) + " days later)"
        
    # Return answer
    return answer


# Testing
# print(add_time("3:00 PM", "3:10")) # Returns: 6:10 PM
# print(add_time("11:30 AM", "2:32", "Monday")) # Returns: 2:02 PM, Monday
# print(add_time("11:43 AM", "00:20")) # Returns: 12:03 PM
# print(add_time("10:10 PM", "3:30")) # Returns: 1:40 AM (next day)
# print(add_time("11:43 PM", "24:20", "tueSday")) # Returns: 12:03 AM, Thursday (2 days later)
# print(add_time("6:30 PM", "205:12")) # Returns: 7:42 AM (9 days later)