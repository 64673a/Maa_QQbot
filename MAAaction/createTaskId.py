from datetime import datetime

def createTaskId(taskType:str):
    date_time = datetime.now()
    taskid=str(date_time)+"-"+taskType
    return taskid
