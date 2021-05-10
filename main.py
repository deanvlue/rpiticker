from PIL import Image, ImageDraw, ImageFont
import requests

img = Image.new('RGB', (480,320),color = (0, 0, 0))
btc_color = (0,255,0)
ltc_color = (0,255,0)

fnt = ImageFont.truetype('./fonts/Roboto-Bold.ttf', 55)
fntPrice = ImageFont.truetype('./fonts/Roboto-Bold.ttf', 35)

# consulta precio de bitcoin
btc_mxn = requests.get("https://api.bitso.com/v3/ticker/?book=btc_mxn")
if btc_mxn.ok:
  btc = "${:,.2f} MXN".format(float(btc_mxn.json()['payload']['last']))
  btc_change = float(btc_mxn.json()['payload']['change_24'])
ltc_mxn = requests.get("https://api.bitso.com/v3/ticker/?book=ltc_mxn")
if ltc_mxn.ok:
  ltc = "${:,.2f} MXN".format(float(ltc_mxn.json()['payload']['last']))
  ltc_change = float(ltc_mxn.json()['payload']['change_24'])

if btc_change < 0:
  btc_color = (255,0,0)


if ltc_change < 0:
  ltc_color = (255,0,0)
  


d = ImageDraw.Draw(img)
d.text((10,5), "BTC: ", fill=btc_color, font=fnt)
d.text((10,80), btc , fill=btc_color, font=fntPrice)

d.text((10,160), "LTC: ", fill=ltc_color, font=fnt)
d.text((10,230), ltc , fill=ltc_color, font=fntPrice)

img.save('ticker.png')

