# Import the Pillow library
from PIL import Image, ImageDraw, ImageFont
# import pandas as pd
# import numpy as np
import random
import xml.etree.ElementTree as ET
tree = ET.parse('header.xml')
root = tree.getroot()
# df = pd.read_excel(r'C:\Users\PC\Downloads\Test_AI.xlsx')
col = [0,65,298,481,936,1217,1431]
row = 0
header = ["STT", "Họ và tên", "Số CCHN", "Phạm vi Hoạt động chuyên môn", "Thời gian làm việc", "Vị trí khám bệnh"]
fnt = ImageFont.truetype("timesbd.ttf",25)
number_row = 6
number_table = 4
name_for_cell = ["Nguyễn", "Trọng", "Thị", "Bùi", "Hoàng", "Văn", "Đức", "Mạnh", "Huy", "Hiệp", "Long"]
week = ["thứ 2", "thứ 3", "thứ 4","thứ 5","thứ 6","thứ 7", "chủ nhật"]
# line_of_row = [2,3,4,5,6,7]
# number_for_random =[0,1,2,3,4,5,6,7,8,9]
cell_CCHN = ["/HNO-", "/BYT-", "/BN-"]
local_in_xml =[6,7,8,9,10,11,13]
# Create a new image with the given size and color

img = Image.new("RGB", (1700, 2200), "white")

draw = ImageDraw.Draw(img)
def Draw_table(img, row, color = 'black', width = 3 ):
# Create a draw object to draw on the image
    draw.line((175,100, 1606,100), fill= color, width=width)
    
# Draw a horizontal line 
    for i in range(row+1):
        draw.line((175,100+ (i+1)*105, 1606,100+ (i+1)*105), fill= color, width=width)
# Draw a vertical line 
    for j in col:
        draw.line((175+j,100,175+j, 100+(row+1)*105), fill = color, width =width)
    return img

def Set_Text_Header(img, fnt, fill = "black"):
    for j in range(len(header)):
        draw.text((175+(col[j+1]+col[j])/2,100+105/2), header[j], font= fnt, fill=fill, anchor="mm")
    # for j in range(len(header)):
    #     dd = header[j].split()
    #     h_width, h_height = draw.textsize(header[j], fnt)
    #     s =[]
    #     g =[]
    #     if h_width < col[j+1]-col[j]:
    #         draw.text((175+(col[j+1]+col[j])/2,100+3*47/2), header[j], font= fnt, fill=fill, anchor="mm")
    #     else:
    #         for i in dd:
    #             s.append(i)
    #             ss = " ".join(s)   
    #             text_width, text_height = draw.textsize(ss, fnt)
    #             line = int(h_width/(col[j+1]-col[j]))+1 #số dòng của dữ liệu             
    #             if text_width > col[j+1]-col[j]: 
    #                 vs = s.pop()
    #                 L_1 =" ".join(s)
    #                 draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)), L_1, font= fnt, fill=fill, anchor="mm")
    #                 ff = set(s)^set(dd)  
                   
            
    #         for k in ff:
    #             H1 = " ".join(ff)
    #             h1_width, h1_height = draw.textsize(H1, fnt)
    #             g.append(k)
    #             gg = " ".join(g)   
    #             text_width, text_height = draw.textsize(gg, fnt)
    #             line = int(h_width/(col[j+1]-col[j]))+1 #số dòng của dữ liệu 
    #             if h1_width < col[j+1]-col[j]:
    #                 draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)+47),H1 , font= fnt, fill=fill, anchor="mm")       
    #             else:
    #                 vs = g.pop()
    #                 L_2 =" ".join(g)
    #                 draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)+47), L_2, font= fnt, fill=fill, anchor="mm")
                         
    return img
# def Set_content(img, fnt, fill = "black",width = 3):
#     L = 0
#     LT =-1
#     P = 100 + 4*47
#     for a in range(6):
#         row1 = df.iloc[a]
#         r = np.asarray(row1)
#         for i in range(len(r)):
#             if pd.isna(r[i]):
#                 r[i]=" "
#             content = r.tolist()
#         for i in range(len(content)):
#             c_width, c_height = draw.textsize(str(content[i]), fnt)
#             line = int(c_width/(col[i+1]-col[i]-16))+1
#             if line > L:
#                 L = line
#         LT += L  
#         S = L
#         L=0     
#         draw.line((175,P + 47*LT, 1597,P + 47*LT), fill= fill, width=width)
#         for j in col:
#             draw.line((175+j,100+4*47,175+j, 100+(LT+4)*47), fill = fill, width =width)
#         P = 100+(L+4)*47


