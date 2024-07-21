import pandas as pd

def info(dF):
    correlation_matrix = dF.corr()
    info = pd.DataFrame({"name": dF.columns,
                     "non-nulls": len(dF) - dF.isnull().sum().values,
                     "nulls": dF.isnull().sum().values,
                     "type": dF.dtypes.values,
                     "unique value of feature":dF.nunique(),
                     "corr_target": correlation_matrix["Sales_Revenue"]
                    })
    describe_stats = dF.describe(include='all').transpose()

    info["count"] = describe_stats["count"].values
    info["mean"] = describe_stats["mean"].values if 'mean' in describe_stats else None
    info["std"] = describe_stats["std"].values if 'std' in describe_stats else None
    info["min"] = describe_stats["min"].values if 'min' in describe_stats else None
    info["25%"] = describe_stats["25%"].values if '25%' in describe_stats else None
    info["50%"] = describe_stats["50%"].values if '50%' in describe_stats else None
    info["75%"] = describe_stats["75%"].values if '75%' in describe_stats else None
    info["max"] = describe_stats["max"].values if 'max' in describe_stats else None
    return info
    