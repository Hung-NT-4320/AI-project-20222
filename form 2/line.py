# Import the Pillow library
from PIL import Image, ImageDraw, ImageFont
# import pandas as pd
# import numpy as np
import xml.etree.ElementTree as ET
import random
import time
content = ["Tôi","Bách", "Khoa", "toán", "lý", "hóa", "văn", "anh","sinh","thể", "địa","Chào","hoạt", "chạy","nhảy", "đá","sút", "ném", "ngã", "vấp","qua","trượt", "AI","thầy", "cô","trò", "bắt", "đánh","yêu", "ghét", "A", 0,1,2,3,4,5,6,7,8,9,10,11,12, "ông", "bà","họp", "chính", "phụ"]
# df = pd.read_excel(r'D:\AI\Project\Nhom_1\temp1_Danh _muc_ky_thuat_phe_duyet\Test.xlsx')
col = [0,113,300,427,1090,1422]
col2 = [0,113,300,427,1090,1173,1256,1339,1422]
row = 0
number_row = 12
cell_of_row = [1,2,3,4]
final_word = [1,2,3,4,5,6,7,8,9]
number_table = 3
check_or_no =["X", " "]
locationInXML =[7,8,9,10,13,14,15,16,18]
header = ["STT", "QDUBND THÀNH PHỐ", "TT CỦA BYT", "DANH MỤC KỸ THUẬT", "PHÂN TUYẾN KỸ THUẬT"]
header2 =["A", "B", "C", "D"]

tree = ET.parse('table.xml')
root = tree.getroot()

# content =["1", " ", "1", "Theo dõi huyết áp liên tục không xâm nhập tại giường ≤ 8 giờ trong một ngày bất kỳ trong tuần", "X", "X","X"," "]
# content2 =["2", " ", "1", "Theo dõi huyết áp liên tục không xâm nhập tại giường ≤ 8 giờ trong một ngày", "X", "X","X"," "]
fnt = ImageFont.truetype("timesbd.ttf",25)
# Create a new image with the given size and color

img = Image.new("RGB", (1700, 2200), "white")
draw = ImageDraw.Draw(img)

# Vẽ bảng cho header
def Draw_table(img, row, color = 'black', width = 3 ):
# Create a draw object to draw on the image
    
    
# Draw a horizontal line 
    for i in range(row +1):
        draw.line((175,100+ (i+4)*47, 1597,100+ (i+4)*47), fill= color, width=width)
# Draw a vertical line 
    for j in col:
        draw.line((175+j,100,175+j, 100+(row+4)*47), fill = color, width =width)
    # draw.line((175, 100, 175, 100+(row+4)*47),fill=color, width=width)
    # draw.line((175+113, 100, 175+113, 100+(row+4)*47),fill=color, width=width)
    # draw.line((175+300, 100, 175+300, 100+(row+4)*47),fill=color, width=width)
    # draw.line((175+427, 100, 175+427, 100+(row+4)*47),fill=color, width=width)
    # draw.line((175+1090, 100, 175+1090, 100+(row+4)*47),fill=color, width=width)
    # draw.line((1597, 100, 1597, 100+(row+4)*47),fill=color, width=width)
#Draw header
    draw.line((175,100, 1597,100), fill= color, width=width)
    draw.line((175,100+4*47, 1597,100+4*47), fill= color, width=width)
    draw.line((175+col[1],100+3*47,175+col[3],100+3*47), fill = color, width = width)
    draw.line((175+col[4],100+3*47,175+col[5],100+3*47), fill = color, width = width)
#Draw column 4/5
    col4 = (col[5]-col[4])/4
    for k in range(4):
        draw.line((175+col[4]+k*col4, 100 +3*47,175+col[4]+k*col4, 100+(row+4)*47 ), fill = color, width = width)
        draw.text((175+col[4]+(2*k+1)*col4/2,100+3*47+47/2), header2[k], font= fnt, fill=color, anchor="mm")
#Return
    return img

