import zipfile
import re
from datetime import datetime


def get_images_size(from_date: datetime, to_date: datetime) -> int:
    with zipfile.ZipFile("resources/logs.zip", "r") as myfile:
        candidates_list = re.findall(r"((^|\n).+\[(1[89])/May/2015.+\] \"GET.+\.(png|jpg|jpeg|gif).+\" 200.+)",
                                     myfile.read("logs.txt").decode())
        sum = 0
        for candidate in candidates_list:
            date_str = re.findall(r"\[.+]", candidate[0])[0][1:-7]
            date = datetime.strptime(date_str, "%d/%b/%Y:%X")
            if from_date < date < to_date:
                size = re.findall(r".+\d{3} (\d+)", candidate[0])
                sum += int(size[0])
        return sum


print(get_images_size(datetime(2015, 5, 18, 13, 18, 54), datetime(2015, 5, 19, 12, 8, 4)))
