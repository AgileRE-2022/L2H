import re
from .const import *
from .html import *
import string
import random
from html5print import HTMLBeautifier

def toHtmlString(data, containerWidth):
    htmlString = "\n".join(data) #convert the generated HTML to a string
    prettyHTML = HTMLBeautifier.beautify(htmlString, 4) #beautify the HTML
    prettyHTML = base%(containerWidth, prettyHTML) #add the base html
    return prettyHTML

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def toConverterPayload(data):
    payload = data.split("\n")
    return payload

def toSplitGrid(data):
    payload = data.split("|")
    return payload

def toButton(salt, group_id):
    saltButton = re.search(re_button, salt)
    if saltButton:
        label = saltButton.group("text").strip()
        width = len(saltButton.group("text"))
        html1 = button1%(width,label)
        html2 = button2%(width,label)
        return html1, html2
    return "",""

def toPlainText(salt, group_id):
    html1 = plainText1%salt
    html2 = plainText2%salt
    return html1, html2\

def toUncheckedRadio(salt, group_id):
    saltUncheckedRadio = re.search(re_unchecked_radio, salt)
    if saltUncheckedRadio:
        id = id_generator()
        html1 = uncheckedRadio1%(group_id, id, id, saltUncheckedRadio.group("text"))
        html2 = uncheckedRadio2%(group_id, id, id, saltUncheckedRadio.group("text"))
        return html1, html2
    return "",""    

def toCheckedRadio(salt, group_id):
    saltCheckedRadio = re.search(re_checked_radio, salt)
    if saltCheckedRadio:
        id = id_generator()
        html1 = checkedRadio1%(group_id, id, id, saltCheckedRadio.group("text"))
        html2 = checkedRadio2%(group_id, id, id, saltCheckedRadio.group("text"))
        return html1, html2 
    return "",""   

def toUncheckedBox(salt, group_id):
    saltUncheckedBox = re.search(re_unchecked_box, salt)
    if saltUncheckedBox:
        id = id_generator()
        html1 = uncheckedBox1%(id, id, saltUncheckedBox.group("text"))
        html2 = uncheckedBox2%(id, id, saltUncheckedBox.group("text"))
        return html1, html2 
    return "",""   

def toCheckedBox(salt, group_id):
    saltCheckedBox = re.search(re_checked_box, salt)
    if saltCheckedBox:
        id = id_generator()
        html1 = checkedBox1%(id, id, saltCheckedBox.group("text"))
        html2 = checkedBox2%(id, id, saltCheckedBox.group("text"))
        return html1, html2 
    return "",""

def toDropList(salt, group_id):
    saltDropList = re.search(re_droplist, salt)
    if saltDropList:
        label = saltDropList.group("text").strip()
        width = len(saltDropList.group("text"))
        html1 = dropList1%(width,label)
        html2 = dropList2%(width,label)
        return html1, html2 
    return "",""

def toInputText(salt, group_id):
    saltInputText = re.search(re_text_input, salt)
    id = id_generator()
    if saltInputText:
        label = saltInputText.group("text").strip()
        width = len(saltInputText.group("text"))
        html1 = inputText1%(id, width,label)
        html2 = inputText2%(id, width,label)
        return html1, html2
    return "",""

def toDivOpen(salt, group_id):
    saltDivOpen = re.search(re_open_bracket, salt)
    if saltDivOpen:
        return divOpen, divOpen
    return "",""

def toDivClose(salt, group_id):
    saltDivClose = re.search(re_close_bracket, salt)
    if saltDivClose:
        return divClose, divClose
    return "",""

def toBlankLine(salt, group_id):
    saltNewLine = re.search(re_new_line, salt)
    if saltNewLine:
        html = newLine
        return html, html
    return "",""

functions=[
    toButton,
    toCheckedRadio,
    toUncheckedRadio,
    toCheckedBox,
    toUncheckedBox,
    toDropList,
    toInputText,
    toDivOpen,
    toDivClose,
    toBlankLine,
]
