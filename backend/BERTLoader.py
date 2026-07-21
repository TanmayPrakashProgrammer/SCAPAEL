# backend/BERTLoader.py
import warnings
import logging
import os

# Suppress warnings
warnings.filterwarnings('ignore')
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Disable transformers logging
logging.getLogger("transformers").setLevel(logging.ERROR)

try:
    from transformers import BertTokenizer, BertModel
    import torch
    import numpy as np
    
    # Load once at module level
    print("Loading BERT model... (this happens only once)")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    model.eval()
    print("BERT model loaded successfully!")
    
except Exception as e:
    print(f"Error loading BERT: {e}")
    # Fallback to dummy model if needed
    tokenizer = None
    model = None