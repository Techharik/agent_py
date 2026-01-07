# What is a LLM?

# Chat gpt - chat with a gpt - gpt - llm - large language model.

# llm - Training the data - give the response.

# We need to talk to the system in a structured way . Understand the natural language and generate the natural language.

# Deep Dive into the GPT:

# Input tokens - client query given to the llm
# Output Token - llm sends a response.

# GPT- Generative pretrained Transformer.
# Generative - Generate a output for the reponse.(Its not searching it generate it creates it own.)
# Pretrained - It generate the pretrained model based on the pretrained data.
# Transformer -Reality (It transforms to Genrativie based on pretrained model)

# How the LLMS work under the Hood
# Transformer -- model artitectures -

# Sequence Input ---> Transformer ---> Out sequence
#                  (Google translate)
# English       ---> Transformer ---> Tamil
# (Google Translate)

# Gpt -For every input token it generate the next one token
# input token ----> Transformer ----> Predict the next Token
#                     GPT
# hI tHERE    ---->            -----> hello
# hi there hello ---->         -----> I am fine
# Hi there hello I am fine ----> -----> <ENd>
#Internals of working

# Input token go with the output token for every returns

# if i ask for the hi there , pretict the token with hey then again itrate with hey hari then again itrate with , how are you.
# Hi there ----> Hey hari, how are you ---> 3 token 3 iteration happen.
# So in normal senerio it takes more iterations that y it is CPU intensive task so we need the GPU.

# So  a Transformer which used to predict the next token to send the generative response using the pretrained model

#Fundamental of Tokenization in NLP

# Token - The charachter that human are mapped to some numbersis known as token .

#  a-1, b-2 , c-3 -- Do if we give abc the transformers able to predict the token 4 which is D

# Tokenizer Vercel.com --
# Hey their , my name is hari - 17 token .

# Tokenization - converting the user input to set of number is know as tokenizations.
# Query - numbers -token - llm -transformers - predict the next token - Detokenization - send to client.

# Everymodel has their own way of tokenization and detokenization.

# Implemention a custom tokenizer in python.

# tiktoken --- helps to tokenize and detokenize by open ai
# create a tokenizer and untokenizer using this Package.

# Google Papper on Attention.

# Machine Leraning - creating a llm (Math)(Research work)
# Developer        - Solving business problems (application development.)

# What is Vector Embedddings :

# How to write a code to make the machine understand the codings.
# Vector Embeddings - gives the simentatic meanings. numberial represenatin of text and images which has a relations.

# FIRST PRINCIPLE - basically kind a mapping where the catgeroized data interconnected with each other.3D

# Position Encoding.

# HI THERE, HOW ARE YOU

# STEP : 1 --- CRETAE A TOKEN 25 2372 26 6821 681 902
# STEP :2  --- vector emeddings[] []  []  []  []  []
# STEP:3 ----  add position    0   1  2    3  4  5  -- add the position to that  on what order direction we have
# Self Attention --- based on the vector emmbedding the meaning can change
# Multiple Attention --- see through multiple possiblity.
# Feed forward      --- Propability predictions
# Linear -- gives example 10 prediction --
#  softmax pic the most relatable things.
