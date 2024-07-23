from dataset import ecom_sales_new
import plotly.express as px

bar_fig = px.bar(
    data_frame=ecom_sales_new
    x='Total Sales $',
    y='Country',
    orientation="h",
    # 3:40
)
