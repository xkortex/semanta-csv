import pandas as pd

# df = pd.DataFrame()
#
# df.to_csv()
# pd.read_csv()

class MantaFrame(pd.DataFrame):
    """
    MantaFrame is a hybrid of a Pandas DataFrame and a Semanta semantic graph object
    """
    def __init__(self, data=None, index=None, columns=None, dtype=None,
                 copy=False):
        super(MantaFrame, self).__init__(data=data, index=index, columns=columns, dtype=dtype, copy=copy)