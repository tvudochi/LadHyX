from django.template import Library, Node, TemplateSyntaxError

register = Library()

@register.filter(name='range')
def filter_range(start, end):
	return range(start, end+1)
