import dash_html_components as html


from app import app

def get_image():
    

    image = html.Div(html.Img(src=app.get_asset_url('image.png'), width="80%"))

    return image