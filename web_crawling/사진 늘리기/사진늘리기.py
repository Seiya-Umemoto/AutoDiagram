import cv2
import numpy as np
import sys
import os

# 룩업 테이블의 생성
min_table  =  50 
max_table  =  205 
diff_table  =  max_table  -  min_table

LUT_HC  =  np . arange ( 256 ,  dtype  =  'uint8'  ) 
LUT_LC  =  np . arange ( 256 ,  dtype  =  'uint8'  )

# 경조 LUT 생성
for  i  in  range ( 0 ,  min_table ) : 
    LUT_HC [ i ]  =  0 
for  i  in  range ( min_table ,  max_table ) : 
    LUT_HC [ i ]  =  255  *  ( i  -  min_table )  /  diff_table 
for  i  in  range ( max_table ,  255 ) : 
    LUT_HC [ i ]  = 255

# 로우 콘트라스트 LUT 생성
for  i  in  range ( 256 ) : 
    LUT_LC [ i ]  =  min_table  +  i  *  ( diff_table )  /  10

# 변환
src  =  cv2 . imread ( "carrot/carrot_0001.jpg " ,  1 ) 
high_cont_img  =  cv2 . LUT ( src ,  LUT_HC ) 
low_cont_img  =  cv2 . LUT ( src ,  LUT_LC )

src