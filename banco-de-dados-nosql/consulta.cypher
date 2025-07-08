-- Criação do nó de identificação do projeto/aluno
MERGE (:Project {id: "projeto-nosql-2025"});

-- Carregamento e ingestão dos dados dos tweets a partir de arquivos JSON
CALL apoc.load.directory("*.json") YIELD value
CALL apoc.load.json(value) YIELD value AS jsonData
UNWIND jsonData.data AS tweet_data 

MERGE (t:Tweet {id_tuite: tweet_data.id})
ON CREATE SET
  t.text = tweet_data.text,
  t.created_at = tweet_data.created_at,
  t.source = tweet_data.source,
  t.lang = tweet_data.lang,
  t.conversation_id = tweet_data.conversation_id,
  t.like_count = tweet_data.public_metrics.like_count,
  t.reply_count = tweet_data.public_metrics.reply_count,
  t.retweet_count = tweet_data.public_metrics.retweet_count,
  t.quote_count = tweet_data.public_metrics.quote_count,
  t.project_id = "projeto-nosql-2025"

MERGE (u:User {user_id: tweet_data.author_id})
MERGE (u)-[:POSTED]->(t)

FOREACH (hash IN tweet_data.entities.hashtags |
  MERGE (h:Hashtag {tag: apoc.text.clean(toLower(hash.tag))})
  MERGE (t)-[:HAS_HASHTAG]->(h)
)

FOREACH (mention IN tweet_data.entities.mentions |
  MERGE (mu:User {user_id: mention.id})
  ON CREATE SET mu.username = mention.username
  MERGE (t)-[:MENTIONS]->(mu)
)

FOREACH (ref_tweet IN tweet_data.referenced_tweets |
  SET t.tipo_ref = ref_tweet.type, t.id_ref = ref_tweet.id
);


-- Refinamento dos labels dos tweets com base no tipo de referência
MATCH (t:Tweet) WHERE t.tipo_ref = "retweeted"
REMOVE t:Tweet SET t:Retweet;

MATCH (t:Tweet) WHERE t.tipo_ref = "replied_to"
REMOVE t:Tweet SET t:Replied;

MATCH (t:Tweet) WHERE t.tipo_ref = "quoted"
REMOVE t:Tweet SET t:Quoted;


-- Consulta 1: Hashtag mais popular e uma amostra de tweets relacionados
MATCH (h:Hashtag)<-[:HAS_HASHTAG]-(t:Tweet)
WHERE t.project_id = "projeto-nosql-2025"
WITH h, count(t) AS contagem
ORDER BY contagem DESC
LIMIT 1

MATCH (h)<-[:HAS_HASHTAG]-(relatedTweet:Tweet)
MATCH (p:Project {id: "projeto-nosql-2025"})
RETURN h, p, collect(relatedTweet)[..10] as sampleTweets;


-- Consulta 2: Usuário que mais deu retweets e uma amostra de seus retweets
MATCH (u:User)-[:POSTED]->(rt:Retweet)
WHERE rt.project_id = "projeto-nosql-2025"
WITH u, count(rt) AS retweetCount
ORDER BY retweetCount DESC
LIMIT 1

MATCH (u)-[r:POSTED]->(t:Retweet)
MATCH (p:Project {id: "projeto-nosql-2025"})
RETURN u, t, r, p
LIMIT 10;
