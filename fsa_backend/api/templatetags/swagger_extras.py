from urllib.parse import urlencode

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def fields_beautify(title, fields):
    if fields:
        ul_content = ""
        if "ordering" in title:
            fields += ["-" + field for field in fields]
        for field in fields:
            if isinstance(field, tuple):
                ul_content += "<li><code>%s</code> - <b>%s</b> </li>" % field
            else:
                ul_content += "<li><code>%s</code></li>" % field
        result = "<h3>%s:</h3><ul>%s</ul>" % (title, ul_content)
        return mark_safe(result)
    else:
        return mark_safe("")


@register.simple_tag
def url_query_example(path, query):
    query_encoded = "?" + urlencode(query) if query else ""
    if path:
        result = "<hr><h3>URL Example:</h3><pre class=\"example microlight\">/%s%s</pre>" % ("/".join(path) + "/", query_encoded)
        if query:
            result += "<h3>Query example decoded:</h3><pre class=\"example microlight\">%s</pre>" % str(query)
        return mark_safe(result)
    else:
        return mark_safe("")


@register.simple_tag(takes_context=True)
def return_fields(context):
    result = ""
    for key, value in context.flatten().items():
        if "return" in key:
            if key is not "returns":
                name = "_".join(key.split("_")[1:-1])
                title = "Returns fields for <code>%s</code>" % name
            else:
                title = "Returns"
            result += fields_beautify(title=title, fields=value)
    if result:
        return mark_safe("<hr>" + result)
    else:
        return mark_safe("")
