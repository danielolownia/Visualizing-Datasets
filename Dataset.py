import pandas as pd
import matplotlib.pyplot as plt

#first graph
df = pd.read_csv("/Users/danielolownia/Documents/MINIMUM_WAGES.csv")
df["2017"] = pd.to_numeric(df["2017"])

top10 = df.sort_values("2017", ascending=False).head(10)

plt.bar(top10["Country"], top10["2017"])
plt.xticks(rotation=45, ha="right")

plt.title("Top 10 Countries by Minimum Wage in 2017")
plt.xlabel("Country")
plt.ylabel("Minimum Wage (Dollars)")

plt.tight_layout()
plt.show()


#second graph
top5_countries = top10["Country"].head(5)

years = [col for col in df.columns if col.isdigit() and 2000 <= int(col) <= 2017]

growth = df[df["Country"].isin(top5_countries)][["Country"] + years]
growth = growth.set_index("Country").T
growth = growth.apply(pd.to_numeric) 
growth.plot(marker='o')

plt.title("Minimum Wage Growth from 2000-2017 for Top 5 Countries")
plt.xlabel("Year")
plt.ylabel("Minimum Wage (Dollars)")

plt.tight_layout()
plt.grid(True)
plt.show()
