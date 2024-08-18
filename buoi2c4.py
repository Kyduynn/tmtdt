# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

distance = float(input("Nhập độ dài đoạn đường đến trường (m): "))
 
if distance > 1200:
    print("Đường đến trường xa quá. ")
else:
    print("Không xác định được xa-gần. ")
      
    
distance = float(input("Nhập độ dài đoạn đường đến trường(m): "))

if distance < 300:
    print("Đường đến trường gần quá. Thôi! Đi bộ")
elif distance > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print("Không xác định")