import re
import string
import string

def clean_text(text):
    
    cleaned_text = text.strip()
    
    # Thay một hoặc nhiều khoảng trắng bằng -
    cleaned_text = re.sub('\s+','- ', cleaned_text)
    
    # Chuyển " +++++++ " thành  ""
    cleaned_text = re.sub('\++', '', cleaned_text)
    
    # Xóa hết xuống dòng
    cleaned_text = re.sub('\n+', '', cleaned_text)
    
    # cleaned_text = re.sub('^[A-Za-z]', '-', cleaned_text)
    if cleaned_text[0] in string.ascii_letters or cleaned_text[0] in string.ascii_uppercase:
        cleaned_text = '-{}'.format(cleaned_text)
        
    
    return cleaned_text