#         for j in range(len(content)):
            
#             if j == 4:
#                 dd = str(content[j]).split()
#                 h_width, h_height = draw.textsize(str(content[j]), fnt)
#                 s =[]
#                 g =[]
#                 if h_width < (col[j+1]-col[j] - 16):
#                     d.text((175+col[j]+16,100+(4+LT-(S-1)-1/2)*47), content[j], font= fnt, fill=fill,anchor = "lm")
#                 else:
#                     for i in dd:
#                         s.append(i)
#                         ss = " ".join(s)   
#                         text_width, text_height = draw.textsize(ss, fnt)
#                         line = int(h_width/(col[j+1]-col[j]-16))+1 #số dòng của dữ liệu             
#                         if text_width > col[j+1]-col[j]-16: 
#                             vs = s.pop()
#                             L_1 =" ".join(s)
#                             d.text((175+col[j]+16,100+(4+LT-(S-1)-1/2)*47), L_1, font= fnt, fill=fill,anchor = "lm")
#                             ff = set(s)^set(dd)  
                        
                    
#                     for k in ff:
#                         H1 = " ".join(ff)
#                         h1_width, h1_height = draw.textsize(H1, fnt)
#                         g.append(k)
#                         gg = " ".join(g)   
#                         text_width, text_height = draw.textsize(gg, fnt)
#                         line = int(h_width/(col[j+1]-col[j]-16))+1 #số dòng của dữ liệu 
#                         if h1_width < col[j+1]-col[j]:
#                             d.text((175+col[j]+16,100+(4+LT-(S-2)-1/2)*47),H1 , font= fnt, fill=fill,anchor = "ls")       
#                         else:
#                             vs = g.pop()
#                             L_2 =" ".join(g)
#                             d.text((175+col[j]+16,100+(4+LT-(S-2)-1/2)*47), L_2, font= fnt, fill=fill,anchor = "ls")
#                 continue
            
#             d.text((175+(col[j+1] +col[j])/2 , 100+(4+LT-S+(S/2))*47), str(content[j]), font= fnt, fill=fill,anchor = "mm")
            
#     return img

