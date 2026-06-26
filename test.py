from pymediainfo import MediaInfo
from  datetime import *

#'encoded_date'
def getExif_data_video(path, data_type):
    try:
        media_info = MediaInfo.parse(path).to_data()
        creation_date = media_info['tracks'][0].get(data_type)

        cleanDate = creation_date.replace("UTC", "").strip()
        return cleanDate

    except OSError as e:
        log_errors(f"getExif_data(): {e}\nwith file: {path}")

Date = getExif_data_video(r"\\AMV-DC1.diginet.local\Profiles\morten.goudswaard\videos\file_example_AVI_1920_2_3MG.avi", "encoded_date")
convertedDate = datetime.strptime(Date, "%Y-%m-%d %H:%M:%S")

print(f"Date: {Date},\nconvertedDate: {convertedDate},\nconvertedDate_type: {type(convertedDate)}")






