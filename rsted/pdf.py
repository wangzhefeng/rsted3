from rst2pdf.createpdf import RstToPdf
import codecs
utf8codec = codecs.lookup('utf-8')

from flask import current_app


from io import BytesIO

def rst2pdf(content, theme=None):
    topdf = RstToPdf(basedir=current_app.config.root_path, breaklevel=0)
    buf = BytesIO()

    if not content:
        content = '\0'
    content_utf8 = utf8codec.encode(content)[0]
    topdf.createPdf(text=content_utf8, output=buf, compressed=False)

    return buf.getvalue()
