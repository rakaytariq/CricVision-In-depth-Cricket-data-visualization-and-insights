
import numpy as np
import pandas as pd
from plots.pitch_heatmap import pitch_heatmap
import matplotlib
import numpy as np
import pandas as pd
from plots.pitch_densitymap import pitch_densitymap


def generate_plots():
    # Import Steve Smith data
    df = pd.read_csv('data/ssmith_ashes_2019.csv')

    # Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX and stumpsX for plotting
    df['pitchX'] = -df['pitchX']
    df['stumpsX'] = -df['stumpsX']

    xy = np.array(df[['pitchX', 'pitchY']])
    runs = df.batterRuns

    title = 'Steve Smith'
    subtitle_1 = 'Series Batting Strike Rate Zones | Ashes 2019 | 1England'
    subtitle_2 = 'From {0} balls faced with tracking enabled | Minimum 12 balls per zone'.format(len(xy))
    legend_title = 'Strike Rate'

    result = pitch_heatmap(xy, runs, title, subtitle_1, subtitle_2, legend_title, measure='strike_rate')
    result.show()



    # Import Moeen Ali data
    df = pd.read_csv('data/moeen.csv')

    # Hawkeye Data has Y co-ord as meters from stumps towards bowler, so need to flip pitchX and stumpsX for plotting
    df['pitchX'] = -df['pitchX']
    df['stumpsX'] = -df['stumpsX']

    # Filter to balls with tracking enabled
    balls = df[df['pitchY'] > 0]

    # Split balls for RHB and LHB and select pitch co-ords
    xy_rh = np.array(balls[balls.rightHandedBat == True][['pitchX', 'pitchY']])

    title = 'Moeen Ali'
    subtitle_1 = 'Deliveries to Right-handers'
    subtitle_2 = 'ICC Cricket World Cup 2015 | vs Australia | 14-02-2015'

    result = pitch_densitymap(xy_rh, title=title, subtitle_1=subtitle_1, subtitle_2=subtitle_2)
    result.show()
if __name__ == "__main__":
    generate_plots()


