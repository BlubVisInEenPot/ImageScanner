from pymediainfo import MediaInfo
from  datetime import *

#'encoded_date'
def getExif_data_video(path, data_type):
    try:
        media_info = MediaInfo.parse(path).to_data()
        creation_date = media_info['tracks'][0].get(data_type)

        print(creation_date)
        if creation_date is not None:
            cleanDate = creation_date.replace("UTC", "").strip()
            return cleanDate

    except OSError as e:
        # log_errors(f"getExif_data(): {e}\nwith file: {path}")
        print("error")

Date = getExif_data_video(r"C:\Users\mort\Videos\file_example_WMV_1920_9_3MB.wmv", "encoded_date")
if Date is not None:
    convertedDate = datetime.strptime(Date, "%Y-%m-%d %H:%M:%S")

    print(f"Date: {Date},\nconvertedDate: {convertedDate},\nconvertedDate_type: {type(convertedDate)}")

#test commit/puch






