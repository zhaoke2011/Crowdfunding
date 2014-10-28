#coding:utf-8
import sys,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crowdfunding.settings")
import inspect
from django.conf import settings
from django.db import models
from django.template import Context,Template



template = '''
	<html>        
		<head>
			<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
			<title>Data table schema document</title>
			<style type="text/css">
				.loopeven {background:#f1f1f1;}
				.loopodd {}
			</style>
		</head>
		<body>
			{%for model,fields in models%}
			<p style="clear:both; margin-top:40px; display:inline;">
				<table border="0" width="100%">
					<tbody>
						<tr>
							<td colspan="4" style="border:1px solid #000;">
								<b>Model Name: {{model|safe}}<b>
							</td>
						</tr>
						<tr style="background:#000; color:#fff;">
							<th width="15%">列名</th>
							<th width="15%">简称</th>
							<th width="15%">列类型</th>
							<th>描述</th>
						</tr>
						{%for field in fields%}
						<tr style="background:#{%cycle 'f1f1f1' 'ffffff'%}">
							<td>{{field.name}}</td>
							<td>{{field.verbose_name}}</td>
							<td>{{field.class_name}}
								{%if field.related_name%}
									({{field.related_name}})
								{%endif%}
							</td>
							<td>{{field.help_text}}</td>
						</tr> 
						{%endfor%}
					</tbody>
				</table>
			</p>
			{% endfor %}
			<p style="margin-top:50px; padding:10px; width:100%;text-align:center;">
				this document generated by scott
				<a href="http://www.congyuandong.cn"> django-m2doc</a>
			</p>
		</body>
	</html>
	'''
						
def get_propertys(cls):
	fields = []
	#print cls.verbose_name_plural
	for f in cls._meta.fields:
		setattr(f, 'class_name', f.__class__.__name__)
		if hasattr(f, 'related'):
			setattr(f, 'related_name', f.related.parent_model.__name__)
		fields.append(f)
	#print fields
	return fields

def main():    
	mod_list = []
	model_list = []
	for app in settings.INSTALLED_APPS:
		mod_list.append('%s.%s' % (app, 'models'))
	modules = map(__import__, mod_list)
	#print modules
	for s_model in mod_list:
		for member in inspect.getmembers(sys.modules[s_model], predicate=inspect.isclass):
			name,obj=member
			module_name = inspect.getmodule(obj).__name__
			#print sys.modules[s_model]._meta
			#print module_name         
			if module_name.startswith('qdinvest'):
				#print module_name
				#print obj._meta.verbose_name_plural
				model_list.append((obj._meta.verbose_name_plural, get_propertys(obj)))

	print model_list
	if model_list:
		t = Template(template)
		c = Context({'models':model_list})
		html = t.render(c)
		html_file = open('models_doc.html', 'w+')
		html_file.write(html.encode('utf-8'))
		html_file.close()

if __name__ == '__main__':
	main()