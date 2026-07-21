# backend/Abstract.py
import sys
import os
import warnings
import logging
import numpy as np

# Suppress warnings
warnings.filterwarnings('ignore')
logging.getLogger("transformers").setLevel(logging.ERROR)

from sklearn.metrics.pairwise import cosine_similarity

# Import the pre-loaded model
from backend.BERTLoader import tokenizer, model

def Abstraction(data):
    """Abstract the input text to a shorter, more concise version"""
    
    # If model failed to load, return truncated data
    if model is None or tokenizer is None:
        return data[:max(1, len(data) - 1)]
    
    def get_sentence_embedding(sentence):
        # Return a zero vector for very short/empty sentences
        if not sentence or len(sentence.strip()) < 2:
            return np.zeros(model.config.hidden_size)
        
        try:
            inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
            return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        except:
            return np.zeros(model.config.hidden_size)

    # Ensure data is a string and handle very short inputs
    data = str(data).strip()
    if len(data) <= 1:
        return ""

    # Split the input data into sentences
    sentences = [s.strip() for s in data.replace('\n', ' ').split('.') if s.strip()]

    if not sentences:
        return data[:max(1, len(data) - 1)]

    doc_embedding = get_sentence_embedding(data)

    # Get embeddings for each valid sentence
    sentence_embeddings = []
    valid_sentences = []
    for s in sentences:
        if len(s.strip()) > 1:
            emb = get_sentence_embedding(s)
            if not np.all(emb == 0):  # Only add if embedding is valid
                sentence_embeddings.append(emb)
                valid_sentences.append(s)
    
    if not valid_sentences or not sentence_embeddings:
        return data[:max(1, len(data) - 1)]

    # Calculate cosine similarity
    similarities = []
    for s_embed in sentence_embeddings:
        try:
            sim = cosine_similarity(doc_embedding.reshape(1, -1), s_embed.reshape(1, -1))[0][0]
            similarities.append(sim)
        except:
            similarities.append(0)

    # Find the most similar sentence
    most_similar_idx = np.argmax(similarities)
    initial_output = valid_sentences[most_similar_idx]

    Output = initial_output

    # Check if the initial output meets the length condition
    if len(Output) < len(data):
        return Output

    # Try to find any valid sentence shorter than the input
    shorter_options = [s for s in valid_sentences if len(s) < len(data)]

    if shorter_options:
        shorter_similarities = []
        for s in shorter_options:
            try:
                emb = get_sentence_embedding(s)
                if not np.all(emb == 0):
                    sim = cosine_similarity(doc_embedding.reshape(1, -1), emb.reshape(1, -1))[0][0]
                    shorter_similarities.append(sim)
                else:
                    shorter_similarities.append(0)
            except:
                shorter_similarities.append(0)
        
        if shorter_similarities:
            Output = shorter_options[np.argmax(shorter_similarities)]
            if len(Output) < len(data):
                return Output
    
    # Final fallback: truncate the original data
    truncated_output = data[:max(1, len(data) - 1)]
    
    # Add ellipsis if truncation is significant
    if len(data) > 20 and len(truncated_output) <= len(data) * 0.8:
        truncated_output = truncated_output.strip() + "..."
        if len(truncated_output) >= len(data):
            truncated_output = data[:max(1, len(data) - 1)]
    else:
        truncated_output = truncated_output.strip()

    if len(truncated_output) < len(data):
        return truncated_output
    else:
        return data[:max(1, len(data) - 1)]