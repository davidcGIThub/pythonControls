import numpy as np
import plotly.plotly as py
from plotly.grid_objs import Grid, Column
import time

x = np.array([1,23,23,4,6])
column_1 = Column(x, 'x')
column_2 = Column([0.5], 'y')
column_3 = Column([1.5], 'x2')
column_4 = Column([1.5], 'y2')

grid = Grid([column_1, column_2, column_3, column_4])
py.grid_ops.upload(grid, 'ping_pong_grid',auto_open=False)
#py.grid_ops.upload(grid, 'ping_pong_grid'+str(time.time()), auto_open=False)
