import pandas as pd

data = []
for page in range(1, 20000):
    print("Page %d" % page)

    url = 'http://www.salarii-it.ro/salarii?page=%d' % page
    df = pd.read_html(url, header=0)
    if len(df) == 1 and not df[0].empty:
        data.append(df[0])
    else:
        break

df_data = pd.concat(data)
df_data.to_csv('data.csv')
