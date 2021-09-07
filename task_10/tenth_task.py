'''	Напишите функцию, которая принимает число - таймзону от GMT (например, Киев - таймзона +2, соответсвенно передаёте 2, или Гавайи - таймзона = -10, соответсвенно передаёте -10), и возвращает текущую дату и время в указаной таймзоне.
Формат:
[<часов>:<минут>:<секунд>] - <день месяца>, <полное название месяца> of <год>
например: [16:22:26] - 11, March of 2021
'''

from datetime import datetime, timezone, timedelta

import pytz


def print_time(offset):

    tz = timezone(timedelta(hours=offset))
    datetime_inserted_timezone = datetime.now(tz)
    datetime_UTC = datetime.now(pytz.timezone('UTC'))

    print("Inserted datetime is:", datetime_inserted_timezone.strftime(f"[%H:%M:%S] - %d, %B of %Y"))
    print("UTC datetime is:", datetime_UTC.strftime(f"[%H:%M:%S] - %d, %B of %Y"))


if __name__ == '__main__':
    print_time(+2)
