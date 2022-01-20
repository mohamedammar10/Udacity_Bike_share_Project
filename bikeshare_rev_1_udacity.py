import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv','new york city':
'new_york_city.csv','washington': 'washington.csv' }

def get_filters():

    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    #Loop to ensure the correct user input correct city name
    while city not in CITY_DATA.keys():
        print()

        city = str(input("enter the city name:")).lower()

        if city not in CITY_DATA.keys():
            print("Please check the city name!")

        #Loop to ensure user input correct month OR choosen all
        #Creating a dictionary to store all the months.
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        month = str(input("enter the month from: January to June:")).lower()

        if month not in MONTH_DATA.keys():
            print("Please check the month name!")

        #Loop to ensure user input correct day OR all
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:

        day = str(input("enter the day:")).lower()

        if day not in DAY_LIST:
            print("Please check the day name!")

        # print the selection tiltle for the following calculation:
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month 
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return (df)


def time_stats(df):
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO:1 display the most common month

        # find the most common month
        popular_month = df['month'].mode()[0]

        print('Most common month:', popular_month)

        # TO DO:2 display the most common day of week

        # find the most common weekday
        popular_day = df['day_of_week'].mode()[0]

        print('Most common day:', popular_day)

        # TO DO:3 display the most common start hour

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

        # find the most popular hour
        popular_hour = df['hour'].mode()[0]

        print('Most Popular Start Hour:', popular_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO:1 display most commonly used start station
        popular_start_station = df['Start Station'].mode()[0]

        print('Most Popular Start station:', popular_start_station)

        # TO DO:2 display most commonly used end station
        popular_end_station = df['End Station'].mode()[0]

        print('Most Popular end station:', popular_end_station)

        # TO DO:3 display most frequent combination of start station and end station trip
        df['Start End Station'] = df['Start Station'] +","+ df['End Station']
        popular_start_end_station=df['Start End Station'].mode()[0]

        print('Most Popular start/end station:', popular_start_end_station)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO:1 display total travel time
        total_travel_time=(df['Trip Duration']).sum()
        print('total_travel_time in hour:', total_travel_time/3600)
       
        # TO DO:2 display mean travel time
        mean_travel_time=(df['Trip Duration']).mean()
        print('mean_travel_time in min:', mean_travel_time/60)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

       
        # if condition to check column exist in df
        if 'User Type' not in df.columns:
            print("Data does not contain User Type column")
        else: 
             # TO DO: Display counts of user types
            user_types=(df['User Type']).value_counts()
            print('\n user_types: \n', user_types)

        
        ## if condition to check column exist in df
        if 'Gender' not in df.columns:
            print("Data does not contain 'Gender' column")
        # TO DO: Display counts of gender
        else:    
            gender_types=(df['Gender']).value_counts()
            print('\n Gender: \n', gender_types)
        
        
        # if condition to check column exist in df
        if 'Birth Year' not in df.columns:
            print("Data does not contain 'Birth Year' column")
        else:    
        # TO DO: Display earliest, most recent, and most common year of birth
            youngest_rider_age=(df['Birth Year']).max()
            oldest_rider_age=(df['Birth Year']).min()
            average_rider_age=(df['Birth Year']).mode()[0]
            print('\n youngest_rider_age:', youngest_rider_age)
            print('\n oldest_rider_age:', oldest_rider_age)
            print('\n average_rider_age:', average_rider_age)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(list(df.columns))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
