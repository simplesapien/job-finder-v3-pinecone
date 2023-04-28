# from dotenv import load_dotenv
# import pinecone

# pinecone.deinit()
# pinecone.init(api_key=load_dotenv("PINECONE_API"))

# INDEX_NAME = "job_postings"


# def create_index():
#     if INDEX_NAME not in pinecone.list_indexes():
#         pinecone.create_index(index_name=INDEX_NAME, metric="cosine", shards=1)


# def delete_index():
#     if INDEX_NAME in pinecone.list_indexes():
#         pinecone.deinit_index(index_name=INDEX_NAME)


# def upsert_item(item_id, item_vector):
#     pinecone_namespace = pinecone.Namespace(index_name=INDEX_NAME)
#     pinecone_namespace.upsert_item(item_id, item_vector)


# def query_item(item_vector, top_k=10):
#     pinecone_namespace = pinecone.Namespace(index_name=INDEX_NAME)
#     results = pinecone_namespace.fetch_top_k_nearest(item_vector, k=top_k)
#     return results


# def deinit_pinecone():
#     pinecone.deinit()
