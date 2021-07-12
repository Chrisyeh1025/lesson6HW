name_list = ['Bob','Chris','Emily','Andy','Vanessa']
score_list = [80, 90, 75, 65, 100]
i = int(input('總共有幾個分數'))
i = int(i)
max = 0
max_name = ''
for s in score_list:
    if s > max:
        max = s
min = 101
for s in score_list:        
    if s < min:
        min = s
print('max=',max, 'min=',min)    
    
 

