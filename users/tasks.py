
from celery import shared_task  # Used to mark a function as a Celery task
from celery.utils.log import get_task_logger  # U
logger = get_task_logger(__name__)

import time


@shared_task(name="my_task")
def my_task():
    for i in range(10):
        print(i)
        time.sleep(1)
    logger.info("This is a test task")


# @shared_task(bind=True)
# def none_task(self):
#     for i in range(10):
#         print(i)
#     return "Done!"