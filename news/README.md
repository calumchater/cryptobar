Uses Google Search API to collect news article links from the web

Once articles are collected, do some web scraping and extract the article content

Once content is extracted, do sentiment analysis and publish in db

After publish in DB, send pub to Kafka to say that there is analysis ready to be done by the analysis service