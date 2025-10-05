# RAG - PROBLEM STATMENT .
# RAG - Its a framework that combines the llm with External data.

# PREMATURE RAG.

# pdf -- Text  --- SYSTEM PROMPT --- INPUT AND OUTPUT

# PROBLEMS:
# COST
# CONTEXT WINDOE(1M TOKEN WINDOW) lIMITED , WE CANNOT INGEST A ALL DATA

# RAG PIPLINE:
'''
 1. INFDEXING PHASE - PROVIDE THE DATA.
 2. RETRIVAL PHASE -- CHATTING WITH DATA.

INDEXING Phase:
user gave a lot of data  --- chunking (split it into smaller peaces) ---> Embedding  model ---> vector embeddings ---> stored in vector database(chunk and   vectors) 

Retrival Phase :
user - query - vector embeddings - Embedding Models -- Vector embedding (query) --> Vector similarty search in db - got the relvent chucks from the dbs (vector - content) --> Pass the data to the system prompt.  -- lllm - user query data it return output 
'''

# WE Need Vector database. - pinecone -weaviate - chromadb - pgvector -qdrant db

# Qdrant
# LangChain - Having all the abstract code we can use the prebuild functions.
