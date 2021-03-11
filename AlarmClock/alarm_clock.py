from playsound import playsound
import re
import datetime
import threading

class AlarmClock():

    alarms = []

    def set_alarm(self):
        time = ''

        while not re.match('\d\d\W\d\d', time):
            time = input('\tSet an alarm in form hh:mm ')
            hour = int(time[:2])
            minute = int(time[3:])

        self.alarms.append(datetime.time(hour, minute, 0, 0))

    def show_alarms(self):
        i = 1
        print("""
    Alarms
    ------
            """)
        for alarm in self.alarms:
            print(f'\t{i}. {alarm.hour}:{alarm.minute}')
            i += 1
        print("""
    ------
            """)

    def cancel_alarm(self, alarm_index):

        self.alarms.pop(alarm_index)

    def wait_for_alarm(self):

        while len(self.alarms) != 0:
            curr_time = datetime.datetime.now()
            
            for alarm in self.alarms:
                if alarm.hour == curr_time.hour and alarm.minute == curr_time.minute:
                    
                    playsound('Alarm-ringtone.mp3')
                    self.alarms.pop(self.alarms.index(alarm))
                    continue



al = AlarmClock()
flag = True

while flag:

    print("""
    Choose an option:
    ----------------
    1. Set an alarm
    2. Cancel an alarm
    3. Show alarm's time
    4. Quit
    ----------------

        """)
    choice = ''
    while choice not in ['1','2','3','4']:

        choice = input()

    if choice == '1':
        
        if len(al.alarms) > 0:
            print('The alarm is already set!')
            continue

        else:
            al.set_alarm()
            wait_for_alarm_thread = threading.Thread(target=al.wait_for_alarm)
            wait_for_alarm_thread.start()

    elif choice == '2':
        
        if len(al.alarms) > 0:

            choice = '0'
            al.show_alarms()
        
            while int(choice) not in range(1, len(al.alarms)+1):

                choice = input('\tSelect an alarm to cancel ')

            al.cancel_alarm(int(choice)-1)
        
        else:
            print('\tNo alarm available')

    elif choice == '3':

        al.show_alarms()

    elif choice == '4':
        flag = False
        break