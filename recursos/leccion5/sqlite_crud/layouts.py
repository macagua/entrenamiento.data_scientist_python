""" Streamlit Layout Templates """

### "Header" Section #############################################################
BLOG_HEADER_HTML_TPL = """
<div style="background-color:{div_bg_color};padding:10px;border-radius:10px">
  <h1 style="color:{h1_color};text-align:center;">{app_title}</h1>
</div>
"""

### "Home" Item Menu ##############################################################
HOME_ENTRIES_HTML_TPL = """
<div style="background-color:{div_bg_color};padding:10px;border-radius:5px;margin:10px;">
  <h4 style="color:white;text-align:center;">{title}</h4>
  <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align:middle;width:50px;height:50px;border-radius:50%;"/>
  <h5 style="color:white;">Author: {author}</h5>
  <h6 style="color:white;">Post Date: {date}</h6>
  <p style="background-color:silver;color:black;text-align:justify">{content}...</p>
</div>
"""

# ENTRY_TITLE_HTML_TPL = """
# <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
#   <h4 style="color:white;text-align:center;">{title}</h4>
#   <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align:middle;float:left;width:50px;height:50px;border-radius:50%;"/>
#   <h5 style="color:white;">Author: {author}</h5>
#   <br/>
#   <p style="color:black;text-align:justify">{content}...</p>
# </div>
# """

### "View Posts / Search..." Item(s) Menu ########################################
ENTRY_DETAILS_HTML_TPL = """
<div style="background-color:{div_bg_color};padding:10px;border-radius:5px;margin:10px;">
  <h4 style="color:white;text-align:center;">{title}</h4>
  <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align:middle;float:left;width:50px;height:50px;border-radius:50%;"/>
  <h5 style="color:white;">Author: {author}</h5>
  <h6 style="color:white;">Post Date: {date}</h6>
</div>
"""

### "View Posts / Search..." Item(s) Menu ########################################
ENTRY_CONTENT_MSG_HTML_TPL = """
<div style="background-color:silver;overflow-x:auto;padding:10px;border-radius:5px;margin:10px;">
  <p style="text-align:justify;color:black;padding:10px">{content}</p>
</div>
"""

### "Home / View Posts / Manage Blog" Item(s) Menu ###############################
NOTFOUND_ENTRY_MSG_HTML_TPL = """
<div style="background-color:{div_bg_color};padding:10px;border-radius:5px;margin:10px;">
  <h4 style="color:white;text-align:center;">Not article items found!!!</h4>
  <p style="color:white;text-align:center;">Please go to 'Add Posts' form to add an blog article entry</p>
</div>
"""

### "Search..." Item(s) Menu #####################################################
NOTFOUND_SEARCH_MSG_HTML_TPL = """
<div style="background-color:{div_bg_color};padding:10px;border-radius:5px;margin:10px;">
  <h4 style="color:white;text-align:center;">Not article items found!!!</h4>
  <p style="color:white;text-align:center;">Try with other Search criteria</p>
</div>
"""