def Set_Text_Header(img, fnt, fill = "black"):
    draw.text((175+(col[2]+col[1])/2,100+3*47+47/2), "2168", font= fnt, fill=fill, anchor="mm")
    draw.text((175+(col[3]+col[2])/2,100+3*47+47/2), "TT43", font= fnt, fill=fill, anchor="mm")

    for j in range(len(header)):
    # d.text((175+col[1]/2,100+3*47/2), header[0], font= fnt, fill=fill, anchor="mm")
    # d.text((175+(col[2]+col[1])/2,100+3*47/2), header[1], font= fnt, fill=fill, anchor="mm")
    
        dd = header[j].split()
        _,_,h_width, h_height = draw.textbbox((0,0),header[j], fnt)
        s =[]
        g =[]
        if h_width < col[j+1]-col[j]:
            draw.text((175+(col[j+1]+col[j])/2,100+3*47/2), header[j], font= fnt, fill=fill, anchor="mm")
        else:
            for i in dd:
                s.append(i)
                ss = " ".join(s)   
                _,_,text_width, text_height = draw.textbbox((0,0),ss, fnt)
                line = int(h_width/(col[j+1]-col[j]))+1 #số dòng của dữ liệu             
                if text_width > col[j+1]-col[j]: 
                    vs = s.pop()
                    L_1 =" ".join(s)
                    draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)), L_1, font= fnt, fill=fill, anchor="mm")
                    ff = set(s)^set(dd)  
                   
            
            for k in ff:
                H1 = " ".join(ff)
                _,_,h1_width, h1_height = draw.textbbox((0,0),H1, fnt)
                g.append(k)
                gg = " ".join(g)   
                _,_,text_width, text_height = draw.textbbox((0,0),gg, fnt)
                line = int(h_width/(col[j+1]-col[j]))+1 #số dòng của dữ liệu 
                if h1_width < col[j+1]-col[j]:
                    draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)+47),H1 , font= fnt, fill=fill, anchor="mm")       
                else:
                    vs = g.pop()
                    L_2 =" ".join(g)
                    draw.text((175+(col[j+1]+col[j])/2,100+3*47/(line+1)+47), L_2, font= fnt, fill=fill, anchor="mm")
                         
    return img

# Lấy dữ liệu từ file excel
# def Set_content(img, fnt, fill = "black",width = 3):
#     L = 0
#     LT = 0
#     P = 100 + 4*47
#     for a in range(9):
#         row1 = df.iloc[a]
#         r = np.asarray(row1)
#         for i in range(len(r)):
#             if pd.isna(r[i]):
#                 r[i]=" "
#             content = r.tolist()
#         for i in range(len(content)):
#             _,_,c_width, c_height = draw.textbbox((0,0),str(content[i]), fnt)
#             line = int(c_width/(col2[i+1]-col2[i]-16))+1 
#             if line > L:
#                 L = line
#         LT += L  
#         S = L
#         L=0     
#         draw.line((175,P + 47*LT, 1597,P + 47*LT), fill= fill, width=width)
#         for j in col2:
#             draw.line((175+j,100+4*47,175+j, 100+(LT+4)*47), fill = fill, width =width)
#         P = 100+(L+4)*47


#         for j in range(len(content)):
#         # d.text((175+col[1]/2,100+3*47/2), header[0], font= fnt, fill=fill, anchor="mm")
#         # d.text((175+(col[2]+col[1])/2,100+3*47/2), header[1], font= fnt, fill=fill, anchor="mm")
            
#             if j == 3:
#                 dd = str(content[j]).split()
#                 _,_,h_width, h_height = draw.textbbox((0,0),str(content[j]), fnt)
#                 s =[]
#                 g =[]
#                 if h_width < (col2[j+1]-col2[j] - 16):
#                     draw.text((175+col2[j]+16,100+(4+LT-(S-1)-1/2)*47), content[j], font= fnt, fill=fill,anchor = "lm")
#                 else:
#                     for i in dd:
#                         s.append(i)
#                         ss = " ".join(s)   
#                         _,_,text_width, text_height = draw.textbbox((0,0),ss, fnt)
#                         line = int(h_width/(col2[j+1]-col2[j]-16))+1 #số dòng của dữ liệu             
#                         if text_width > col2[j+1]-col2[j]-16: 
#                             vs = s.pop()
#                             L_1 =" ".join(s)
#                             draw.text((175+col2[j]+16,100+(4+LT-(S-1)-1/2)*47), L_1, font= fnt, fill=fill,anchor = "lm")
                            
#                             ff = set(s)^set(dd)  
                        
                    
#                     for k in ff:
#                         H1 = " ".join(ff)
#                         _,_,h1_width, h1_height = draw.textbbox((0,0),H1, fnt)
#                         g.append(k)
#                         gg = " ".join(g)   
#                         _,_,text_width, text_height = draw.textbbox((0,0),gg, fnt)
#                         line = int(h_width/(col2[j+1]-col2[j]-16))+1 #số dòng của dữ liệu 
#                         if h1_width < col2[j+1]-col2[j]:
#                             draw.text((175+col2[j]+16,100+(4+LT-(S-2)-1/2)*47),H1 , font= fnt, fill=fill,anchor = "ls")       
#                         else:
#                             vs = g.pop()
#                             L_2 =" ".join(g)
#                             draw.text((175+col2[j]+16,100+(4+LT-(S-2)-1/2)*47), L_2, font= fnt, fill=fill,anchor = "ls")
#                 continue
            
