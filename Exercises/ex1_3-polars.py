import polars as pl

from Exercises.pcost import read_portfolio

raw_list = read_portfolio('Data/portfolio.dat')

# Convert the list to a polars DataFrame
df = pl.DataFrame(raw_list)

# sort df by descending total_cost and
# convert name to a factor
df = df.sort('total_cost', descending=True)
df = df.with_columns(pl.col("name").cast(pl.Categorical))

df.select(pl.sum("total_cost"))

import plotnine as p9

# plot df
# reorder the plot by descending total_cost

(p9.ggplot(df, p9.aes(x='name', y='total_cost'))
  + p9.geom_col()
  + p9.theme_minimal()
  + p9.labs(x='Portfolio', y='Total Cost', title='Portfolio Cost')
  + p9.theme_bw())
    
plot.draw()

plot2 = p9.ggplot(df, p9.aes(x='name', y='total_cost')) \
    + p9.geom_point() \
    + p9.labs(title='Portfolio') \
    + p9.theme_bw()


plot2.draw()

    
plot.draw()

p9.reorder()

