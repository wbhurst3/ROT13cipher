import webapp2
import cgi

form = """
<div style="width:960px;height:960px;padding:20px;">
<form method="post">
	<p style="align:left;margin:0px;">Enter some text to <b>ROT13</b>:</p><br>
	<textarea name='text' style="align:left;width:200px;height:50px;">%(result)s</textarea><br>
	<input style="margin-top:5px;width:200px;height:40px;" type='submit'>
</form>
</div>
"""

rot_indexes = {
	'0':13,
	'1':14,
	'2':15,
	'3':16,
	'4':17,
	'5':18,
	'6':19,
	'7':20,
	'8':21,
	'9':22,
	'10':23,
	'11':24,
	'12':25,
	'13':0,
	'14':1,
	'15':2,
	'16':3,
	'17':4,
	'18':5,
	'19':6,
	'20':7,
	'21':8,
	'22':9,
	'23':10,
	'24':11,
	'25':12
}

lower_list = 'abcdefghijklmnopqrstuvwxyz'
upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotted(s):
	new_string = ""
	for i in s:
		if i.isupper():
			f = upper_list.index(i)
			i = upper_list[rot_indexes[str(f)]]
			new_string += i
		elif i.islower():
			f = lower_list.index(i)
			i = lower_list[rot_indexes[str(f)]]
			new_string += i
		else:
			new_string += i
	return new_string

class ROT13(webapp2.RequestHandler):
    def get(self):
    	self.write_form(result="")

    def post(self):
    	result = self.request.get('text')
        if result:
        	result = rotted(result)
        	result = cgi.escape(result, quote = True)
        	self.write_form(result)
        else:
        	self.response.out.write(form)

    def write_form(self, result=""):
    	self.response.out.write(form % {'result':result})

application = webapp2.WSGIApplication([
    ('/', ROT13),
], debug=True)