def Set_content(img, fnt, fill = "black",width = 3):
    L = 0
    ymax_0 = 205
    tree = ET.parse('header.xml')
    root = tree.getroot()
    for i in range(number_row):
        random_cell = random.randint(3,7)
        name_cell =[]
        L += random_cell
        P = 100 + (L + 3)*35
        draw.line((175,P, 1606,P), fill= fill, width=width)
        for j in col:
            draw.line((175+j,100+3*35,175+j, 100+(L+3)*35), fill = fill, width =width)
        # STT
        draw.text((175+(col[0]+col[1])/2,100+(L+3)*35-(random_cell/2)*35), str(i+1), font= fnt, fill=fill, anchor="mm")
        #  Số CCHN
        CCHN1 = Set_number_CCHN()
        CCHN2 = random.choice(cell_CCHN)
        # print(type(random.choice(cell_CCHN)))
        draw.text((175+(col[2]+col[3])/2,100+(L+3)*35-(random_cell/2)*35 - 35/2),CCHN1 + CCHN2 , font= fnt, fill=fill, anchor="mm")
        draw.text((175+(col[2]+col[3])/2,100+(L+3)*35-(random_cell/2)*35 + 35/2), "CCHN", font= fnt, fill=fill, anchor="mm")
        # Họ và tên
        for k in range(random.choice([3,4])):
            name_cell.append(random.choice(name_for_cell))
        name_put_cell = " ".join(name_cell)
        text_width, text_height = draw.textsize(name_put_cell, fnt)
        if text_width < (col[2]-col[1]-10):
            draw.text((175+col[1]+10,100+(L+3)*35-(random_cell/2)*35 ),name_put_cell , font= fnt, fill=fill, anchor="lm")
        else:
            pop_name = name_cell.pop()
            name_put_cell = " ".join(name_cell)
            draw.text((175+col[1]+10,100+(L+3)*35-(random_cell/2)*35 - 35/2 ),name_put_cell , font= fnt, fill=fill, anchor="lm")
            draw.text((175+col[1]+10,100+(L+3)*35-(random_cell/2)*35 + 35/2),pop_name , font= fnt, fill=fill, anchor="lm")
        # Thời gian làm việc
        time = "Từ " + str(random.randint(1,24)) + "h00- " + str(random.randint(1,24)) + "h00"
        day = "Từ " + str(random.choice(week)) + "- " + str(random.choice(week)).capitalize()
        # print(time)
        # print(day)
        draw.text((175+(col[4]+col[5])/2,100+(L+3)*35-(random_cell/2)*35 - 35/2),time , font= fnt, fill=fill, anchor="mm")
        draw.text((175+(col[4]+col[5])/2,100+(L+3)*35-(random_cell/2)*35 + 35/2),day , font= fnt, fill=fill, anchor="mm")
        # Vị trí khám bệnh
        line_use_in_cell_6= random.randint(1, random_cell)
        # print(line_use_in_cell)
        Line = 0
        while Line < line_use_in_cell_6:
            content_cell = []   
            text_width = 0
            while text_width < col[6]-col[5]-10:
                content_cell.append(str(random.choice(name_for_cell)))
                content_write = " ".join(content_cell)   
                text_width, text_height = draw.textsize(content_write, fnt)
            content_cell.pop()
            content_write = " ".join(content_cell)
            draw.text((175+(col[5]+col[6])/2,100+(L+3 - random_cell )*35+((random_cell-line_use_in_cell_6)/2)*35 +35/2 +35*Line),content_write , font= fnt, fill=fill, anchor="mm")
            Line += 1
        # Phạm vi hoạt đông chuyên môn
        Line4 = 0
        while Line4 < random_cell-1:
            content_cell4 = []   
            text_width = 0
            while text_width < col[4]-col[3]-10:
                content_cell4.append(str(random.choice(name_for_cell)))
                content_write4 = " ".join(content_cell4)   
                text_width, text_height = draw.textsize(content_write4, fnt)
            content_cell4.pop()
            content_write4 = " ".join(content_cell4)
            draw.text((175+(col[3]+col[4])/2,100+(L+3 - random_cell )*35 + 35/2 + 35*Line4),content_write4 , font= fnt, fill=fill, anchor="mm")
            Line4 +=1
        content_last_line = []
        for m in range(random.randint(1,6)):
            content_last_line.append(str(random.choice(name_for_cell)))
        content_write_last = " ".join(content_last_line)
        draw.text((175+(col[3]+col[4])/2,100+(L+3)*35 - 35/2),content_write_last , font= fnt, fill=fill, anchor="mm")

        # label table row 
        object = ET.SubElement(root, "object")

        name = ET.SubElement(object, "name")
        name.text = "Table row"

        pose = ET.SubElement(object, "pose")
        pose.text = "Unspecified"

        truncated = ET.SubElement(object, "truncated")
        truncated.text = "0"

        difficult = ET.SubElement(object, "difficult")
        difficult.text = "0"

        bndbox = ET.SubElement(object, "bndbox")

        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(176)

        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(ymax_0)

        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(1598)

        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(ymax_0 + random_cell*35)

        ymax_0 = ymax_0 + random_cell*35
    # Kéo dài các table column và table
    for n in local_in_xml:
        root[n][4][3].text = str(int(root[n][4][3].text) + L*35)
    tree.write("filename.xml")
    return img

def Set_number_CCHN():
    number_CCHN = []
    for i in range(6):
        number_CCHN.append(str(random.randint(0,9)))
    CCHN = "".join(number_CCHN)
    return CCHN

#Run 
for o in range(number_table):
    img = Image.new("RGB", (1700, 2200), "white")
    draw = ImageDraw.Draw(img)
    img = Draw_table(img, row)
    img = Set_Text_Header(img, fnt)
    # img = Set_content(img, fnt)
    img = Set_content(img,fnt)
    tree = ET.parse('filename.xml')
    # tree = ET.ElementTree(root)
    tree.write(f'Table_{o}.xml')
    img.save(f'Table_{o}.png')
    img.show()   
# img = Draw_table(img, row)
# img = Set_Text_Header(img, fnt)
# img = Set_content(img, fnt)
# img.show()
# img.save("header.png")