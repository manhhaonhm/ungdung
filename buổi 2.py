class chunhat:
 def __init__(self, chieu_dai,chieu_rong):
    self.chieu_dai= chieu_dai
    self.chieu_rong= chieu_rong
 def chu_vi(self):
   return(self.chieu_dai + self.chieu_rong) * 2
 def dien_tich(self):
   return(self.chieu_dai * self.chieu_rong)
 
hcn = chunhat(10,5)
print(hcn.chu_vi())
hcn_2 = chunhat(12,36)
print(hcn_2.dien_tich())