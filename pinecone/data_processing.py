# import json
# import tensorflow as tf
# import tensorflow_hub as hub

# embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


# def preprocess_data(job_postings):
#     job_data = []
#     for posting in job_postings:
#         job_data.append(json.dumps(posting))

#     job_vectors = embed(job_data).numpy()

#     return job_vectors
