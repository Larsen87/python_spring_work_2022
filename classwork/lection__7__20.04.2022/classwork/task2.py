#todo: задан словарь

dic = { "sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12,
        "overscan_top":10 }

# Нужно создать  файл config.txt с содержимым вида:
sdtv_mode=2
hdmi_drive=2
hdmi_group=2
hdmi_mode=16
overscan_left=20
overscan_right=12
overscan_top=10

f = open("config.txt",mode="a", encoding="UTF-8")

for key, val in dic.items():
        f.write(key+"="+str(val)+"\n")

f.close()

