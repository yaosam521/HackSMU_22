def latestCrime():
  # !pip3 install sodapy
  # !pip3 install socrata-py
  from socrata.authorization import Authorization
  from socrata import Socrata
  from sodapy import Socrata
  import pandas as pd
  #authorization
  auth = Authorization(
    "",
    "ay6ucx8w0pkf3wpblrvah7zfq",
    "22m1ry5evkqtlnigmf79s79spk2r7rv04s3ewbwv38gvcjx9lf"
  )
  #client to connect
  client = Socrata(
          "www.dallasopendata.com",
          "JEh8Dh72mlqeCbRYUcSq5CVbQ",
          timeout=10
      )
  #Store results from GET Request
  results = client.get("9fxf-t2tr")

  #Sort through to find the latest crime
  df_dallaspd = pd.DataFrame.from_records(results)
  df_dallaspd=df_dallaspd.sort_values(by=['date', 'time'], ascending=False)
  latest_crime = df_dallaspd.iloc[0]
  return latest_crime