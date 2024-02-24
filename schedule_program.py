class Schedule:
    def __init__(self):
        self.schedule_dict = {}

    def add_schedule(self, date, task):
        if date in self.schedule_dict:
            self.schedule_dict[date].append(task)
        else:
            self.schedule_dict[date] = [task]

    def show_schedule(self, date):
        if date in self.schedule_dict:
            return self.schedule_dict[date]
        else:
            return "해당 날짜에는 일정이 없습니다."

    def delete_schedule(self, date, task):
        if date in self.schedule_dict:
            if task in self.schedule_dict[date]:
                self.schedule_dict[date].remove(task)
                return "일정이 삭제되었습니다."
            else:
                return "해당 일정이 없습니다."
        else:
            return "해당 날짜에는 일정이 없습니다."

    def modify_schedule(self, date, task, new_task):
        if date in self.schedule_dict:
            if task in self.schedule_dict[date]:
                index = self.schedule_dict[date].index(task)
                self.schedule_dict[date][index] = new_task
                return "일정이 수정되었습니다."
            else:
                return "해당 일정이 없습니다."
        else:
            return "해당 날짜에는 일정이 없습니다."


my_schedule = Schedule()

while True:
    print("1. 일정 추가")
    print("2. 일정 확인")
    print("3. 일정 삭제")
    print("4. 일정 수정")
    print("5. 종료")
    menu = int(input("메뉴를 선택하세요: "))

    if menu == 1:
        date = input("날짜를 입력하세요 (예: 20240223): ")
        task = input("일정을 입력하세요: ")
        my_schedule.add_schedule(date, task)
    elif menu == 2:
        date = input("일정을 확인할 날짜를 입력하세요 (예: 20240223): ")
        print(my_schedule.show_schedule(date))
    elif menu == 3:
        date = input("일정을 삭제할 날짜를 입력하세요 (예: 20240223): ")
        task = input("삭제할 일정을 입력하세요: ")
        print(my_schedule.delete_schedule(date, task))
    elif menu == 4:
        date = input("일정을 수정할 날짜를 입력하세요 (예: 20240223): ")
        task = input("수정할 일정을 입력하세요: ")
        new_task = input("새로운 일정을 입력하세요: ")
        print(my_schedule.modify_schedule(date, task, new_task))
    elif menu == 5:
        break
