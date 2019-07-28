data = [] #空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1 # 意思同count += 1
		if count % 1000 == 0: # %求餘數 除1000餘數=0
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

#OPEN=開啟 reviews.txt檔案  r=讀取  as=當作   
#with= 自動close  離開with的架構 (4.5行=with架構)

#data的  append=加入功能 +到line裡

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:          #把清單中的東西一個一個拿出來
	if len(d) < 100:    #date=100萬筆資料 d=篩出來的2萬筆資料
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])