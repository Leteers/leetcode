# from datetime import datetime
# from pytz import timezone

# timestamp = int(datetime.now(timezone("Europe/Moscow")).timestamp())

# print(timestamp)

# 1_744_629_262
# 2_147_483_647

is_lexo = lambda x: [True if x[i]<x[i+1] else False for i in range(len(x) - 1)]

print(all(is_lexo(["xc","yb","za"])))