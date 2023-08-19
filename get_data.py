import requests
import pandas as pd
#url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0N2FhM2FkNzQxMzI3ODNhMjM5NmI0ZDA1MzA3NWZhNSIsInN1YiI6IjY0YTY4MWE2MDdmYWEyMDExZTAzMTNlNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tkYBnPdTVrKAqUOPXL5Z3Piud1_1OvURSgBeI_28qpc"
}

#response = requests.get(url, headers=headers)

# df=pd.DataFrame(response.json()["results"])
# df=df[['id','title','release_date','original_language','vote_average','vote_count']]
# print(df)
# df.to_csv("top_movies.csv",index=False)

df=pd.DataFrame()

for i in range(1,2):
  response = requests.get("https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={}".format(i), headers=headers)
  df_temp=pd.DataFrame(response.json()["results"])
  df_temp2=df_temp[['id','title','release_date','original_language','vote_average','vote_count']]
  df=pd.concat([df,df_temp2])

df.to_csv("top_movies.csv",index=False)  