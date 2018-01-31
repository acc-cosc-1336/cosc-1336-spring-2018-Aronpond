def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    '''
    Returns a time in 12 or 24 hour format

    :param hour: The hour of day-
                 when time_type 12 hr hour valid range 1 to 12 otherwise return 'Invalid hours(1-12)'
                 when time_type 24 hr hour valid range 0 to 23 otherwise return 'Invalid hours(range 0-23)'

    :param minutes: Minutes of an hour--minutes valid range 0 to 59 otherwise return 'Invalid minutes(range 0-59)'
    :param seconds:  seconds of an hour--seconds valid range 0 to 59 otherwise 'Invalid seconds(range 0-59)'
    :param time_type: Indicates the format of time to derive 12hr or 24hr
                      Valid time_type values 12 or 24 otherwise return 'Invalid time_type(12 or 24 only)'
                      If time_type is 24 ignore meridiem value;

                      If time_type is 12hr time use meridiem parameter value(AM or PM)

    :param meridiem:  AM, PM

    :return: time in 12 or 24 hour format
      Example for 12 hour format 09:09:09 PM
      Example for 24 hour format 21:09:09
    ADD YOUR CODE AFTER THE THREE QUOTES BELOW (dont forget to include a return statement at the end
    '''
    if time_type 12 hours < 1 or hours > 12 
        print('Invalid hours(1-12)')
    if time_type 24 hours > 23 or hours < 0
        print('Invalid hours(range 0-23)
    if minutes < 0 or minutes > 59
        print('Invalid minutes(range 0-59)
    if seconds < 0 or seconds > 59
        print('invalid seconds(range 0-59)')
    if time_type != 12 or != 24
              print('Invalid time_type(12 or 24 only)')
    if time_type = 12
              meridiem = str('AM')

    if hour < 10
              hour = "0" + str(hour)
    if minutes < 10
              minutes = "0" + str(minutes)
    if seconds < 10
              seconds = "0" + str(seconds)

              
    
    
    time = ''
    #write decision structure code here

    return  time

def time_from_utc(utc_offset, utc_zero_time):
    '''
    Write code to calculate a time zone's time after applying utc_offset
    :param utc_offset:
    :param utc_zero_time:
    :return:
    DON NOT CHANGE ANYTHING IN THIS FUNCTION
    '''

    return (utc_zero_time + utc_offset) % 24