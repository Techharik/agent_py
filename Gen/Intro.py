# What is a LLM?

# Chat gpt - chat with a gpt - gpt - llm - large language model.

# llm - Training the data - give the response.

# We need to talk to the system in a structured way . Understand the natural language and generate the natural language.

# Deep Dive into the GPT:

# Input tokens - client query given to the llm
# Output Token - llm sends a response.

# GPT- Generative pretrained Transformer.
# Generative - Generate a output for the reponse.(Its not searching it generate it creates it own.)
# Pretrained - It generate the pretrained model based on the pretrained model.
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

# Input token go with the output token for every returns

# if i ask for the hi there , pretict the token with hey then again itrate with hey hari then again itrate with , how are you.
# Hi there ----> Hey hari, how are you ---> 3 token 3 iteration happen.
# So in normal senerio it takes more iterations that y it is CPU intensive task so we need the GPU.

# So  a Transformer which used to predict the next token to send the generative response using the pretrained model

#Fundamental of Tokenization in NLP

# Token - the charachter that human are mapped to some numbersis known as token

#  a-1, b-2 , c-3 -- do if we give abc the transformers able to predict the token 4 which is D

# Tokenizer Vercel.com --
# Hey their , my name is hari - 17 token

# Tokenization - converting the user input to set of number is know as tokenizations.
# Hey there - numbers -token - llm -transformers - predict the next token - Detokenization - send to client.

# Everymodel has their own way of tokenization and detokenization.

# Implemention a custom tokenizer in python.

# tiktoken --- helps to tokenize and detokenize by open ai
# create a tokenizer and untokenizer using this Package.

# Google Papper on Attention.
