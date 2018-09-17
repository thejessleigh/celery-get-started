import time
from tasks import data_extractor
from celery.result import AsyncResult

# result = add.delay(1, 2)


# while True:
#     _result2 = AsyncResult(result.task_id)
#     status = _result2.status
#     print(status)
#     if 'SUCCESS' in status:
#         print ('result after wait: {result2}'.format(result2=_result2.get()))
#         break
#
#     time.sleep(5)

data_extractor.delay()