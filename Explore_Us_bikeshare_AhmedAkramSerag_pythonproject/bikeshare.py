import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def check_user_input(input_str,input_type):
    """"checks if input is true """

    while True:
        input_read = input(input_str).lower()
        try:
            if input_read in CITY_DATA and input_type == 1:
                input_read
                break
            elif input_read in ['january','february','march','april','may', 'june','all'] and input_type==2:
                break
            elif input_read in ['sunday','monday', 'tuesday','wednesday','thursday','friday','saturday','all'] and input_type==3:
                break
            else:
                if input_type==1:
                    print('wrong city ,you should choose between chicago,new york city, or washington')
                if input_type == 2:
                    print("wrong month,you should choose between jan through june")
                if input_type==3:
                    print("wrong day")
        except ValueError:
            print('Sorry Error input')
    return input_read

def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.
        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_user_input("what city do you want to check chicago, newyork or washington?",1).lower()

    #get user input for month (all, january, february, ... , june)
    month = check_user_input("which month?",2).lower()

    #get user input for day of week (all, monday, tuesday, ... sunday)
    day= check_user_input("which day of week?? ",3).lower()

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

    # extract month and day of week from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    # extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


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
    print('Most Common Month is')
    print(df['month'].mode()[0])
    # TO DO: display the most common day of week
    print('most common week day  is')
    print(df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('most common Start Hour is')
    print(df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip.

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used Start Station is')
    print(df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('Most commonly used End Station is')
    print(df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print('Most Common Routes are')
    common_routes = df.groupby(['Start Station', 'End Station'])
    print(common_routes.size().sort_values(ascending = False))
    print('another way of calculating most common routes')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time in your city is ')
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time in your city is ')
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users.

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('count of User Type:')
    print(df['User Type'].value_counts().to_frame)

    # TO DO: Display counts of gender in chicago and Newyork
    if city != 'washington':
        print("Gender Count is")
        print(df['Gender'].value_counts().to_frame)
        # TO DO: Display earliest, most recent, and most common year of birth
        print("most common year of birth is")
        print(df[('Birth Year')].mode()[0].astype(int))
        print("earliest year of birth is")
        print(df['Birth Year'].max().astype(int))
        print("most recent year of birth is")
        print(df["Birth Year"].min().astype(int))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

def display_data(df):
    user_display_input=input('Would You like to display 5 rows of the data?').lower()
    if user_display_input.lower() == 'yes':
        i = 0
        while True:
            print(df.iloc[i:i + 5])
            i = i + 5
            ask = input('would you like to show 5 more rows??')
            if ask != 'yes':
                print('thank you')
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes','no']:
           print('Please enter a valid answer')
        elif restart.lower() != 'yes':
            exit()

if __name__ == "__main__":
    main()
