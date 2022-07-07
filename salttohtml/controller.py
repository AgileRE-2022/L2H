from .const import *
from .html import *
from .mapper import *
import re

def doConvert(salt):
    result1 = []
    result2 = []
    convert = False
    last_pattern = const_PLAIN_TEXT
    group_id = 0
    containerWidth = 0
    for line in salt:
        if isStartSalt(line):
            convert = True
            print("start")
            continue
        if isEndSalt(line):
            convert = False
            print("finish")
            continue
        if convert:
            if containerWidth <= len(line):
                containerWidth = len(line)
            if isGridView(line):
                gridData = toSplitGrid(line)
                cGrid1 = ""
                cGrid2 = ""
                nGrid  = len(gridData)
                group_id += 1
                for row in gridData:
                    if not isSamePattern(last_pattern, row):
                        group_id += 1
                    html1, html2, pattern = convertSalt2Html(row, group_id)
                    cGrid1 += div%html1 + "\n"
                    cGrid2 += div%html2 + "\n"
                    last_pattern = pattern
                result1.append(gridView1%(nGrid,cGrid1))
                result2.append(gridView2%(nGrid,cGrid2))
                group_id += 1
            else: 
                if not isSamePattern(last_pattern, line):
                    group_id += 1
                html1, html2, pattern = convertSalt2Html(line, group_id)
                last_pattern = pattern
                result1.append(html1)
                result2.append(html2)
    
    return toHtmlString(result1, containerWidth), toHtmlString(result2, containerWidth)

def convertSalt2Html(salt, group_id):
    patt = const_PLAIN_TEXT
    for component, pattern in zip(functions,patterns):
        html1, html2 = component(salt, group_id)
        if html1 != "" and html2 != "":
            patt = pattern
            html1.strip()
            html2.strip()
            return html1, html2, patt
    salt.strip()
    html1,html2 = toPlainText(salt, group_id)
    return html1, html2, patt

def isStartSalt(salt):
    if re.search(re_start_salt, salt):
        return True
    return False

def isEndSalt(salt):
    if re.search(re_end_salt, salt):
        return True
    return False

def isGridView(salt):
    if re.search(re_grid_row, salt):
        return True
    return False

def isButtonSalt(salt):
    if re.search(re_button, salt):
        return True
    return False

def isUncheckedRadioSalt(salt):
    if re.search(re_unchecked_radio, salt):
        return True
    return False

def isCheckedRadioSalt(salt):
    if re.search(re_checked_radio, salt):
        return True
    return False

def isUncheckedBoxSalt(salt):
    if re.search(re_unchecked_box, salt):
        return True
    return False

def isCheckedBoxSalt(salt):
    if re.search(re_checked_box, salt):
        return True
    return False

def isDropListSalt(salt):
    if re.search(re_droplist, salt):
        return True
    return False

def isTextInputSalt(salt):
    if re.search(re_text_input, salt):
        return True
    return False

def isOpenBracketSalt(salt):
    if re.search(re_open_bracket, salt):
        return True
    return False

def isCloseBracketSalt(salt):
    if re.search(re_close_bracket, salt):
        return True
    return False

def isNewLineSalt(salt):
    if re.search(re_new_line, salt):
        return True
    return False

patterns=[
    const_BUTTON,
    const_RADIO,
    const_RADIO,
    const_CHECK_BOX,
    const_CHECK_BOX,
    const_DROP_LIST,
    const_TEXT_INPUT,
    const_OPEN_BRACKET,
    const_CLOSE_BRACKET,
    const_NEW_LINE,
]

funct=[
    isButtonSalt,
    isUncheckedRadioSalt,
    isCheckedRadioSalt,
    isUncheckedBoxSalt,
    isCheckedBoxSalt,
    isDropListSalt,
    isTextInputSalt,
    isOpenBracketSalt,
    isCloseBracketSalt,
    isNewLineSalt,
]

def isSamePattern(last_pattern, salt):
    for do,pattern in zip(funct, patterns):
        if do(salt):
            if pattern != last_pattern:
                return False
            return True
    if last_pattern == const_PLAIN_TEXT:
        return True
    return False