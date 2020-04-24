import time
import pandas as pd
import numpy as np
import datetime as dt
import click

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')

def get_filters():
    """Ask user to specify city(ies) and filters, month(s) and weekday(s).
    Returns:
        (str) city - name of the city(ies) to analyze
        (str) month - name of the month(s) to filter
        (str) day - name of the day(s) of week to filter
    """

    print("\nUS Bikeshare data exploration !\n")

    print("Enter exit if you would like to exit the program.\n")

    while True:
        city = choice("\nWhich city or cities do you want do select data, "
                      "New York, Chicago or Washington? Use commas "
                      "to list the names.\n>", CITY_DATA.keys())
        month = choice("\nChoose what month(s) from January to June you want do filter data ?"
                       "Use commas to list the names.\n>",
                       months)
        day = choice("\nWhich weekday(s) do you want do filter bikeshare data?"
                     "Use commas to list the names.\n>", weekdays)

        confirmation = choice("\nConfirm that you would like to apply "
                              "the following filter(s) to the bikeshare data."
                              "\n\n City(ies): {}\n Month(s): {}\n Weekday(s)"
                              ": {}\n\n [Y] Yes\n [N] No\n\n>"
                              .format(city, month, day))
        if confirmation == 'y':
            break
        else:
            print("\nLet us do that one more time")

    print('-'*50)
    return city, month, day

def load_data(city, month, day):
    """Load data for the specified filters of city(ies), month(s) and
       day(s) whenever applicable.
    Args:
        (str) city - name of the city(ies) to analyze
        (str) month - name of the month(s) to filter
        (str) day - name of the day(s) of week to filter
    Returns:
        df - Pandas DataFrame containing filtered data
    """

    print("\nThe program is loading the data for the filters you have chosen.")
    start_time = time.time()

    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)
                                      
        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (months.index(month)+1)]

    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

    return df

def load_data(city, month, day):
    """Load data for the specified filters of city(ies), month(s) and
       day(s) whenever applicable.
    Args:
        (str) city - name of the city(ies) to analyze
        (str) month - name of the month(s) to filter
        (str) day - name of the day(s) of week to filter
    Returns:
        df - Pandas DataFrame containing filtered data
    """

    print("\nThe program is loading the data for the filters you have chosen.")
    start_time = time.time()

    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)

        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (months.index(month)+1)]

    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

    return df

def time_stats(df):
    """Display statistics on the most frequent times of travel."""

    print('\nDisplaying the statistics on the most frequent times of '
          'travel...\n')
    start_time = time.time()

    most_common_month = df['Month'].mode()[0]
    print('For the selected filter, the month with the most travels is: ' +
          str(months[most_common_month-1]).title() + '.')

    most_common_day = df['Weekday'].mode()[0]
    print('For the selected filter, the most common day of the week is: ' +
          str(most_common_day) + '.')

    most_common_hour = df['Start Hour'].mode()[0]
    print('For the selected filter, the most common start hour is: ' +
          str(most_common_hour) + '.')

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

def station_stats(df):
    """Display statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = str(df['Start Station'].mode()[0])
    print("For the selected filters, the most common start station is: " +
          most_common_start_station)

    most_common_end_station = str(df['End Station'].mode()[0])
    print("For the selected filters, the most common start end is: " +
          most_common_end_station)

    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("For the selected filters, the most common start-end combination "
          "of stations is: " + most_common_start_end_combination)

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('For the selected filters, the total travel time is : ' +
          total_travel_time + '.')

    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("For the selected filters, the mean travel time is : " +
          mean_travel_time + ".")

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

def user_stats(df, city):
    """Display statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)

    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender (male or female):")
        print(gender_distribution)
    except KeyError:
        print("We are sorry! There is no data of user genders for {}."
              .format(city.title()))

    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one bike was born in: "
               + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one bike was born in: "
               + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst riders is: "
              + most_common_birth_year)
    except:
        print("We are sorry! There is no data of birth year for {}."
              .format(city.title()))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*50)

def raw_data(df, mark_place):
    """Display 5 line of sorted raw data each time."""

    print("\nYou have chosen to see raw data.")

    if mark_place > 0:
        last_place = choice("\nWould you want to continue from where you ended latest time? "
                            "\n [y] Yes\n [n] No\n\n>")
        if last_place == 'n':
            mark_place = 0

    if mark_place == 0:
        sort_df = choice("\nHow would you like to sort the way the data is displayed? Tap Enter to view the unsorted data.\n \n [1] Start Time\n [2] End Time\n "
                         "[3] Trip Duration\n [4] Start Station\n "
                         "[5] End Station\n\n>",
                         ('1', '2', '3', '4', '5', ''))

        asc_or_desc = choice("\nWould you like it to be sorted ascending or "
                             "descending? \n [a] Ascending\n [d] Descending"
                             "\n\n>",
                             ('a', 'd'))

        if asc_or_desc == 'a':
            asc_or_desc = True
        elif asc_or_desc == 'd':
            asc_or_desc = False

        if sort_df == '1':
            df = df.sort_values(['Start Time'], ascending=asc_or_desc)
        elif sort_df == '2':
            df = df.sort_values(['End Time'], ascending=asc_or_desc)
        elif sort_df == '3':
            df = df.sort_values(['Trip Duration'], ascending=asc_or_desc)
        elif sort_df == '4':
            df = df.sort_values(['Start Station'], ascending=asc_or_desc)
        elif sort_df == '5':
            df = df.sort_values(['End Station'], ascending=asc_or_desc)
        elif sort_df == '':
            pass

    while True:
        for i in range(mark_place, len(df.index)):
            print("\n")
            print(df.iloc[mark_place:mark_place+5].to_string())
            print("\n")
            mark_place += 5

            if choice("Keep printing raw data?"
                      "\n\n[y]Yes\n[n]No\n\n>") == 'y':
                continue
            else:
                break
        break

    return mark_place

def choice(prompt, choices=('y', 'n')):
    """Return a valid input from the user given an array of possible answers.
    """

    while True:
        choice = input(prompt).lower().strip()
        if choice == 'exit':
            raise SystemExit
        elif ',' not in choice:
            if choice in choices:
                break
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        prompt = ("\nSomething went wrong. Please respect the formatting and be sure to enter a valid option:\n")

    return choice


def main():
    while True:
        click.clear()
        city, month, day = get_filters()
        df = load_data(city, month, day)

        mark_place = 0
        while True:
            select_data = choice("\nPlease select the information you would "
                                 "like to obtain.\n\n [1] Time Stats\n [2] "
                                 "Station Stats\n [3] Trip Duration Stats\n "
                                 "[4] User Stats\n [5] Display Raw Data\n "
                                 "[6] Restart\n\n>",
                                 ('1', '2', '3', '4', '5', '6'))
            click.clear()
            if select_data == '1':
                time_stats(df)
            elif select_data == '2':
                station_stats(df)
            elif select_data == '3':
                trip_duration_stats(df)
            elif select_data == '4':
                user_stats(df, city)
            elif select_data == '5':
                mark_place = raw_data(df, mark_place)
            elif select_data == '6':
                break

        restart = choice("\nWould you like to restart the process?\n\n[Y]Yes\n[N]No\n\n>")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
    main()