#             draw.text((175+(col2[j+1] +col2[j])/2 , 100+(4+LT-S+(S/2))*47), str(content[j]), font= fnt, fill=fill,anchor = "mm")
            
#     return img

def Set_content_2(img, fnt,fill = "black",width = 3):    
    L = 0
    col4 = (col[5]-col[4])/4
    ymax_0 = 289
    tree = ET.parse('table.xml')
    root = tree.getroot()
    for i in range(number_row):
        Line = 1
        content_cell_last =[]
        random_cell = random.choice(cell_of_row)
        
        L += random_cell
        P = 100 + (L+4)*47
        draw.line((175,P, 1597,P), fill= fill, width=width)
        for j in col2:
            draw.line((175+j,100+4*47,175+j, 100+(L+4)*47), fill = fill, width =width)
        # Viết STT và TT
        draw.text((175+(col[0]+col[1])/2,100+(L+4)*47-(random_cell/2)*47), str(i+1), font= fnt, fill=fill, anchor="mm")
        draw.text((175+(col[2]+col[3])/2,100+(L+4)*47-(random_cell/2)*47),str(i+1) , font= fnt, fill=fill, anchor="mm")
        # print(random_cell)
        
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
        ymax.text = str(ymax_0 + random_cell*47)

        ymax_0 = ymax_0 + random_cell*47
# viết nội dung các dòng đầu
        while Line < random_cell :           
            
            content_cell = Set_content_for_a_cell(fnt)
            # print(content_cell)
            content_cell.pop()
            content_write = " ".join(content_cell)   
            draw.text((175+col2[3]+16,100+(4+L-(random_cell-Line)-1/2)*47), content_write, font= fnt, fill=fill,anchor = "lm")
            # content_cell = content_next_line
            # print(content_cell)
            Line +=1
#  Viết nội dung dòng cuôi
        for i in range(random.choice(final_word)):
            content_cell_last.append(str(random.choice(content)))
        content_write_last = " ".join(content_cell_last)
        draw.text((175+col2[3]+16,100+(4+L-1/2)*47), content_write_last, font= fnt, fill=fill,anchor = "lm")
# Viết cho các cột ABCD
        for k in range(4):
            draw.text((175+col[4]+(2*k+1)*col4/2,100+(L+4)*47-(random_cell/2)*47), random.choice(check_or_no), font= fnt, fill=fill, anchor="mm")
# Kéo dài chiều sâu của ymax  
    for j in locationInXML:
        # root[j][4][3].text = str(int(root[j][4][3].text) + L*47)
        deep = int(root[j][4][3].text)+ L*47
        root[j][4][3].text = str(deep)
        # print(deep)
# Đổi tên cho hợp form hàng cột
    for j in range(len(locationInXML)-1):
        location = locationInXML[j]
        root[location][0].text = "table column"
# Xóa các class không cần thiết trong thiết lập file header xml
    for object in root.findall('object'):
        name = object.find('name').text
        # print(name)
        if name == "QDUBND theo BYT" or name =="TT":
            root.remove(object)
    tree.write("filename.xml")   
    
    # print(L)
    
    return img
def Set_content_for_a_cell(fnt):
    content_cell = []
    
    text_width = 0
    while text_width < (col2[4]-col2[3] - 16):
        content_cell.append(str(random.choice(content)))
        content_write = " ".join(content_cell)   
        # text_width, text_height = draw.textsize(content_write, fnt)
        _,_,text_width, text_height = draw.textbbox((0,0),content_write, fnt)
    return(content_cell)

#Run 
check = 0
start_time = time.time()
for i in range(number_table):
    img = Image.new("RGB", (1700, 2200), "white")
    draw = ImageDraw.Draw(img)
    img = Draw_table(img, row)
    img = Set_Text_Header(img, fnt)
    # img = Set_content(img, fnt)
    img = Set_content_2(img,fnt)
    tree = ET.parse('filename.xml')
    # tree = ET.ElementTree(root)
    tree.write(f'Table_{i}.xml')
    img.save(f'Table_{i}.png')
    img.show()   
    check += 1
if check == number_table:
    print("Xong")
end_time = time.time()
print("Thời gian hoàn thành code là: ", end_time - start_time)   

    
    
# Save the image to a file
# img.save("table.png")
