import requests
import plotly.express as px

# API lấy vị trí ISS hiện tại
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

# Lấy tọa độ
pos = data["iss_position"]
lat = float(pos["latitude"])
lon = float(pos["longitude"])

# Vẽ bản đồ
title = "ISS Live Position"
fig = px.scatter_geo(
    lat=[lat],
    lon=[lon],
    title=title
)

fig.show()
