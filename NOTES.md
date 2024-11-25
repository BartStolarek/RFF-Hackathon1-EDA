Team 6

@zaemis
@Ivanos - M.I.A.

# start Jupyter notebook
docker run -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/base-notebook

# General Thoughts - @zaemis
As an engineer whose prior experience focused so heavily on  web technologies
and databases, answering questions like "What are the top 10 most streamed
songs on Spotify?" with Pandas feels strange. Compare:

df[['Track', 'Stream']].sort_values(by='Stream', ascending=False).head(10)

SELECT TOP 10 Track, Stream FROM Spotify ORDER BY Stream DESC

And this is just a simple query. Things get more convoluted when needing
to calculate values using multiple columns.

Sure, I "gotta learn this" because that's the way the data world works, and
luckily I have tools like ChatGPT that can help me fake it until I make it,
but curious whether the experiences that shape how I approach problem solving
will be a hinderance (difficulty with tooling) or a help (different
perspective)? Hooray, self doubt!

