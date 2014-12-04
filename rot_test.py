rot_indexes = {
    '0':14,
	'1':15,
	'2':16,
	'3':17,
	'4':18,
	'5':19,
	'6':20,
	'7':21,
	'8':22,
	'9':23,
	'10':24,
	'11':25,
	'12':0,
	'13':1,
	'14':2,
	'15':3,
	'16':4,
	'17':5,
	'18':6,
	'19':7,
	'20':8,
	'21':9,
	'22':10,
	'23':11,
	'24':12,
	'25':13
}

lower_list = 'abcdefghijklmnopqrstuvwxyz'
upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotted(s):
    for i in s:
		if i.isupper():
			f = upper_list.index(i)
			i = upper_list[str(rot_indexes[str(f)])]
			return i
		elif i.islower():
			f = lower_list.index(i)
			i = lower_list[str(rot_indexes[str(f)])]
			return i
		else:
			return i
    return s