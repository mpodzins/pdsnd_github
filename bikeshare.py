import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Three sets which helps getting user input
cities = {'chicago', 'new york city', 'washington'}
months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
days = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

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
    while True:
	    try:
	        city = input('Input city name (chicago, new york city, washington): ').lower()
	        if city in cities:
                    break
	    except ValueError:
	        print('That\'s not a valid String!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
	    try:
	        month = input('Input month name (all, january, february, ... , june): ').lower()
	        if month in months:
                       break
	    except ValueError:
	        print('That\'s not a valid String!')

    # TO DO: get user input for day of week (all, monday, tuesday, ..., sunday)
    while True:
	    try:
	        day = input('Input day of week (all, monday, tuesday, ..., sunday): ').lower()
	        if day in days:
                    break
	    except ValueError:
	        print('That\'s not a valid String!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    popular_month = months[popular_month - 1]
    print('Most common month: {}'.format(popular_month))


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week: {}'.format(popular_day))

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour is at {} o\'clock'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    max_used_st = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly used start station: {}'.format(max_used_st))


    # TO DO: display most commonly used end station
    max_end_st = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station: {}'.format(max_end_st))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + ' TO ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('\nFrequent combination of start station and end station trip: FROM {}'.format(popular_start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = np.sum(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time']))
    totalDays = str(total_travel_time).split()[0]
    clock = str(total_travel_time).split()[2]
    print ("\nThe total travel time was " + totalDays + " days " + clock.split(':')[0] + " hours " + clock.split(':')[1] + " minutes" + "\n")

    # TO DO: display mean travel time
    mean_travel_time = np.mean(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time']))
    clock1 = str(mean_travel_time).split()[2]
    print("The mean travel time was {} hours {} minutes\n".format(clock1.split(':')[0], clock1.split(':')[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        types = df['User Type'].value_counts()
        print("   Type       Count\n")
        print(types)
    except:
        print('There is no user type data available for this city!\n')

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nGender    Count\n")
        print(gender)
    except:
        print('\nThere is no data about gender available for this city!')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is {}\n".format(earliest))
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is {}\n".format(latest))
        most_frequent= df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is {}\n".format(most_frequent))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('\nThere is no data about birth available for this city!')
    print('-'*40)

def five_more(df):
    i = 0
    while True:
        more_data = input('Would you like to see raw data? Please enter yes or no: ').lower()
        if more_data not in ('yes', 'y'):
            break
        else:
            print(df.iloc[i:i+5])
            i += 5




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        five_more(df)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
