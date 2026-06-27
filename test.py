# from PIL import Image
# from PIL.ExifTags import TAGS
# from pillow_heif import register_heif_opener

# register_heif_opener()

# def getExif_data(path, data_type):
#     try:
#         imagename = path
#         image = Image.open(imagename)
#         exifdata = image.getexif()
#         exif = { TAGS.get(tag_id, tag_id): value for tag_id, value in exifdata.items() }
#         return(exif.get(data_type))
    
#     except OSError as e:
#         print(f"error: {e}")
#         # log_errors(f"getExif_data(): {e}\nwith file: {path}")


# print(getExif_data(r"C:\Users\mort\Pictures\IMG_1522.HEIC", "DateTime"))

string = "UTC YYYY-MM-DD HH:MM:SS"

print(string.replace("UTC", "").replace("-", ":").strip())

# string.replace("condition1", "").replace("condition2", "text")
