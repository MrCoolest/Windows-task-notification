try:
    from plyer import notification
    import schedule 
    import time
    from csv import DictReader, DictWriter
    import os
except Exception as e:
    print(f'Error in Importing modules as {e}')

class Task_notify:
    def __init__(self):
        if not os.path.exists('task.csv'):
            self.f_write = open('task.csv','w')
            self.csv_writer = DictWriter(self.f_write, fieldnames=['Title','Task','Time', 'Done'])
            self.csv_writer.writeheader()
            print('Fill the rows of your task in Current created file and Rerun this program!')
            exit()
            


        self.f_read = open('task.csv','r')
        self.csv_reader  = DictReader(self.f_read)



    def work(self,title, message):
        notification.notify(title=title,message=message)

    @property
    def task_notification(self):
        for row in self.csv_reader:
            if row['Done'] == 'FALSE':
                schedule.every().day.at(row['Time']).do(self.work, title = row["Title"], message = row['Task'])
        while True:
            schedule.run_pending()
            time.sleep(1)

        

